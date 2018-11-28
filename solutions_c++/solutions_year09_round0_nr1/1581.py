#include<cstdio>
#include<cstring>
int l,d,n;
char str[5010][17];
int map[15][26];
int main() {
	char in[500];
	int lin;
	freopen("aa.in","r",stdin);
	freopen("jam1.out","w",stdout);
	scanf("%d %d %d",&l,&d,&n);
	int i,j,k,ct,ans;
	for(i=0;i<d;i++) {
		scanf(" %s",str[i]);
	}
	for(i=0;i<n;i++) {
		scanf(" %s",in);
		lin = strlen(in);
		ct = 0;
		for(j=0;j<lin;j++) {
			if(in[j]=='(') {
				for(j++;in[j]!=')';j++)
					map[ct][in[j]-'a']=1;
				ct++;
			} else
				map[ct++][in[j]-'a']=1;
		}
		ans=0;
		for(j=0;j<d;j++) {
			for(k=0;k<l;k++) {
				if(!map[k][str[j][k]-'a'])
					goto no;
			}
			ans++;
			no:	;
		}
		for(j=0;j<l;j++)
			for(k=0;k<26;k++)
				map[j][k]=0;
		printf("Case #%d: %d\n",i+1,ans);
/*		for(j=0;j<lin;j++,printf("\n"))
			for(k=0;k<26;k++)
				if(map[j][k])printf("%d ",k);*/
	}
}
