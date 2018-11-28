#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <ctime>
#include <cstring>
#pragma comment(linker, "/STACK:16777216")
using namespace std;
#define pb push_back
#define ppb pop_back
#define pi 3.1415926535897932384626433832795028841971
#define mp make_pair
#define x first
#define y second
#define sqr(a) (a)*(a)
#define D(a,b) sqrt(((a).x-(b).x)*((a).x-(b).x)+((a).y-(b).y)*((a).y-(b).y))
#define pii pair<int,int>
#define pdd pair<double,double>
#define INF 1000000000
#define FOR(i,a,b) for (int _n(b), i(a); i <= _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))
#define rep(i,n) FOR(i,1,(n))
#define rept(i,n) FOR(i,0,(n)-1)
#define L(s) (int)((s).size())
#define C(a) memset((a),0,sizeof(a))
#define VI vector <int>
#define ll long long
int a,b,c,d,i,j,n,m,k,kolt;
bool mas[101][101],nmas[101][101];
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&kolt);
	rep(hod,kolt)
	{
		cerr<<hod<<endl;
		printf("Case #%d: ",hod);
		scanf("%d",&m);
		n=100;
		rept(i,m)
		{
			scanf("%d%d%d%d",&a,&b,&c,&d); --a; --b; --c; --d; if (a>c) swap(a,c); if (b>d) swap(b,d);
			FOR(x,a,c) FOR(y,b,d) mas[x][y]=1;
		}
		rept(h,INF)
		{
			bool ok=0;
			C(nmas);
			rept(i,n)
			{
				rept(j,n)
				{
					if (mas[i][j])
					{
						ok=1;
						if ((i && mas[i-1][j]) || (j && mas[i][j-1])) nmas[i][j]=1;
					} else
					{
						if (i && mas[i-1][j] && j && mas[i][j-1]) nmas[i][j]=1;
					}
				}
			}
			if (!ok)
			{
				printf("%d\n",h);
				break;
			}
			memcpy(mas,nmas,sizeof(nmas));
		}
	}
}
