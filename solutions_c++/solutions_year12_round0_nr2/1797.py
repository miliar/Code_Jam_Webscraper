#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;

int P,RET[40];
int solve(int N)
{
	switch(N%3)
	{
		case 0: if(N/3 >= P) return 2;
				if(N/3 + 1 >= P && N >= 3) return 3;
				return 0;
				
		case 1: if((N+2)/3 >= P) return 2;
				return 0;
			
		case 2: if((N+1)/3 >= P) return 2;
				if((N+4)/3 >= P && N >= 2) return 3;
				return 0;
	}
	return 0;
}

int main(){
	int T,N,S;
	int i,j,k;
	int A[110];
	
	j = 1;
	scanf("%d",&T);
	while(T--){
		scanf("%d%d%d",&N,&S,&P);
		for(i=0;i<=30;i++)
			RET[i] = solve(i);
		
		for(i=0;i<N;i++) scanf("%d",&A[i]);
		sort(A,A+N);
		
		for(i=N-1,k=0;i>=0;i--){
			S -= (RET[A[i]]%2);
			if(S < 0) 
				break;
			k += (RET[A[i]]/2);
		}
		printf("Case #%d: %d\n",j++,k);
	}
	return 0;	
}
