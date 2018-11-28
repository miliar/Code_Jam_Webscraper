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

#define L (2000000+1)



int main(){
	freopen("input.in","r",stdin);
#ifndef _DEBUG 
	freopen ("output.txt","w",stdout);
#endif
	clock_t start = clock();

	
	int T;
	scanf("%d",&T);	
	FOR(tT,0,T){
		int A,B;
		scanf("%d%d",&A,&B);

		LONG S=0;
		int T10=1;
		for(int t=A;t!=0;t/=10,T10*=10);
		
		for(int i=A;i<B;i++){
			map<int,int> C;
			for(int k=10;k<T10;k*=10){				
				int t=(i%k)*(T10/k)+i/k;
				if(t>i && t<=B && C[t]==0){
					S++;
					C[t]=1;
				}
			}
		}
		printf("Case #%d: %lld\n",tT+1,S);		
	}
	
#ifdef _DEBUG 	
	printf("Time elapsed: %f\n", ((double)clock() - start) / CLOCKS_PER_SEC);
#endif
	return 0;
}





