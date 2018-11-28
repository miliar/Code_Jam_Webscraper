#include<iostream>
#include<stack>
using namespace std;

int getb(int t,int n,int len)
{
	int sum=1;
	int sum2=1;
	for(int i=0;i<n;i++)
	{
		sum*=10;
	}
	for(int i=0;i<len-n;i++)
	{
		sum2*=10;
	}
	int temp=t%sum;
	t/=sum;
	t=t+temp*sum2;
	return t;
}

int  dignum(int t)
{
	int sum=0;
	while(t)
	{
		sum++;
		t/=10;
		
	}
	return sum;
}

int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);
	int t;
	cin>>t;
	int Case=0;
	while(t--)
	{
		Case++;
		int n,m;
		cin>>n>>m;
		int sum=0;
		bool visa[1001][1001];
		memset(visa,0,sizeof(visa));
		for(int i=n;i<=m;i++)
		{
			int len=dignum(i);
			if(len==1)
				continue;
			for(int j=1;j<len;j++)
			{
				int tab=getb(i,j,len);
				if(tab<=m&&!visa[i][tab]&&!visa[tab][i])
				{
					
					if(i<tab)
					{
					//cout<<i<< " "<<tab<<endl;
					sum++;
					visa[i][tab]=1;
					visa[tab][i]=1;
					}
					
				}
			}
		}
		printf("Case #%d: %d\n",Case,sum);
	}
	//system("pause");
	return 0;
}