#include<stdio.h>
#include<string.h>
char a[128][128],b[128][128];
char out[100];
int l;
int main(){
	int _,t,c,n;
	char s[999];
	scanf("%d",&_);
	for(int t=1; t<=_; t++){
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		for(scanf("%d",&c); c--;){
			scanf("%s",s);
			a[s[0]][s[1]]=s[2];
			a[s[1]][s[0]]=s[2];
		}
		for(scanf("%d",&c); c--;){
			scanf("%s",s);
			b[s[0]][s[1]]=b[s[1]][s[0]]=1;
		}
		scanf("%d%s",&n,s);
		l=0;
		for(int i=0; i<n; i++)
		{
			if(l==0){out[l++]=s[i];continue;}
			if(a[out[l-1]][s[i]]){
				out[l-1]=a[out[l-1]][s[i]];
				continue;
			}
			for(int j=0; j<l; j++)
				if(b[s[i]][out[j]]){
					l=0;
					break;
				}
			if(l==0)continue;
			out[l++]=s[i];
		}
		printf("Case #%d: [",t);
		for(int i=0; i<l; i++){
			putchar(out[i]);
			if(i<l-1)printf(", ");
		}
		puts("]");
	}
	return 0;
}
