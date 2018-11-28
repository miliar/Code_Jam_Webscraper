#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define ll long long
int mark[2000005],md,A,B,L,ten;
int get_len(int x){
	int r=0;
	ten=1;
	while(x){
		r++;
		x/=10;ten*=10;
	}
	ten/=10;
	return r;
}
int change(int x){
	int t=x%10;
	return x/10+t*ten;
}
void run(){
	int i,t;
	ll res=0;md=1;
	memset(mark,0,sizeof(mark));
	for(i=A;i<=B;i++){
		md++;
		mark[i]=md;
		t=change(i);
		while(t>=2000005||mark[t]!=md){
			if(t>i&&t<=B)res++;
			if(t<2000005)mark[t]=md;
			t=change(t);
		}
	}
	printf("%lld\n",res);
}
int main(){
	freopen("1.txt","w",stdout);
	int i,t;
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		scanf("%d%d",&A,&B);
		L=get_len(A);
		printf("Case #%d: ",i);
		run();
	}
	return 0;
}
