#include <iostream>
#include <stdio.h>
#include <queue>
#include <vector>
#include <algorithm>
#include <set>
#include <math.h>
#include <memory.h>

using namespace std;

#define FOR(i,b) for (int i = 0; i < (b); i++)
#define MP(A,B) make_pair(A,B)

char ch[200][200];
int N;

long long games[200];
long long win[200];
long long loose[200];


pair<long long , long long> ven[300];

long long C;
long long D;

bool CanDo(long double seconds)
{
	long double firstpos = ven[0].first-seconds;
	long double lastpos = firstpos+D*(ven[0].second-1);
	
	if(fabs(ven[0].first-lastpos)>seconds)
	{
		return false;
	}
	else
	{
		for(int n=1;n<C;n++)
		{
			firstpos = max(lastpos+D,ven[n].first-seconds);
			lastpos = firstpos+D*(ven[n].second-1);
			
			if(fabs(ven[n].first-lastpos)>seconds)
			{
				return false;
			}
		}
	}
	
	return true;
}

int main()
{
	int T;
	
	scanf("%d",&T);
	
	FOR(t,T)
	{
		scanf("%lld %lld",&C,&D);
		
		FOR(c,C)
		{
			long long a;
			long long b;
			scanf("%lld %lld",&a,&b);
			ven[c]= MP(a,b);
		}
		
		// sort vendor by position
		sort(ven,ven+C);
		
		
		long double start = 1.0e10;
		long double end =0;
		
		
		while(start-end>1.0e-9)
		{
			long double mid = (start+end)/2.0;
			
			//cout<<"mid : "<<mid<<endl;
			
			if(CanDo(mid))
			{
				start = mid;
			}
			else
			{
				end = mid;
			}
		}
		
		printf("Case #%d: %.9Lf\n",t+1,start);
		
	}
}