#include<stdio.h>
struct com{
	char r;
	int x;
};
inline int abs(int a){
	if(a<0)return -a;
	else return a;
}
#define max(a,b) ((a>b) ? (a) : (b))
//com a[128];
int solve(){
	int n,i;
	int x;char c;
	int time=0;
	scanf("%d",&n);
	int tr[2]={0,0};
	int xr[2]={1,1};
	int dt;
	for(i=0;i<n;i++){
		scanf(" %c %d",&c,&x);
		c=(c=='B');

		dt=abs(x-xr[c])+1-tr[!c];

		if(dt<=0){
			tr[!c]=0;
			dt=1;

		}
		else tr[!c]=0;
		tr[c]+=dt;
		/*
		if(tr[!c]<abs(x-xr[c])+1){
			dt=abs(x-xr[c])+1-tr[!c];
			tr[!c]=0;
			tr[c]+=dt;
		}
		else {
			dt=1;
			tr[!c]=0;
		}*/
		xr[c]=x;
		time+=dt;
	}


	return time;
}
int main(){
	int t;
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for(int I=1;I<=t;I++)
		printf("Case #%d: %d\n",I,solve());

	return 0;
}