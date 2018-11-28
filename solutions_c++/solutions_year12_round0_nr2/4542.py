#include<stdio.h>
#include<stdlib.h>
int t,s,p; //t:googler s:surprising
int m,k;
int data[101];

main(){
	freopen("B-large.in","rb",stdin);
	freopen("data.out","wb",stdout);
	while(scanf("%d ",&m)==1){
		for(k=1;k<=m;k++){
			int ans=0;
			int tmp=0;
			scanf("%d%d%d",&t,&s,&p);
			for(int i=1;i<=t;i++){
				scanf("%d",&data[i]);
				if(data[i]%3==0){
					if(data[i]/3>=p)ans+=1;
					else if(data[i]/3+1>=p && data[i]>0)tmp+=1;
				}
				else if(data[i]%3==1){
					if(data[i]/3+1>=p)ans+=1;
					//printf("yaa\n");
				}
				else if(data[i]%3==2){
					if(data[i]/3+1>=p)ans+=1;
					else if(data[i]/3+2>=p)tmp+=1;
					//printf("yaa\n");
				}
			}
			if(s>=tmp)ans+=tmp;
			else ans+=s;
			printf("Case #%d: %d\n",k,ans);
		}
	}
}
