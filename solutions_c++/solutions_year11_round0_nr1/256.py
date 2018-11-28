#include<stdio.h>
#include<algorithm>
using namespace std;
int main(){
	int _,n,x,y,z,t1,t2;
	char s[99];
	scanf("%d",&_);
	for(int t=1; t<=_; t++){
		t1=0,t2=0;
		y=z=1;
		for(scanf("%d",&n); n--;){
			scanf("%s%d",s,&x);
			if(*s=='O'){
				t1=max(t1+labs(y-x),t2+0L)+1;
				y=x;
			}else{
				t2=max(t2+labs(z-x),t1+0L)+1;
				z=x;
			}
		}
		printf("Case #%d: %d\n",t,max(t1,t2));
	}
	return 0;
}
