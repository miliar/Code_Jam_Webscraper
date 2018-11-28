#include <stdio.h>
char c[110];
int p[110],tm[110];
int max(int i,int j){return i<j?j:i;}
int abs(int n){return n>0?n:-n;}
int main(int argc, const char *argv[])
{
	int times;
	scanf("%d",&times);
	for(int timesNumber=1;timesNumber<=times;timesNumber++){
		int n;
		scanf("%d",&n);
		int b=1,o=1;
		for(int i=0;i<n;i++){
			char s[2];
			scanf("%s%d",s,&p[i]);
			c[i]=s[0];
			switch(c[i]){
				case 'B':
					tm[i]=abs(p[i]-b)+1;
					b=p[i];
					break;
				case 'O':
					tm[i]=abs(p[i]-o)+1;
					o=p[i];
					break;
				default:break;
			}
		}
		int res=0,t=0;
		for(int i=0;i<n;i++){
			if(!i || c[i]==c[i-1]){
				t+=tm[i];
			}else{
				res+=t;
				t=max(0,tm[i]-1-t)+1;
			}
		}
		if(t)res+=t;
		printf("Case #%d: %d\n",timesNumber,res);
	}
	return 0;
}
