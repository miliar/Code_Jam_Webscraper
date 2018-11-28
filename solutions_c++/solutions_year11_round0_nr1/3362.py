#include <stdio.h>

#define abs(n) ((n)<0?(-(n)):(n))
#define max(a, b) ((a)>(b)?(a):(b))

int n;
int r[200],b[200];
int tb,to,pb,po;

int main() {
	int i,k;
	int T;
	char buf[100];
	scanf("%d",&T);
	for(int lT=1;lT<=T;lT++){
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%s%d",buf,&b[i]);
			if(buf[0]=='B')r[i]=0;
			else r[i]=1;
		}
		tb=to=0;
		pb=po=1;
		for(i=0;i<n;i++){
			if(!r[i]){
				tb+=abs(pb-b[i])+1;
				pb=b[i];
				if(tb<=to)tb=to+1;
			}else{
				to+=abs(po-b[i])+1;
				po=b[i];
				if(to<=tb)to=tb+1;
			}
		}
		printf("Case #%d: %d\n",lT,max(tb,to));
	}
	return 0;
}
