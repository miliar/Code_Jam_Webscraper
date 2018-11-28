#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <math.h>
#include <queue>
#include <list>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <fstream>
using namespace std;

#define abs(A) (((A)>=0)?(A):(-(A)))
#define present(c,x) (find(c.begin(),c.end(),x) != (c).end())
#define pb push_back
template<class A, class B> A cvt(B x) { stringstream s; s<<x; A r; s>>r; return r; }
typedef long long int64;

int tests;
int n,k;
int p[100][25];
int adj[100][100];

int vis[100],prev[100];

int dfs(int x) {
	//cerr << "at " << x << endl;
	if (x==-1) return 1;
	if (vis[x]) return 0;
	vis[x]=1;
	for (int i=0;i<n;i++) {
		if (adj[x][i] && dfs(prev[i])) {
			prev[i]=x;
			return 1;
		}
	}
	return 0;
}

int dp[1<<16];

int solve(int mask) {
	if (dp[mask]!=-1) return dp[mask];

	if (mask==0) return 0;
	int st=0;

	int done=1;
	for (int i=0;i<n;i++) if ((mask&(1<<i))>0) {
		st++;
		for (int j=i+1;j<n;j++) if ((mask&(1<<j))>0) {
			if (adj[i][j]==0) done=0;
		}
	}
	if (done) { dp[mask]=1; return 1; }

	int best=st;
	for (int m=(mask-1)&mask;m>0;m=(m-1)&mask) {
		int r1=solve(m);
		int r2=solve(mask^m);
		if (r1!=-1 && r2!=-1) {
			if (r1+r2<best) best=r1+r2;
		}
	}
	dp[mask]=best;

	return best;
}

int main() {
	ifstream fin("C-small-attempt1.in");
	//ifstream fin("C.in");
	FILE *fout=fopen("C-small-attempt1.out","w");
	//FILE *fout=stdout;
	fin >> tests;
	for (int test=1;test<=tests;test++) {
		cerr << test << endl;
		fin >> n >> k;
		for (int i=0;i<n;i++) {
			for (int j=0;j<k;j++) {
				fin >> p[i][j];
			}
		}

		memset(adj,0,sizeof(adj));
		for (int i=0;i<n;i++) {
			for (int j=i+1;j<n;j++) {
				if (p[i][0]==p[j][0]) {  }
				else if (p[i][0]<p[j][0]) {
					adj[i][j]=1;
					for (int d=0;d<k;d++) {
						if (p[i][d]>=p[j][d]) adj[i][j]=0;
					}
				} else {
					adj[i][j]=1;
					for (int d=0;d<k;d++) {
						if (p[i][d]<=p[j][d]) adj[i][j]=0;
					}
				}
			}
		}

		/*//bipartite matching
		memset(prev,-1,sizeof(prev));
		int f=0;
		for (int i=0;i<n;i++) {
			//cerr << "X" << endl;
			memset(vis,0,sizeof(vis));
			if (dfs(i)) f++;
		}*/

		//cerr << "B"<<endl;
		memset(dp,-1,sizeof(dp));
		fprintf(fout,"Case #%d: %d\n",test,solve((1<<n)-1));
	}
    return 0;
}
