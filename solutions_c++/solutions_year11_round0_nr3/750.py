#include<iostream>
using namespace std;
int num[1001];
int main()
{
	int T;
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	cin>>T;
	int j = 1;
	int n;
	int i;
	while(j <= T)
	{
		int min;
		int sum=0;
		int temp=0;
		cin>>n;
		for(i = 0 ; i < n ; i ++)
		{
			cin>>num[i];
			if(i == 0)
			{
				min = num[i];
			}
			else
			{
				if(min>num[i])
				{
					min = num[i];
				}
			}
			sum+=num[i];
			temp = temp^num[i];
		}
		if(temp != 0)
		{
			cout<<"Case #"<<j<<": NO"<<endl;
		}
		else
		{
			cout<<"Case #"<<j<<": "<<sum-min<<endl;
		}
		j++;
	}
	return 0;
}