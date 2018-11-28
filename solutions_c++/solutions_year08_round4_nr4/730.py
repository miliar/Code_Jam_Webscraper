#include<cstdio>
#include<cstring>
#include<string>
#include<iostream>
#include<algorithm>
using namespace std;
typedef unsigned long long LL;
const int maxn=40;

int n1,n2,m,v,n,len;
string a,str;
int per[maxn];

int main()
{
	int t,cas;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>t;
	for(cas=1;cas<=t;cas++)
	{
		cin>>n;
		cin>>str;
		len=str.length();
		for(int i=0;i<n;i++)
		{
			per[i]=i;
		}
		int ans=1<<29;
		do
		{
			a=str;
			for(int i=0;i<len;i+=n)
			{
				string tmp;
				tmp=a.substr(i,n);
				for(int j=0;j<n;j++)
				{
					a[i+j]=tmp[per[j]];
				}
			}
			int sum=1;
			for(int i=1;i<len;i++)
			{
				if(a[i]!=a[i-1])sum++;
			}
			if(sum<ans)ans=sum;
		}while(next_permutation(per,per+n));
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}
