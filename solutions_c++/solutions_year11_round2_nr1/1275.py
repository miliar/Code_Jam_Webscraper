#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <deque>
#include <string>
#include <cmath>
#include <set>
#include <queue>
#include <map>
#include <ctime>
#define pb push_back 
#define mp make_pair 
using namespace std;
int n, t, w[101][101], g[101]; double wp[101], owp[101], oowp[101]; char ch;
int main()
{
	scanf("%d", &t);
	for (int T=0; T<t; T++)
	{
		scanf("%d", &n);
		for (int i=0; i<n; i++)
		{
			scanf("%c", &ch);
			for (int j=0; j<n; j++)
			{
				scanf("%c", &ch);
				if (ch=='.') w[i][j]=-1; else if (ch=='1') w[i][j]=1; else w[i][j]=0;
			}
		}
		for (int i=0; i<n; i++)
		{
			g[i]=0; wp[i]=0;
			for (int j=0; j<n; j++)
				if (w[i][j]+1)
				{
					if (w[i][j]) wp[i]++; g[i]++;
				}
			wp[i]/=g[i];
		}
		for (int i=0; i<n; i++)
		{
			owp[i]=0;
			for (int j=0; j<n; j++)
				if (w[i][j]+1)
				{
					if (w[i][j]) owp[i]+=(wp[j]*g[j])/(g[j]-1); else owp[i]+=(wp[j]*g[j]-1)/(g[j]-1);
				}
			owp[i]/=g[i];
		}
		for (int i=0; i<n; i++)
		{
			oowp[i]=0;
			for (int j=0; j<n; j++)
				if (w[i][j]+1) oowp[i]+=owp[j];
			oowp[i]/=g[i];
		}
		printf("Case #%d:\n", T+1);
		for (int i=0; i<n; i++)
			printf("%.9lf\n", 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
	}
	return 0;
}
