#include<cstdio>
#include<string>
#include<cstring>
#include<map>
using namespace std;
bool mark[1005];
map<string,int>hash;
map<string,int>::iterator it;
char str[1000];
int main()
{
	int t,cc,i,n,q,sum,x,j,ct;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	for(cc=1;cc<=t;cc++)
	{
		scanf("%d\n",&n);
		ct=0;
		hash.clear();
		for(i=0;i<n;i++)
		{
			gets(str);
			hash[str]=i;
		}
		scanf("%d\n",&q);
		for(i=0;i<n;i++)mark[i]=0;sum=0;
		for(i=0;i<q;i++)
		{
			gets(str);
			it=hash.find(str);
			if(it==hash.end())continue;
			x=it->second;
			if(mark[x]==0)
			{
				sum++;
				mark[x]=1;
			}
			if(sum==n)
			{
				for(j=0;j<n;j++)mark[j]=0;
				mark[x]=1;
				sum=1;
				ct++;
			}
		}
		printf("Case #%d: %d\n",cc,ct);
	}
	return 0;
}



		

		

