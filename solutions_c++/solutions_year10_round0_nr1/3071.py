#include <iostream>
using namespace std;
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int t,i,temp,j,n[10010],k[10010];
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>n[i]>>k[i];
	}
	for(i=0;i<t;i++)
	{
		temp=1;
		for(j=0;j<n[i];j++)
			temp=temp*2;
		for(j=0;1;j++)
		{
			if(k[i]==temp*j-1)
			{
				cout<<"Case #"<<i+1<<": ON"<<endl;
				break;
			}
			else
				if(k[i]<temp*j-1)
				{
					cout<<"Case #"<<i+1<<": OFF"<<endl;
					break;
				}
		}
	}
	return 0;
}