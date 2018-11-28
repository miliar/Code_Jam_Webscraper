#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <ctime>
#include <cassert>

using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
#define FOR(k,a,b) for(LL k(a); k < (b); ++k)
#define FORD(k,a,b) for(int k(b-1); k >= (a); --k)
#define REP(k,a) for(int k=0; k < (a); ++k)
#define ABS(a) ((a)>0?(a):-(a))

int main()
{
#ifdef HOME
	clock_t start=clock();
	freopen ("C-small-attempt3.in","r",stdin);
	freopen ("C-small-attempt3.out","w",stdout);
	//freopen ("in.txt","r",stdin);
	//freopen ("out.txt","w",stdout);
#endif
	int T,N;
	scanf("%d",&T);
	double epsilon=1e-9;
	
	FOR(testcase,1,T+1)
	{
		scanf("%d",&N);
		vector<int> v(N);
		vector<double> h(N);
		FOR(i,0,N-1)
		{
			scanf("%d",&(v[i]));
			--v[i];
		}
		bool check=true;
		REP(i,N)
		{
			FOR(j,i,v[i]-1)
			{
				if(v[j]<v[j+1] && j+1<v[j])
					check=false;
			}
		}
		printf("Case #%d:",testcase);
		if(check)
		{
			bool ok=false;
			clock_t curr=clock();
			do 
			{
				if(0.001*(clock()-curr)>6)
					break;
				ok=true;
				REP(i,N)
					h[i]=rand()%100;
				REP(i,N-1)
				{
					FOR(j,i+1,v[i])
					{
						if((h[j]-h[i])/(j-i)>(h[v[i]]-h[i])/(v[i]-i)-epsilon)
						{
							ok=false;
							break;
						}
						if(!ok)
							break;
					}
					FOR(j,v[i]+1,N)
					{
						if((h[j]-h[i])/(j-i)>(h[v[i]]-h[i])/(v[i]-i))
						{
							ok=false;
							break;
						}
						if(!ok)
							break;
					}
				}
			
			} while (!ok);
			REP(i,N)
			{
				printf(" %d",(int)h[i]);
			}
		}
		else
		{
			printf(" Impossible");
		}
		printf("\n");
	}
	
#ifdef HOME
	fprintf(stderr,"time=%.3lfsec\n",0.001*(clock()-start));
#endif
	return 0;
} 