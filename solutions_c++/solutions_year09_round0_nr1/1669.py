#include<cstdio>
#include<cstring>
using namespace std;

const int MAXL=17;
const int MAXD=5050;

int a[MAXD*MAXL][26];
char s[400], ss[20];
int cnt, ans, len;
int l, d, n;
int L[20], R[20];

void get(int x, int now)
{
	if (x==l) {
		++ans; 
//		printf("%s\n",ss);
		return;
	}
	for(int i=L[x];i<=R[x];++i) 
		if (a[now][s[i]-'a']) {
			ss[x]=s[i];
			get(x+1,a[now][s[i]-'a']);
	}
}

int main()
{
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
	scanf("%d%d%d",&l,&d,&n);
	for(int i=0;i<d;++i) {
		scanf("%s",s);
//		printf("%s\n",s);
		len=strlen(s);
		int now=0;
		for(int j=0;j<len;++j) {
			if (a[now][s[j]-'a']==0) 
				a[now][s[j]-'a']=++cnt;
			now=a[now][s[j]-'a'];
		}
	}
	for(int t=1;t<=n;++t) {
		scanf("%s",s);
//				printf("%s\n",s);
		len=strlen(s);
		int p=0;
		for(int i=0;i<len;++i) {
			if (s[i]=='(') {
				L[p]=++i;
				while (s[++i]!=')');
				R[p]=i-1;
			} else L[p]=R[p]=i;
			++p;
		}
		ans=0;
		get(0,0);
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}