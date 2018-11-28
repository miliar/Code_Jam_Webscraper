/* Author :: Kaushik */

//STL includes
#include <vector>
#include <algorithm>
#include <list>
#include <map>
#include <deque>
#include <queue>
#include <set>
#include <stack>
#include <string>

//C includes
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <ctime>

//Other includes
#include <iomanip>
#include <iostream>
#include <sstream>
#include <fstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <tr1/random>
#include <tr1/unordered_map>

using namespace std;
using namespace std::tr1;

#define FOR(i,a,b) 	for(int i= (int )a ; i < (int )b ; ++i) 
#define REP(i,n) 	FOR(i,0,n)
#define V(x) 		vector< x >
#define PB 			push_back
#define ALL(x) 		x.begin(),x.end()
#define SORT(x) 	sort(ALL(x))
#define fill(a,v) 	memset(a, v, sizeof(a))
#define PRINT(x)    cout << #x << " " << x << endl
#define S(N)		scanf("%d",&N)
#define sqr(x)  	((x)*(x))
#define gcd  __gcd
#define mp make_pair

//Constants
const long double MPI = 3.14159265358979323846264338;
const long double E   = 2.71828182845904523536028747;
const int 		  INF = (int) 1e9;

typedef pair<int,int>   PI;
typedef pair<int,PI>    TRI;
typedef V( int )        VI;
typedef V( PI  )        VII;
typedef V( string )     VS;
typedef long long       ll;

ll nll(){ll a;cin>>a;return a;}
int ni(){int a;cin>>a;return a;}


#define maxn 128
long double wp[maxn],owp[maxn],oowp[maxn];
char grid[maxn][maxn];
int gc[maxn];
				int Gw[maxn],Gl[maxn];

int main()
{
		int kases;
		S(kases);
		for(int kase = 1;kase <= kases;kase++)
		{
				printf("Case #%d:\n",kase);
				REP(i,maxn)wp[i]=owp[i]=oowp[i]=0.0;
				REP(i,maxn)Gw[i]=Gl[i]=0;
				int n;
				S(n);
				REP(i,maxn)REP(j,maxn)grid[i][j]='\0';
				REP(i,n)scanf("%s",grid[i]);
				REP(i,n)
				{
						int gw=0,gl=0;
						REP(j,n)
						{
								if(grid[i][j]=='1')gw++,Gw[i]++;
								if(grid[i][j]=='0')gl++,Gl[i]++;
						}
						long double wins = gw,loss = gl;
						wp[i] = wins*1.0/((wins+loss*1.0)*1.0);
				}
				REP(i,n)gc[i]=0;
				REP(i,n)
				{
						REP(j,n)
						{
								if(grid[i][j]=='1' || grid[i][j]=='0')
								{
										long double tmp=0;
										if(grid[i][j]=='0')
										{
												tmp = (Gw[j]-1)*1.0/((Gw[j]+Gl[j]-1)*1.0);
										}
										else
												tmp = (Gw[j])*1.0/((Gw[j]+Gl[j]-1)*1.0);
										owp[i]+=(tmp);
										gc[i]++;
								}
						}
						owp[i] = owp[i]/(gc[i]*1.0);
				}
				REP(i,n)
				{
						oowp[i]=0;
						REP(j,n)
						{
								if(grid[i][j]!='.')
										oowp[i]+=owp[j];
						}
						oowp[i]=oowp[i]/(gc[i]*1.0);
				}
				REP(i,n)
				{
						long double ans = 0.25*wp[i] + 0.50*owp[i] + 0.25*oowp[i];
						printf("%.12Lf\n",ans);
				}
		}
		return EXIT_SUCCESS;
}
