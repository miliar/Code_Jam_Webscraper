#include<cstdio>
#include<cstring>
#include<map>
using namespace std;

map<char,int> hash;
char s[10000];
int a[10000];
int n;
int tr;
int TT=0;
void work()
{
	bool u0=true;
	int num;
	tr = 1;
	for(int i=0;i<n;i++)
	{
		if( hash.find(s[i])!=hash.end() ) a[i] = hash[s[i]];else
		{
			if( u0 && i>0 )
			{
				num = 0;
				u0 = false;
			}else num = tr++;
			hash[ s[i] ] = num;
			a[i] = num;
		}
	}

	long long ans = 0;
	for(int i=0;i<n;i++) ans=ans*tr+a[i];
	printf("Case #%d: %I64d\n",++TT,ans);
}
int main()
{
	int T;
	for(scanf("%d\n",&T);T;T--)
	{
		gets(s);
		n = strlen(s);
		hash.clear();
		work();
	}
	return 0;
}
