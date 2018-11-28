#include<stdio.h>
#include<string.h>
#include<stdlib.h>

struct node{
	char c;
	int pos;
}seq[120];

int sign(int a,int b){
	return a<b?-1:1;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int k=0;k<T;++k){
		int n,t=0;
		char str[10];
		scanf("%d",&n);
		for(int i=1;i<=n;++i){
			scanf("%s%d",str,&seq[i].pos);
			seq[i].c=str[0];
		}
		int o=1,b=1;
		for(int i=1;i<=n;++i){
			if(seq[i].c=='O'){
				t+=abs(seq[i].pos-o)+1;
				for(int j=i+1;j<=n;++j){
					if(seq[j].c=='B'){
						if(abs(seq[j].pos-b)>=abs(seq[i].pos-o)+1)
							b+=sign(seq[j].pos,b)*(abs(seq[i].pos-o)+1);
						else
							b=seq[j].pos;
						break;
					}
				}
				o=seq[i].pos;
			}else{
				t+=abs(seq[i].pos-b)+1;
				for(int j=i+1;j<=n;++j){
					if(seq[j].c=='O'){
						if(abs(seq[j].pos-o)>=abs(seq[i].pos-b)+1)
							o+=sign(seq[j].pos,o)*(abs(seq[i].pos-b)+1);
						else
							o=seq[j].pos;
						break;
					}
				}
				b=seq[i].pos;
			}
		}
		printf("Case #%d: %d\n",k+1,t);
	}
	return 0;
}
