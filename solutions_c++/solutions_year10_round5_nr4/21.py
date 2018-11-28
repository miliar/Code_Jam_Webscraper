#include <stdio.h>
#define P 1000000007


int cnt;
int b;

int num[100];

void saiki(int n,int prev,int pos){
	if(n==0){
		int a[100];
		for(int i=0;i<pos;i++)a[i]=num[i];
		//check
		for(;;){
			bool allzero=true;
			bool check[72]={0};
			for(int i=0;i<pos;i++){
				if(a[i]!=0){
					allzero=false;
					int d=a[i]%b;
					if(check[d]==1)return;
					check[d]=1;
					a[i]/=b;
				}
			}
			if(allzero)break;
		}
		cnt++;cnt%=P;
	}else{
		for(int i=1;i<prev;i++){
			if(i>n)break;
			num[pos]=i;
			saiki(n-i,i,pos+1);
		}
	}
}

main(){
	int tests;
	scanf("%d",&tests);
	for(int t=1;t<=tests;t++){
		int n;
		scanf("%d%d",&n,&b);
		cnt=0;
		saiki(n,n+1,0);
		printf("Case #%d: %d\n",t,cnt);
	}
}