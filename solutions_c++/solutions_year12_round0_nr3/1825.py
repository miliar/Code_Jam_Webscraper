#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>
#include <set>
#define MAX 2000000

using namespace std;
int T,K,A,B;
int count(int N)
{
	int i,k,M;
	set<int> s;
	for(i=10,k=0;i<K;i*=10){
		M = (N%i)*(K/i) + (N/i);
		if(M > N && M <= B && s.find(M) == s.end()){
			s.insert(M);
			k++;
		}
	}
	return k;
}

int main(){
	int i,j,k;
	
	j = 1;
	scanf("%d",&T);
	while(T--){
		scanf("%d%d",&A,&B);
		for(k = A,K = 1;k != 0; k /= 10) K *= 10; 	
		for(i=A,k=0;i<B;i++)
			k += count(i);
		printf("Case #%d: %d\n",j++,k);
	}
	return 0;
}
