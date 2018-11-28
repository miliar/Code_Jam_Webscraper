#include<iostream>
#include<cstdio>
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
using namespace std;

int main(){
	int t,i,j,k,l,m;
	int N,L,H;
	int A[1000];
	scanf("%d",&t);
	l=1;
	while(l<=t){
		printf("Case #%d: ",l++);
		scanf("%d%d%d",&N,&L,&H);
		for(i=0;i<N;i++) scanf("%d",&A[i]);
		i=L;
		while(i<=H){
			j=i;
			k=0;
			for(m=0;m<N;m++){
				if(max(i,A[m])%min(i,A[m])==0) k++;
			}
			if(k==N){
				break;
			}else{
				j=-1;
			}
			i++;
		}
		if(j==-1) printf("NO\n");
		else printf("%d\n",j);
	}
	return 0;
}
