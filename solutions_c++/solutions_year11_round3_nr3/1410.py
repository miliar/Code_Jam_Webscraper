#include <iostream>
#include <fstream>
#include <string>
#include <cctype>
#include <stack>
using namespace std;
int main()
{
	freopen("D:\\codejam\\A-small.in","rt",stdin);
	freopen("D:\\codejam\\A-small.out","wt",stdout);
	int T;
	cin>>T;
	for (int i=1;i<=T;i++)
	{
		cout<<"Case #"<<i<<": ";
		long long k,N,L,H,flag=0,val[101];
		cin>>N>>L>>H;
		for(int q=1;q<=N;q++)
			cin>>val[q];
		for(k=L;k<=H;k++)
		{
			flag=1;	
			for(int j=1;j<=N;j++)
				{
					if(k%val[j]==0||val[j]%k==0)
					{
					}
					else 
					{
						flag=0;
						break;
					}
				}
			if(flag)
			{
				cout<<k<<endl;
				break;
			}
		}
		if(k>H) cout<<"NO"<<endl;

	}
	return 0;
}