#include<stdio.h>
#include<string.h>

int n,m,len;
bool st[600][20][26];
char a[5010][50];

int main(){
	scanf("%d%d%d",&len,&n,&m);
	for (int i=0; i<n; i++) scanf("%s",a[i]);
	memset(st,0,sizeof(st));
	for (int i=0; i<m; i++){
		char ss[1000]; 
		scanf("%s",ss);
		int k=strlen(ss),p=0,q=0;
		while (q<len){
			if (ss[p]>='a' && ss[p]<='z'){
				st[i][q++][ss[p]-'a']=true;
				p++;
			}else{
				p++;
				while (ss[p]!=')'){
					st[i][q][ss[p]-'a']=true;
					p++;
				}
				q++;
				p++;
			}
		}
	}
	for (int i=0; i<m; i++){
		int ans=0;
		for (int j=0; j<n; j++){
			bool ok=true;
			for (int k=0; k<len; k++){
				if (!st[i][k][a[j][k]-'a']) ok=false;
			}
			if (ok) ans++;
		}
		printf("Case #%d: %d\n",i+1,ans);
	}
	return 0;
}
