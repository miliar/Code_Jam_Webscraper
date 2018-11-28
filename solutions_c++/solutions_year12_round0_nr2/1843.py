#include <cstdio>
#include <iostream>
#include <cstring>
int main(){
	int T,tt,res;
	int N,S,p,ti;
	int i;
	//freopen("b.in","r",stdin);
	//freopen("b.out","w",stdout);
	scanf("%d",&T);
	for(tt=1;tt<=T;++tt){
		scanf("%d%d%d",&N,&S,&p);
		res=0;
		for(i=0;i<N;++i){
			scanf("%d",&ti);
			int a=ti/3;
			int b=ti%3;
			if(a>=p)++res;
			else if(b&&a+1>=p) ++res;
			else if(S&&(a+2>=p&&2==b||a+1>=p&&a)) ++res,--S;
		}
		printf("Case #%d: %d\n",tt,res);
	}
	return 0;
}