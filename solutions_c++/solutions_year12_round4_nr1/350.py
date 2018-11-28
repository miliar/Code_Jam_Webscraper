#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
int s[20000], p[20000], q[20000], n, d;
bool used[20000];

void dfs(int now){
	for(int i=now+1;i<n;i++)
		;
}

int main(void){
	int t, tt;
	scanf("%d",&t);
	for(tt=1;tt<=t;tt++){
		scanf("%d", &n);
		for(int i=0;i<n;i++)
			scanf("%d%d",&s[i],&p[i]);
		scanf("%d",&d);
		
		memset(q,0,sizeof(q));
		q[0] = s[0];
		for(int i=0;i<n;i++){
			for(int j=1;j<n;j++){
				if(s[i]+q[i] >= s[j])
					q[j] = max(q[j], min(p[j],s[j]-s[i]));
			}
		}
		int ii;
		//for(ii=0;ii<n;ii++)
		//	printf("%d ",q[ii]);
		//puts("");
		for(ii=0;ii<n;ii++)
			if(s[ii]+q[ii] >= d)
				break;
		printf("Case #%d: %s\n", tt, ii<n?"YES":"NO");
	}
	
	return 0;
}
