#include <iostream>
#include <cassert>
#include <cstdio>
#include <algorithm>
using namespace std;

#define REP(i,n) for (int i=0;i<(n);i++)

int pr[100];
int tmax;
int f[10002][10002];
int g[10001];

int main()
{
	int tc;
	cin >> tc;
	for (int tno=1;tno<=tc;tno++)
	{
		int p,q;
		cin >> p >> q;
		memset(g, 0, sizeof(g));
		REP(i,q) {
			cin >> pr[i];
			g[pr[i]]=1;
		}
		for (int i=0;i<=p+1;i++)
			for (int j=0;j<=p+1;j++)
				f[i][j]=0;


		for (int sz=1;sz<=p;sz++) {
			for (int i=1;i<=p-sz+1;i++) {
				int j=i+sz-1;
				int minv=100000000;
				for (int k=i;k<=j;k++) {
					if ( !g[k] ) continue;
					int scost = f[i][k-1]+f[k+1][j]+j-i;
					if (scost<minv) minv=scost;
				}
				if (minv==100000000) continue;
				f[i][j]=minv;
			}
		}

		printf("Case #%d: %d\n", tno,f[1][p]);
	}
	return 0;
}