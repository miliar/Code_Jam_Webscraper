#include <stdlib.h>
#include <stdio.h>

int main(){
	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout);
	int h=0;
	scanf("%d\n",&h);
	for(int t=0;t<h;t++){
		int n,s,p;
		int result = 0;
		scanf("%d %d %d",&n,&s,&p);
		for(int i=0;i<n;i++){
			int v;
			scanf("%d",&v);
			if (v%3==0)
			{
				if(v/3>=p) result++;
				if(v/3==p-1 && s>0 && v/3>0) result++,s--;
			}
			if(v%3==1)
			{
				if(v/3+1>=p) result++;
			}
			if(v%3==2)
			{
				if(v/3+1>=p) result++;
				if(v/3+1==p-1 && s>0) result++,s--;
			}
		}
		printf("Case #%d: %d\n",t+1,result);
	}
	return 0;
}