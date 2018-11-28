#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int s[1000];
int main()
{
	int t,i,j,r,c,huang,cas=0,n,a,b;
	freopen("C-small.in","r",stdin);
	freopen("C-small.out","w",stdout);
	scanf("%d",&t);
	while (t--)
	{
		cas++;
		scanf("%d",&n);
		scanf("%d%d",&a,&b);
		for (i=0;i<n;i++)
		{
			scanf("%d",&s[i]);
		}
		for (i=a;i<=b;i++)
		{
			huang=1;
			for (j=0;j<n;j++)
				if (i%s[j]!=0 && s[j]%i!=0) huang=0;
			if (huang==1) break ;
		}
		if (huang==1)
			cout<<"Case #"<<cas<<": "<<i<<endl;
		else
			cout<<"Case #"<<cas<<": NO"<<endl;
		
		
		
		
	}
	return 0;
}