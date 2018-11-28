#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cstring>
using namespace std;
int T,f=0;
int N,L,H;
int val[10010];
bool chk(int k){
    for(int i=0;i<N;i++){
	if(k%val[i] && val[i]%k){
	    return 0;
	}
    }
    return 1;
}
int main(){
    scanf("%d",&T);
    while(T--){
	scanf("%d%d%d",&N,&L,&H);
	for(int i=0;i<N;i++){
	    scanf("%d",&val[i]);
	}
	int cc=-1;
	for(int i=L;i<=H;i++){
	    if(chk(i)){
		cc=i;
		break;
	    }
	}
	printf("Case #%d: ",++f);
	if(cc==-1) puts("NO");
	else printf("%d\n",cc);
    }
}
