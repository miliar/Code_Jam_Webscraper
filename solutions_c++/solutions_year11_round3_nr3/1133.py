#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<string>
#include<vector>
#include<queue>
#include<map>
#include<cctype>
#include<list>
#include<set>
using namespace std;
int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small.out","w",stdout);
	int t,l,h,n,cas=0;;
	cin>>t;
	while(t--)
	{
		int a[10000];
		cas++;
		cin>>n>>l>>h;
		for(int i=0;i<n;i++)
			scanf("%d",&a[i]);
		int i;
		bool ok;
		for(i=l;i<=h;i++)
			{
				ok=true;
				for(int j=0;j<n;j++)
				{
					if(i%a[j]!=0&&a[j]%i!=0)
					{
						ok=false;
						break;
					}
				}
				if(ok) break;
			}
			cout<<"Case #"<<cas<<": ";
			if(i==h+1) cout<<"NO\n";
			else cout<<i<<endl;
	}
	return 0;
}

