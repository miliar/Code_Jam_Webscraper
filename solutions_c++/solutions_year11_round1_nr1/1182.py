#include <cstdio>
#include <map>
#include <string>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <set>


using namespace std;

long long int caso,T,Pg,Pd,N;


long long int mdc(long long int a,long long int b){


	if(b==0) return a;

	return mdc(b,a%b);


}


int main(void){


	scanf("%lld",&T);

	for(int i=0;i<T;i++){
		
		scanf("%lld %lld %lld",&N,&Pd,&Pg);

		if(Pg==0&&Pd!=0){
			printf("Case #%lld: Broken\n",++caso);		
			continue;
		}

		if(Pg==100&&Pd!=100){
			printf("Case #%lld: Broken\n",++caso);		
			continue;
		}

		


		int Wd=Pd;
		int D=100;

		int r=mdc(Wd,D);

		Wd/=r;
		D/=r;
		
		int Wg=Pg;
		int G=100;

		r=mdc(Wg,G);

		Wg/=r;
		G/=r;

		if(D>N) printf("Case #%lld: Broken\n",++caso);
		else printf("Case #%lld: Possible\n",++caso);

	
	}


	return 0;


}
