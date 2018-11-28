#include<stdio.h>
#include<math.h>
char in[100];
bool f;
inline bool iss(long long x){
    long long xx=(long long)sqrt(x);
    return x==xx*xx||x==(xx+1)*(xx+1)||x==(xx-1)*(xx-1);
}
inline long long ton(char* c,int l){
    int i;
    long long a=0;
    for(i=0;i<l;i++)a=a*2+c[i]-'0';
    return a;
}
inline void dfs(int np){
    if(f)return;
    if(in[np]==0){
	if(iss(ton(in,np))){
	    puts(in);
	    f=1;
	}
	return;
    }
    if(in[np]!='?')dfs(np+1);
    else{
	in[np]='1';
	dfs(np+1);
	in[np]='0';
	dfs(np+1);
	in[np]='?';
    }
}
int main(){
    int t,cas=1;
    scanf("%d",&t);
    while(t--){
	scanf("%s",in);
	f=0;
	printf("Case #%d: ",cas++);
	dfs(0);
    }
}
