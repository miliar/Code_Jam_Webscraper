#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;

int Case,test,n,x,y;
long long N;

int main(){
	freopen("i.txt","r",stdin);
	Case=1;
	for (scanf("%d",&test);test--;Case++){
		//scanf("%d%d%d",&N,&x,&y);
		cin>>N>>x>>y;
		printf("Case #%d: ",Case);
		bool ok=false;
		if (x==0 && y==0) ok=true;
		else if (x==100 && y==100) ok=true;
		else 
		if (y!=100 && y!=0){
			int i;
			for (i=1;i<=100;i++){
				if (i*x%100==0) break;
			}
			if (i<=N) ok=true;
		}
		if (ok) puts("Possible");
			else puts("Broken");
	}
	return 0;
}
