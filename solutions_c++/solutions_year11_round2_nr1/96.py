#include <map>
#include <set>
#include <list>
#include <cmath>
#include <stack>
#include <queue>
#include <vector>
#include <cstdio>
#include <string>
#include <bitset>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <sstream>
#include <iostream>
#include <algorithm>
#define sqr(x) ((x)*(x))
#define ABS(x) ((x<0)?(-(x)):(x))
#define eps (1e-9)
#define mp make_pair
#define pb push_back
#define Pair pair<int,int>
#define xx first
#define yy second
#define equal(a,b) (ABS(a-b)<eps)
using namespace std;

template<class T> string tostring(T x) { ostringstream out; out<<x; return out.str();}
long long toint(string s) { istringstream in(s); long long x; in>>x; return x; }

int dx[8]={0, 0, 1,-1, 1, 1,-1,-1};
int dy[8]={1,-1, 0, 0,-1, 1,-1, 1};
int kx[8]={1, 1,-1,-1, 2, 2,-2,-2};
int ky[8]={2,-2, 2,-2, 1,-1, 1,-1};

/////////////////////////////////////////////////////////////////////////////////////////////////////
string testname="a-large";

char s[200][200];
void run_sol(int casenr){
	int n;
	scanf("%d",&n);
	for (int i=0;i<n;i++)
		scanf("%s",s[i]);
	printf("Case #%d:\n",casenr);
	double wp[100],owp[100],oowp[100];
	for (int i=0;i<n;i++){
		int tot=0;
		wp[i]=0.0;
		for (int j=0;j<n;j++){
			if (s[i][j]!='.') tot++;
			if (s[i][j]=='1') wp[i]+=1.0;
		}
		wp[i]/=tot;
	}
	for (int i=0;i<n;i++){
		owp[i]=0.0;
		int tot=0;
		for (int j=0;j<n;j++)
			if (s[i][j]!='.'){
				tot++;
				int tot1=0;
				double w=0.0;
				for (int k=0;k<n;k++){
					if (k==i) continue;
					if (s[j][k]!='.') tot1++;
					if (s[j][k]=='1') w+=1.0;
				}
				w/=tot1;
				owp[i]+=w;
			}
		owp[i]/=tot;
	}
	for (int i=0;i<n;i++){
		oowp[i]=0.0;
		int tot=0;
		for (int j=0;j<n;j++)
			if (s[i][j]!='.'){
				tot++;
				oowp[i]+=owp[j];
			}
		oowp[i]/=tot;
	}
//	printf("%lf %lf %lf\n",wp[0],owp[0],oowp[0]);
	for (int i=0;i<n;i++)
		printf("%.9lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
}
int main(){
	freopen((testname+".in").c_str(),"r",stdin);
	freopen((testname+".out").c_str(),"w",stdout);
	int T;
	scanf("%d",&T);
	for (int t=1;t<=T;t++)
		run_sol(t);
	return 0;
}
