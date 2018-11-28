//f[total][pos]
//f[i][j] = sum(f[k][j+1]), s[k]==w[j+1],,  s[i]==w[j]
//s[i]!=w[j], f[i][j]=0;
// total*pos*total <= 500*20*500   , 100 times

#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace  std;

const char w[]="welcome to code jam";
const int len = 19, CA=110, M=110;

int f[M][len];
char s[M];
int n;
int main()
{
	int i,j,k,t,ca;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d\n",&ca);
	
	for(t=1;t<=ca;++t)
	{
		gets(s);
		n = strlen(s);
		for(i=0;i<n;++i)
		{
			for(j=0;j<len;++j)
			{
				f[i][j]=0;
			}
			if(s[i]==w[len-1]) f[i][len-1]=1;
		}
		for(j=len-2;j>=0;--j)
		{
			
			for(i=n-1;i>=0;--i)
			if(w[j]==s[i])
			{
				for(k=i+1;k<n;++k)
				if(w[j+1]==s[k])
				{
					f[i][j] = (f[i][j]+f[k][j+1])%10000;
				}
			}
			else f[i][j] = 0;
		}
		int ans=0;
		for(i=0;i<n;++i) ans = (ans+f[i][0])%10000;
		printf("Case #%d: %04d\n", t, ans);
		
	}
	return 0;
}


