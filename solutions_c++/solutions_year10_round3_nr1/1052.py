#include<stdio.h>
using namespace std;
int t,ok,n,ar[1000][2];
int main(){
	scanf("%d",&t);
	for(int k=1;k<=t;++k){
		ok=0;
		scanf("%d",&n);
		for(int i=0;i<n;++i)scanf("%d%d",&ar[i][0],&ar[i][1]);
		for(int i=0;i<n;++i) for(int j=i+1;j<n;++j)
			if(ar[i][0]>ar[j][0] && ar[i][1]<ar[j][1]) ++ok; 
			else if(ar[i][0]<ar[j][0] && ar[i][1]>ar[j][1]) ++ok; 
		printf("Case #%d: %d\n",k,ok);
	}
	return 0;
}
