#include <cstdio>
#include <string>
#include <cctype>

using namespace std;


__int64 f[22];
int d[22];
const int M=10009;
int b[26],a[22][26];
char s[10000],temp[100];
string term[10];
int p;
int n;
int m;
int ans[100];

void make(char *s) {
int j;
	p=0;
	for (;;) {
		for (j=0;isalpha(*s);++s,++j) {
			temp[j]=tolower(*s);
		}
		temp[j]=0;
		term[p++]=temp;
		if (*s==0) {
			return;
		}
		++s;
	}
}

void cal(int c) {
int i,j,temp;
__int64 mm=f[c];
	for (i=0;i<n;++i) {
		mm/=f[d[i]];
	}
	mm%=M;
	for (i=0;i<p;++i) {
		temp=1;
		for (j=0;j<term[i].size();++j) {
			temp=temp*b[term[i][j]-'a']%M;
		}
		temp=temp*mm%M;
		ans[c]+=temp;
		if (ans[c]>=M) {
			ans[c]-=M;
		}
	}
}
		

void gao(int now,int choose) {
int i;
	if (now==n) {
		cal(choose);
		return;
	}
	
	if (choose<m) {
		for (i=0;i<26;++i) {
			b[i]+=a[now][i];
		}
		++d[now];
		gao(now,choose+1);
		for (i=0;i<26;++i) {
			b[i]-=a[now][i];
		}
		--d[now];
	}
	gao(now+1,choose);
}



int main() {
int z,zz,i,j;

	f[0]=f[1]=1;
	for (i=2;i<=20;++i) {
		f[i]=i*f[i-1];
	}

	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&zz);
	for (z=1;z<=zz;++z) {
		scanf("%s%d%d",s,&m,&n);
		p=0;
		make(s);
		memset(b,0,sizeof(b));
		memset(a,0,sizeof(a));
		memset(d,0,sizeof(d));
		for (i=0;i<n;++i) {
			scanf("%s",s);
			for (j=0;s[j];++j) {
				++a[i][tolower(s[j])-'a'];
			}
		}

		memset(ans,0,sizeof(ans));
		gao(0,0);
		printf("Case #%d:",z);
		for (i=1;i<=m;++i) {
			printf(" %d",ans[i]);
		}
		puts("");
	}

	return 0;
}