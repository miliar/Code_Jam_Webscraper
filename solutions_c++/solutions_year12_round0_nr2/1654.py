#include<iostream>
#include<cmath>
#include<set>
#include<vector>
#include<list>
#include<map>
#include<algorithm>
#include<stdio.h>
#include<string.h>
#include<stack>
#include<queue>
#include<climits>
#include <string>
#include <sstream>

typedef unsigned long long int ULONG;
typedef long long int LONG;
typedef unsigned int UINT;

using namespace std;
#define FOR(i,a,b) for(int i=a;i<b;++i)

#ifndef ONLINE_JUDGE
#include <time.h>
#endif



int main(){
	freopen("input.in","r",stdin);
#ifndef _DEBUG 
	freopen ("output.txt","w",stdout);
#endif
	clock_t start = clock();

	int A[101];

	int T;
	scanf("%d",&T);	
	FOR(tT,0,T){
		int N,S,P,M=0;
		scanf("%d%d%d",&N,&S,&P);
		FOR(i,0,N)scanf("%d",&A[i]);


		FOR(i,0,N){
			int F=0;
			for(int a=10;a>=P;a--){
				for(int b=a;b>=a-2 && b>=0;b--){
					for(int c=a;c>=a-2 && c>=0;c--){
						//abs(a-b)==2 || abs(a-c)==2 || abs(b-c)==2
						if(a+b+c==A[i]){
							if(abs(a-b)==2 || abs(a-c)==2 || abs(b-c)==2){
								F=2;
							}else{
								F=1;
								goto END;
							}
						}
					}
				}
			}
END:
			if(F==2)S--;
			if(F!=0)M++;
		}

		printf("Case #%d: %d\n",tT+1,(S<0?M+S:M));		
	}
	
#ifdef _DEBUG 	
	printf("Time elapsed: %f\n", ((double)clock() - start) / CLOCKS_PER_SEC);
#endif
	return 0;
}





