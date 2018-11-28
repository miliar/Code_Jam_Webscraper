#include<stdio.h>
int fb[2000000][6];
int main(){
	freopen("2b.in","r",stdin);
	freopen("2b.out","w",stdout);
	int T,a,b;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++){
		scanf("%d%d",&a,&b);
		int count=0,tmp,len,mon,y;
		for(int x=a;x<=b;x++){
			fb[x][10]=0;
			len=0;
			mon=1;
			tmp=x;
			while(tmp>0){
				mon*=10;
				tmp/=10;
				len++;
			}
			mon/=10;
			tmp=x;
			for(int i=1;i<len;i++){
				y=tmp/mon+10*(tmp%mon);
				tmp=y;
				if(y<a||y>b||x>=y)continue;
				int min=x,max=y;
				int j=0;
				for(j=0;j<fb[min][10];j++){
					if(fb[min][j]==max)break;
				}
				if(j>=fb[min][10]){
					count++;
					fb[min][j]=max;
					fb[min][10]++;
					//printf("%d %d  j=%d\n",min,max,j);
				}
			}
		}
		printf("Case #%d: %d\n",cas,count);
	}
	return 0;
}