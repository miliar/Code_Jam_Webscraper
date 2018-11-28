#include<stdio.h>
#include<map>
#include<string>
using namespace std;
#define maxn 200

int main()
{
	int test,count=1;
	int i,n,m,a[210],b[1010];
	char s[maxn];
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&test);
	while(test--)
	{
		bool v[210]={0};
		map<string,int>mp;
		int c=1,na=0,nb=0;
		scanf("%d\n",&n);
		for(i=0;i<n;i++)
		{
			gets(s);
			if(!mp[s]) mp[s]=c++;
			a[na++]=mp[s];
		}
		scanf("%d\n",&m);
		for(i=0;i<m;i++)
		{
			gets(s);
			if(!mp[s]) mp[s]=c++;
			b[nb++]=mp[s];
		}
		int cnt=0;
		int p=0, k=0;
		for(i=0;i<nb;i++)
		{
			if(v[b[i]] == 0) v[b[i]]=1,k++;
			if(k==n) 
			{
				memset(v,0,sizeof(v));
				k=0;
				p=b[i];
				cnt++;
				break;
			}
		}
		for(;i<nb;i++)
		{
			if(v[b[i]]==0 && b[i]!=p) v[b[i]]=1,k++;
			if(k==n-1)
			{
				memset(v,0,sizeof(v));
				k=0;
				p=b[i];
				cnt++;
			}
		}
		printf("Case #%d: %d\n",count++,cnt);
	}
	return 0;
}