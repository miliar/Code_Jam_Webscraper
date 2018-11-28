#include<stdio.h>
#include<string.h>
#include<queue>

const int N=55;

int ft[N];
int now[N];


int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,k,t,ans;
	
	int b,e;
	int T,n;
	char s[N];
	int ca=0;
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		for(i=0;i<n;i++){
			k=0;
			scanf("%s",s);
			for(j=0;j<n;j++){
				if(s[j]=='1') k=j;
			}
			ft[i]=k;
		}

		
		ans=0;
		for(i=0;i<n;i++)
		{
			for(j=i;j<n;j++)
			{
				if(ft[j]<=i)break;
			}
			ans+=j-i;
		
			for(k=j;k>i;k--){
				
				t=ft[k];
				ft[k]=ft[k-1];
				ft[k-1]=t;
			}
				
		}

		printf("Case #%d: %d\n",++ca,ans);
	}
	return 0;
}