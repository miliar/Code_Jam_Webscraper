#include <cmath>
#include <iostream>
#include <cstdio>

#include <list>
#include <cstring>
#include <queue>

using namespace std;

int main(){

	long l,ll,z,tt,p,c,m,;
	long times;
	long i;
	scanf("%d",&tt);
	for(z=0;z<tt;z++)
	{
		scanf("%d%d%d",&l,&p,&c);
		times=0;

		while( (double)p / (double)l > c+1e-8 )
		{
			m=sqrt((double)p*l);
			ll=(long) (m+1e-6);
			if( max((double)p/(double)(ll) , (double)(ll)/(double)l) > max((double)p/(double)(ll+1) , (double)(ll+1)/(double)l) )
				ll++;

			if((double)p/(double)ll>(double)ll/(double)l)
				l=ll;
			else
				p=ll;
			times++;
		}

		printf("Case #%d: %d\n",z+1,times);
	}
	return 0;
}


