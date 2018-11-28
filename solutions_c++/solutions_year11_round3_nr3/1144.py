#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;

long long int f[10001];

int gcd(long long int a,long long int b){
	long long int r;
	while(b!=0){
	  r = a%b;
	  a = b;
	  b = r;
	}
	return a;
}

int main(){
  
  int T,N,L,H,certo,teste=1,i;
  
  long long int g;
  
  long long int t;
  
  scanf("%d",&T);
  
  
  while(T--){
		
		cin >> N >> L >> H;
		
		
		g = 0;
		for(i=0;i<N;i++){
			cin >> f[i];
			g = gcd(f[i],g);
		}
		
		
		for(t=L;t<=H;t++){
			certo = 1;
			for(i=0;i<N;i++){
				if((t>f[i] && t%f[i]!=0) ||(t<f[i] && f[i]%t!=0)){
					certo = 0;
					break;
				}
		  }
			if(certo) break;
		}
		
		printf("Case #%d: ", teste++);
		if(certo)
		 cout << t << endl; 
		else
		  printf("NO\n");
		
	
	}
	
	
	return 0;
}
