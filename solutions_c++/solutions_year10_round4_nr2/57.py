#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <vector>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <map>

#define y0 y63475625
#define y1 y28435
#define sqr(x) ((x)*(x))

using namespace std;

typedef long long ll;
typedef long double ld;

const double pi = acos(-1.0);

int p;
int miss[2024];
int m[2024];
int c[11][1024];

int dp[2024][11][11];

int dfs(int l,int q,int w)
{
	if (q==0)dp[l][q][w]=-2;else
	if (dp[l][q][w]==-1){
		bool kpyto=true;
		for (int i=l;i<l+(1<<q);i++)if (m[i]+w<p){
			kpyto=false;
			break;
		}
		if (kpyto)dp[l][q][w]=0; else {
			kpyto=true;
			for (int i=l;i<l+(1<<q);i++)if (m[i]+q+w<p){
				kpyto=false;
				break;
			}
			if (!kpyto){
				dp[l][q][w]=-2;
			} else {
				if (q==1){
					dp[l][q][w]=c[q][l>>q];
				} else {
					int l0,r0,l1,r1;
					l0=dfs(l,q-1,w);
					r0=dfs(l+(1<<(q-1)),q-1,w);
					l1=dfs(l,q-1,w+1);
					r1=dfs(l+(1<<(q-1)),q-1,w+1);
					if (l0<0||r0<0){
						if (l1<0||r1<0){
							dp[l][q][w]=-2;
						} else dp[l][q][w]=c[q][l>>q]+l1+r1;
					} else
					if (l1<0||r1<0){
						dp[l][q][w]=l0+r0;
					} else dp[l][q][w]=min(c[q][l>>q]+l1+r1,l0+r0);
				}
			}
		}
	}
//	cerr << l << ' ' << q << ' ' << w << ' ' << dp[l][q][w] << endl;
	return dp[l][q][w];
}

int main()
{
	int T;
	cin >> T;
	
	for (int I=0;I<T;I++){
		memset(dp,255,sizeof(dp));
		cin >> p;
		memset(c,0,sizeof(c));
		for (int i=0;i<(1<<p);i++)cin >> m[i];
		for (int i=p-1;i>=0;i--){
			for (int j=0;j<(1<<i);j++)cin >> c[p-i][j];
		}
		//dfs(0,p,0);
		cout << "Case #" << I+1 << ": " << dfs(0,p,0) << endl;
		//return 0;
	}
	return 0;
}
