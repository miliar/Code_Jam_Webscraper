#include<stdio.h>

int t,r,k,n,g[1000];
int lasttime[1000],lastmoney[1000];
int looptime[1000],loopmoney[1000];
int done,money,front;

int main(){
	scanf("%d",&t);
	for(int tt=1;tt<=t;tt++){
		scanf("%d%d%d",&r,&k,&n);
		for(int i=0;i<n;i++){
			scanf("%d",&g[i]);
			lasttime[i]=-1;
			looptime[i]=-1;
		}
		done=0;money=0;front=0;
		lasttime[0]=0;
		while(done<r){
			if(looptime[front]!=-1&&looptime[front]+done<=r){
				done+=looptime[front];
				money+=loopmoney[front];
			}else{
				int f=front,count=0;
				while(count+g[f]<=k){
					count+=g[f];
					f=(f+1)%n;
					if(f==front)break;
				}
				front=f;money+=count;
				done++;
				if(lasttime[front]==-1){
					lasttime[front]=done;
					lastmoney[front]=money;					
				}else if(looptime[front]==-1&&done!=lasttime[front]){
					looptime[front]=done-lasttime[front];
					loopmoney[front]=money-lastmoney[front];
				}
			}
		}
		printf("Case #%d: %d\n",tt,money);
	}
	return 0;
}
