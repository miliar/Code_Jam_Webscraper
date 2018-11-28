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

char D[]="yhesocvxduiglbkrztnwjpfmaq";

int main(){
	freopen("input.in","r",stdin);
#ifndef _DEBUG 
	freopen ("output.txt","w",stdout);
#endif
	clock_t start = clock();

	int T;
	scanf("%d",&T);
	char S[1000];
	cin.getline(S,1000);
	
	FOR(tT,0,T){
		cin.getline(S,1000);
		for(int i=0;S[i]!=0;i++){
			if(S[i]!=' '){
				S[i]=D[S[i]-'a'];
			}
		}
		printf("Case #%d: %s\n",tT+1,S);		
	}
	
	
#ifdef _DEBUG 	
	printf("Time elapsed: %f\n", ((double)clock() - start) / CLOCKS_PER_SEC);
#endif
	return 0;
}





