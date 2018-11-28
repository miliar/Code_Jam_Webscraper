#include<iostream>
#include<algorithm>
#include<cmath>
#include<string>
#define fo(i,u,d) for (long i=(u); i<=(d); ++i)
#define fod(i,u,d) for (long i=(u); i>=(d); --i)
using namespace std;

const long maxn=601;
const char ss[19]={'w','e','l','c','o','m','e',' ','t','o',' ','c','o','d','e',' ','j','a','m'};
const long mo=10000;

char s[maxn];
long len,t,f[maxn][19],ans;

void solve()
{
	memset(f,0,sizeof(f)); ans=0;
	fo(i,0,len) {
		fo(j,1,18) if (s[i]==ss[j])
			fo(l,0,i-1) if (s[l]==ss[j-1]) f[i][j]=(f[i][j]+f[l][j-1])%mo;
		if (s[i]==ss[0]) f[i][0]=1;
		ans=(ans+f[i][18])%mo;
	}
}
void print()
{
	char da[5]={'0','0','0','0','\0'};
	for (long i=3; ans; ans/=10, --i) da[i]='0'+ans%10;
	printf("%s\n",da);
}
int main()
{
	freopen("Cl.in","r",stdin);
	freopen("Cl.out","w",stdout);
	scanf("%d%*c",&t);
	fo(l,1,t) {
		scanf("%[^\n]%*c",s);
		len=strlen(s)-1;
		solve();
		printf("Case #%d: ",l);
		print();
	}
	return 0;
}
