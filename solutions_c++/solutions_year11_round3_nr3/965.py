#include<iostream>
using namespace std;

int main()
{
	int t,i,j,k,n,a[105],l,h;

	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	k=0;
	cin>>t;
	while(t--)
	{
		k++;
		cin>>n>>l>>h;
		for(i=0;i<n;i++)
			cin>>a[i];
		printf("Case #%d: ",k);
		for(i=l;i<=h;i++)
		{
			for(j=0;j<n;j++)
				if (i%a[j]==0||a[j]%i==0) continue;
				else
					break;
			if (j==n) 
			{
				printf("%d\n",i);
				break;
			}
		}
		if (i>h) printf("NO\n");
	}
	//system("pause");
	return 0;
}