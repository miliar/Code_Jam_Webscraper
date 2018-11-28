#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int N,S,P,num[200];
void get_data(){
	scanf("%d%d%d",&N,&S,&P);
	int i;
	for(i=0;i<N;i++)scanf("%d",&num[i]);
}
struct Unit{
	int v[3];
	bool ok(){
		int i;
		for(i=0;i<3;i++){
			if(v[i]<0||v[i]>10)return 0;
		}
		return 1;
	}
};
int get_pt(int x,Unit &a,Unit &b){
	int r=0;
	a.v[0]=x/3;a.v[1]=x/3;a.v[2]=x-a.v[0]-a.v[1];
	b=a;
	if(b.v[0]==b.v[2])b.v[0]--,b.v[2]++;
	else if(b.v[0]==b.v[2]-1)b.v[0]--,b.v[1]++;
	else{
		b.v[2]--;b.v[1]++;swap(a,b);
	}
	if(!a.ok()){
		a=b;r=1;
	}else if(!b.ok()){
		r=1;
	}else r=2;
	return r;
}
void run(){
	int i,s=0,same=0,dif=0,t,ok=0;
	Unit ut[2];
	for(i=0;i<N;i++){
		t=get_pt(num[i],ut[0],ut[1]);
		if(t==1){
			if(ut[0].v[2]>=P)s++;
			if(ut[0].v[2]-ut[0].v[0]==2)ok++;
		}else{
			if(ut[1].v[2]>=P)s++;
			if(ut[0].v[2]>=P&&ut[1].v[2]>=P||ut[0].v[2]<P&&ut[1].v[2]<P)same++;
			else dif++;
			ok++;
		}
	}
	int d=ok-S;
	if(d>same)s-=(d-same);
	printf("%d\n",s);
}
int main(){
//	freopen("1.txt","w",stdout);
	int t,i;
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		get_data();
		printf("Case #%d: ",i);
		run();
	}
	return 0;
}
