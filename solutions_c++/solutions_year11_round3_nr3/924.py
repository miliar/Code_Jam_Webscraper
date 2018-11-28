#include<iostream>
using namespace std;
int main()
{
	int a[110];
    freopen("n.txt","w",stdout);
	int i,j,id,t;
	int n,l,h;
	cin>>t;
	for(id=1;id<=t;id++)
	{
		printf("Case #%d: ",id);
		scanf("%d%d%d",&n,&l,&h);
		for(i=0;i<n;i++)
		{
           scanf("%d",&a[i]);
		}
		int flag=0;
		for(j=l;j<=h;j++)
		{
           for(i=0;i<n;i++)
		   {
			   if(!(a[i]%j==0||j%a[i]==0))
		          break;
		   }
		   if(i==n)
		   {
			   flag=1;
			   goto as;
		   }
		}
as:
		if(flag==1)
			printf("%d\n",j);
		else
			printf("NO\n");
	}
}