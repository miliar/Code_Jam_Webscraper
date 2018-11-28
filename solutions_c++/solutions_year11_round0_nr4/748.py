#include<iostream>
using namespace std;
int main()
{
	int T;
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	cin>>T;
	int j = 1;
	int n;
	int i;
	int temp;
	while(j<= T)
	{
		int sum = 0;
		cin>>n;
		for( i = 0 ; i < n ; i ++)
		{
			cin>>temp;
			if(i != temp-1)
			{
				sum++;
			}
		}
		cout<<"Case #"<<j<<": "<<sum<<".000000"<<endl;
		j++;
	}
	return 0;
}