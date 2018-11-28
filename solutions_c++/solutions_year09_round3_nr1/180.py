#include<iostream>
#include<cstring>
using namespace std;

int CASE;
char s[100];
bool b[256];
int a[256];
int n;
long long ans;
int cnt;
bool usez;

int main()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (CASE=1;CASE<=T;CASE++)
	{
		scanf("%s",s);
		n=0;ans=0;usez=false;cnt=0;
		memset(b,0,sizeof(b));
		memset(a,0,sizeof(a));
		int len=strlen(s);
		for (int i=0;i<len;i++)
			if (!b[s[i]])
			{
				b[s[i]]=true;
				if (i==0)
					a[s[i]]=++cnt;
				else
				{
					if (!usez)
					{
						usez=true;
						a[s[i]]=0;
					}
					else
						a[s[i]]=++cnt;
				}
			}
		for (int i=0;i<256;i++)
			if (b[i]) n++;
		if (n==1) n=2;
		long long t=1;
		for (int i=len-1;i>=0;i--)
		{
			ans+=a[s[i]]*t;
			t*=n;
		}
		printf("Case #%d: %I64d\n",CASE,ans);
	}
}