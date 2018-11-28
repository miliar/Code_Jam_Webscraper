#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
#include<cstring>
#include <string>

//#include <iostream>

using namespace std;

#define REP(i,v)for(int i=0;i<(v);++i)
#define FOR(i,x,v)for(int i=x;i<=(v);++i)
#define FORD(i,x,v)for(int i=x;i>=(v);--i)
#define VAR(v,n) __typeof(n) v = (n)
#define FOREACH(i,c) for(VAR(i,(c).begin()); i != (c).end(); ++i)
#define ALL(c) (c).begin(), c.end()
#define PB push_back
#define SZ size
#define MP make_pair
#define FI first
#define SE second
#define CL clear()
#define RS resize
#define INFTY 1000000001
#define EPS 10e-9
#define SIZE(x) ((int)(x).size())

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef pair<int,int> PII;
typedef long long LL;
typedef vector<string> VS;

void show(PII p)
{printf("(%d %d)\n",p.FI,p.SE);}

void show(VI e)
{REP(i,SIZE(e)) printf("%d ",e[i]); printf("\n");}

void show(vector<PII> e)
{REP(i,SIZE(e)) printf("(%d %d) ",e[i].FI,e[i].SE); printf("\n");}

void show(VS e)
{REP(i,SIZE(e)) printf("%s\n",e[i].c_str());}

void show(VVI e)
{REP(i,SIZE(e)) show(e[i]);}

const int MAX_N = 101;
int scores[MAX_N][MAX_N], won[MAX_N], lost[MAX_N];
double wp[MAX_N], owp[MAX_N], oowp[MAX_N];



int main()
{
	int t, w, tot, n;
	char z;
	double o;
	

	scanf("%d", &t);
	REP(i,t)
	{
		printf("Case #%d:\n", i+1);
		scanf("%d\n", &n);

		REP(j,n)
		{
			won[j] = 0;
			lost[j] = 0;

			REP(k,n)
			{
				scanf("%c", &z);
				if(z == '.') 
				{
					scores[j][k] = -1;
				}
				else if(z == '1')
				{
					won[j]++;
					scores[j][k] = 1;
				}
				else
				{
					lost[j]++;
					scores[j][k] = 0;
				}
			}
			wp[j] = (double) won[j]/(won[j]+lost[j]);
			scanf("\n");
		}
/*
		printf("won, lost, wp:\n");
		REP(j,n)
			printf("%d, %d, %lf\n", won[j], lost[j], wp[j]);
*/

		// owp
		/*
		REP(j,n) // akt
		{
			owp[j] = 0;
			REP(k,n)
			{
				w = 0;
				tot = 0;
				REP(l, n)
				{
					if(l != j)
					{

						if(scores[k][l] == 1)
						{	
							w++;
							tot++;	
						}
						else if(scores[k][l] == 0)
							tot++;
					}

				}
				printf("owp for %d: win = %d, total = %d\n", j,w, tot);
				owp[j] = owp[j] + (double) w/tot;
			}
		}
		*/

		// owp
		REP(j,n)
		{
			owp[j] = 0;
			//printf("owp: j == %d\n", j);
			REP(k,n)
			{
				if(scores[j][k] > -1) // grali ze sobą
				{
					w = won[k];
					tot = won[k] + lost[k];
					if(scores[k][j] == 1)
					{
						w--;
						tot--;
					}
					else if(scores[k][j] == 0)
						tot--;
					//printf("\tk == %d, w = %d, tot = %d\n", k, w, tot);
						owp[j] += (double) w/tot;
				}
			}
			owp[j] = (double) owp[j]/(won[j]+lost[j]);
		}
		/*
		printf("owp:\n");
		REP(j,n)
			printf("%lf\n", owp[j]);
*/
		// oowp
		// wiersz
		REP(j,n)
		{
			tot = 0;
			o = 0;
			REP(k,n)
			{
				if(scores[j][k] >= 0)
				{		
					o+= owp[k];
					tot++;
				}
			}
			oowp[j] = (double) o/tot;
		}
		
		REP(j,n)
		{
			printf("%lf\n", 0.25*wp[j] + 0.5*owp[j] + 0.25*oowp[j]);
		}
	}

	return 0;
}

