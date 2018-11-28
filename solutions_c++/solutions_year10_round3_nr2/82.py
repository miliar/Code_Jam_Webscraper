#include <iostream>
#include <cstdio>
#include <queue>
#include <list>
#include <cstring>
#include <cmath>
#include <cstring>

using namespace std;

int main(){

	long cc,tt;
	long l,p,c;
	double m;
	long lm;
	long times;
	long i;
	scanf("%d",&tt);
	for(cc=0;cc<tt;cc++){
		scanf("%d%d%d",&l,&p,&c);
		
		times=0;
		while((double)p/(double)l>c+1e-8){
			m=sqrt((double)p*l);
			lm=(long)(m+1e-6);
			if( max((double)p/(double)(lm),(double)(lm)/(double)l)>max((double)p/(double)(lm+1),(double)(lm+1)/(double)l) )
				lm++;
			
			if((double)p/(double)lm>(double)lm/(double)l)
				l=lm;
			else
				p=lm;
			times++;
		}

		printf("Case #%d: %d\n",cc+1,times);
	}
	return 0;
}