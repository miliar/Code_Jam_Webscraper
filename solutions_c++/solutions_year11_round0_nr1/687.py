#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("output.in","w",stdout);
	
	int T,t,posa,posb,time,ta,tb,N,i,btn;
	char c;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		time=0;posa=1;posb=1;ta=0;tb=0;
		scanf("%d",&N);
		for(i=1;i<=N;i++){
			scanf(" %c %d",&c,&btn);
			if(c=='O'){
				if(time-ta>=abs(btn-posa))time+=1;
				else time=ta+abs(btn-posa)+1;
				ta=time;posa=btn;
			}
			else if(c=='B'){
				if(time-tb>=abs(btn-posb))time+=1;
				else time=tb+abs(btn-posb)+1;
				tb=time;posb=btn;
			}
		}
		printf("Case #%d: %d\n",t,time);
	}
	
	return 0;
}
