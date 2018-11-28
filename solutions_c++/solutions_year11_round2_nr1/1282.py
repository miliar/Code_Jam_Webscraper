//darkstallion's template

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<string>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define popb pop_back
#define del erase
#define sz size
#define ins insert
#define FOR(a,b,c) for(int a = b; a < c; a++)
#define FORS(a,b,c) for(int a = b; a <= c; a++)
#define FORN(a,b) for(int a = 0; a < b; a++)
#define FORD(a,b,c) for (int a = b; a >= c; a--)
#define RES(a,b) memset(a,b,sizeof(a))
#define LL long long
#define PII pair<int,int>
#define PLL pair<long long,long long>
#define PDD pair<double,double>
#define PCC pair<char,char>
#define PSS pair<string,string>
using namespace std;

int t,n;
double win,tot,win2,tot2;

int main()
{
	scanf("%d",&t);
	FORN(i,t)
	{
		scanf("%d",&n);
		string mat[n];
		FORN(j,n)
			cin >> mat[j];
		double wp[n],owp[n],oowp[n];
		FORN(j,n)
		{
			win = 0;
			tot = 0;
			FORN(k,n)
				if (mat[j][k] == '1')
				{
					win++;
					tot++;
				}
				else if (mat[j][k] == '0')
					tot++;
			if (tot == 0)
				wp[j] = 0;
			else
				wp[j] = win/tot;
		}
		FORN(j,n)
		{
			win = 0;
			tot = 0;
			FORN(k,n)
				if (mat[j][k] != '.')
				{
					win2 = 0;
					tot2 = 0;
					FORN(l,n)
						if ((mat[k][l] != '.') && (l != j))
						{
							if (mat[k][l] == '1')
							{
								win2++;
								tot2++;
							}
							else
								tot2++;
						}
					if (tot2 != 0)
						win += win2/tot2;
					tot++;
				}
			if (tot == 0)
				owp[j] = 0;
			else
				owp[j] = win/tot;
		}
		FORN(j,n)
		{
			win = 0;
			tot = 0;
			FORN(k,n)
				if (mat[j][k] != '.')
				{
					win += owp[k];
					tot++;
				}
			if (tot == 0)
				oowp[j] = 0;
			else
				oowp[j] = win/tot;
		}
		printf("Case #%d:\n",i+1);
		FORN(j,n)
			printf("%lf\n",0.25*wp[j]+0.5*owp[j]+0.25*oowp[j]);
	}
}
