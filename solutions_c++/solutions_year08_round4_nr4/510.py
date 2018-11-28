#include<stdio.h>
#include<string.h>
char s[60000],per[10],s2[60000];
bool used[10];
int ans=1<<29,k,n,m;

void run(int d){
	if (d==k){
		int cnt=0;
		for (int i=0; i<m; i++,cnt+=k){
			for (int j=0; j<k; j++) s2[cnt+j]=s[cnt+per[j]];
		}
		int p=1;
		for (int i=1; i<n; i++){
			if (s2[i]!=s2[i-1]) p++;
		}
		if (p<ans) ans=p;
	}else{
		for (int i=0; i<k; i++){
			if (used[i]) continue;
			used[i]=true; per[d]=i; 
			run(d+1);
			used[i]=false; 
		}
	}
}

int main(){
	int ca; scanf("%d",&ca);
	for (int tt=1; tt<=ca; tt++){
		scanf("%d",&k);
		scanf("%s",s);
		memset(used,0,sizeof(used));
		n=strlen(s);
		m=n/k;
		ans=1<<29;
		run(0);
		printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}
