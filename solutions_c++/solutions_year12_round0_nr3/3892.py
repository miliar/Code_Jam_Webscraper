#include <iostream>
#include <map>
using namespace std;

int roll(int tmp,int m)
{
	int t=tmp/10;
	int p=tmp%10;
	for (int i=0;i<m-1;i++)
		p*=10;
	t+=p;
	return t;
}
int main()
{
	int n,a,b;
	cin>>n;
	for (int i=1;i<=n;i++)
	{
		cin>>a>>b;
		int m=0;
		int t=a;
		while(t!=0)
		{
			m++;
			t/=10;
		}
		int cnt=0;
		map<int,bool> flag;
		for (int j=a;j<=b;j++)
		{
			int tmp=j;
			flag.clear();
			flag[tmp]=true;
			for (int k=1;k<m;k++)
			{
				int t=tmp/10;
				int p=tmp%10;
				for (int l=0;l<m-1;l++)
					p*=10;
				t+=p;
				tmp=t;
				if (tmp<=j)
					continue;
				if (tmp>=a&&tmp<=b&&flag[tmp]==false)
				{
					cnt++;
					flag[tmp]=true;
					//cout<<j<<' '<<tmp<<endl;
				}
			}
		}

		cout<<"Case #"<<i<<": "<<cnt<<endl;
	}
	return 0;
}