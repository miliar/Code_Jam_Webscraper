#include<stdio.h>
#include<cstring>
long mi[26]={1};
long i,j,k,l,t,tt,n,m;
long you[10001];//you which letter it has
long jz[10001][26];
long hh,anss;
char s[10001][21];
long len[10001];
char fm[30];
long nopt[10001],now[10001],fail[10001];//nopt guess true now which letter fail failed times
inline bool check(){
	static long ii;
	if(len[j]!=len[l]) return 0;
	for(ii=0;ii<26;++ii)
		if(mi[ii]&nopt[j])
			if(jz[j][ii]!=jz[l][ii])
				return 0;
	return 1;
}
int main(){
	freopen("B-small-attempt2.in","r",stdin);
	freopen("B-small-attempt2.out","w",stdout);
	for(i=1;i<26;++i) mi[i]=mi[i-1]<<1;
	scanf("%ld",&t);
	for(tt=1;tt<=t;++tt){
		scanf("%ld%ld",&n,&m),gets(s[0]);
		memset(jz,0,sizeof(jz));
		for(i=0;i<n;++i){
			gets(s[i]);
			len[i]=strlen(s[i]),you[i]=0;
			for(j=0;j<len[i];++j)
				you[i]|=mi[s[i][j]-'a'],jz[i][s[i][j]-'a']|=mi[j];
			}
		printf("Case #%ld: ",tt);
		for(i=1;i<=m;++i){
			gets(fm);
			for(j=0;j<n;++j) nopt[j]=0,now[j]=-1,fail[j]=0;
			for(hh=0,j=0;j<n;++j){
				for(l=0;l<n;++l)
					if(check())
						hh|=you[l];
				for(k=0;k<26;++k)
					if(mi[fm[k]-'a']&hh){
						if(jz[j][fm[k]-'a'])
							nopt[j]|=mi[fm[k]-'a'];
						else
							++fail[j],nopt[j]|=mi[fm[k]-'a'];
						now[j]=k;
						for(hh=0,l=0;l<n;++l)
							if(check())
								hh|=you[l];
						}
				}
			for(anss=0,j=1;j<n;++j)
				if(fail[anss]<fail[j])
					anss=j;
			printf("%s%c",s[anss],i==m?'\n':' ');
			}
		}
	scanf("%ld",&t);
	return 0;
}
