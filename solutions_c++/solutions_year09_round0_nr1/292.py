#include<stdio.h>
#include<string.h>


char word[5100][19];
int ok[19][128];
char s[10000];

int n,len,m;


int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int ca=0;
	int i,j,k,t,ans;
	scanf("%d%d%d",&len,&n,&m);
	for(i=0;i<n;i++) scanf("%s",word[i]);
	while(m--){
		scanf("%s",s);
		memset(ok,0,sizeof(ok));
		i=0;
		for(t=0;t<len;t++){
			if(s[i]>='a'&&s[i]<='z'){
				ok[t][s[i]]=1;
				i++;
			}
			else{
				i++;
				while(s[i]>='a'&&s[i]<='z'){
					ok[t][s[i]]=1;
					i++;
				}
				i++;
			}
		}
		ans=0;
		for(t=0;t<n;t++){
			for(i=0;i<len;i++){
				if(!ok[i][word[t][i]]) break;
			}
			if(i>=len) ans++;
		}
		printf("Case #%d: %d\n",++ca,ans);
	}
	return 0;
}