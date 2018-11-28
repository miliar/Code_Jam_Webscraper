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

int t,n,m;
bool pos;

int main()
{
	scanf("%d",&t);
	FORN(i,t)
	{
		scanf("%d%d",&n,&m);
		string mat[n];
		FORN(j,n)
			cin >> mat[j];
		pos = true;
		FORN(j,n)
		{
			FORN(k,m)
				if (mat[j][k] == '#')
					if ((j+1 < n) && (k+1 < m))
					{
						if ((mat[j][k] == '#') && (mat[j+1][k] == '#') && (mat[j][k+1] == '#') && (mat[j+1][k+1] == '#'))
						{
							mat[j][k] = '/';
							mat[j+1][k+1] = '/';
							mat[j+1][k] = (char)92;
							mat[j][k+1] = (char)92;
						}
						else
						{
							pos = false;
							break;
						}
					}
					else
					{
						pos = false;
						break;
					}
			if (!pos)
				break;
		}
		printf("Case #%d:\n",i+1);
		if (pos)
			FORN(j,n)
				cout << mat[j] << endl;
		else
			printf("Impossible\n");
	}
}
