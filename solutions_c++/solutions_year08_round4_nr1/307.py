#include <iostream>
#include <string>
#define task "file"
#define N 10001
#define Inf (int)1e9

using namespace std;
int test;
int m,v;
int t[N][2];
int mark[N][2];
int stat[N];
int chan[N];
int zn;

int max(int a,int b){
	return a+b;
}

int fuck(int ver,int z){
	if (mark[ver][z]) return t[ver][z];
	mark[ver][z]=1;
	int cur;
	if (stat[ver]==1){
		if (z==1){
			cur=max(fuck(ver*2,1),fuck(ver*2+1,1));
			if (cur<t[ver][z]) t[ver][z]=cur;
			if (chan[ver]==1){
				cur=1+max(fuck(ver*2,1),fuck(ver*2+1,0));	
				if (cur<t[ver][z]) t[ver][z]=cur;
				cur=1+max(fuck(ver*2,0),fuck(ver*2+1,1));	
				if (cur<t[ver][z]) t[ver][z]=cur;
			}
		}else{
			cur=max(fuck(ver*2,0),fuck(ver*2+1,0));
			if (cur<t[ver][z]) t[ver][z]=cur;
			cur=max(fuck(ver*2,1),fuck(ver*2+1,0));
			if (cur<t[ver][z]) t[ver][z]=cur;
			cur=max(fuck(ver*2,0),fuck(ver*2+1,1));
			if (cur<t[ver][z]) t[ver][z]=cur;
		}
	}else{
		if (z==1){
			cur=max(fuck(ver*2,1),fuck(ver*2+1,1));
			if (cur<t[ver][z]) t[ver][z]=cur;
			cur=max(fuck(ver*2,1),fuck(ver*2+1,0));
			if (cur<t[ver][z]) t[ver][z]=cur;
			cur=max(fuck(ver*2,0),fuck(ver*2+1,1));
			if (cur<t[ver][z]) t[ver][z]=cur;
		}else{
			cur=max(fuck(ver*2,0),fuck(ver*2+1,0));
			if (cur<t[ver][z]) t[ver][z]=cur;
			if (chan[ver]){
				cur=1+max(fuck(ver*2,1),fuck(ver*2+1,0));	
				if (cur<t[ver][z]) t[ver][z]=cur;
				cur=1+max(fuck(ver*2,0),fuck(ver*2+1,1));	
				if (cur<t[ver][z]) t[ver][z]=cur;
				cur=1+max(fuck(ver*2,0),fuck(ver*2+1,0));	
				if (cur<t[ver][z]) t[ver][z]=cur;
			}
		}
	}
	return t[ver][z];
}

int main(void){
	freopen(task".in","r",stdin);
	freopen(task".out","w",stdout);
	scanf("%i",&test);
	for (int z=1;z<=test;z++){
		printf("Case #%i: ",z);
		scanf("%i %i",&m,&v);
		for (int i=1;i<=m;i++){
			t[i][0]=t[i][1]=Inf;
			mark[i][0]=mark[i][1]=0;
		}
		for (int i=1;i<=(m-1)/2;i++){
			scanf("%i %i",&stat[i],&chan[i]);
		}
		for (int i=1;i<=(m+1)/2;i++){
			scanf("%i",&zn);
			int q=(m-1)/2+i;
			t[q][zn]=0;
			mark[q][0]=mark[q][1]=1;
		}
		int res=fuck(1,v);
		//for (int i=1;i<=m;i++){
			//printf("%i   -  %i    ,  %i\n",i,t[i][0],t[i][1]);
		//}
		if (res==Inf) cout<<"IMPOSSIBLE";
		else cout<<res;
		cout<<endl;
	}

	return 0;
}
