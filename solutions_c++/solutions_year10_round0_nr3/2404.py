#include <fstream>
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main() {

	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt1.out", "w", stdout);
	int R, K ;
    int T,N,i=0,j=0,k=0,t=0,earn=0,temp=0,r=0,count=0;
	int G[1001];
	scanf("%d", &T);
	for (t = 0; t < T; ++t,i=0,earn=0,count=0) {
	scanf("%d", &R);
	scanf("%d", &K);
	scanf("%d", &N);
	for(i=0;i<N;i++) scanf("%d", &G[i]);
	for (r = 0,i=0; r < R; ++r,count=0) {
	 do{
	 if((G[i]+count>K)||(i==N))
	   break;
	 count=G[i]+count;
	 i=i+1;
	 }while(count<K);

     for (j = 0; j < i; ++j) {
	   temp=G[0];
	   for(k = 0; k < N; ++k){
		if(k==N-1)
		G[k]=temp;
		else
		G[k]=G[k+1];
		}
	 }
	 i=0;
	 earn=earn+count;
	}
printf("Case #%d: %d\n",t+1,earn);
	}
	
//	system("pause");
	
}


