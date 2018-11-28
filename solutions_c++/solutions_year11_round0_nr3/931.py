#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<stack>
#include<cmath>
using namespace std;

int main()
{

	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int test;
	cin>>test;
	for (int curt=1;curt<=test;curt++)
	{
		int n;
		cin>>n;
		int Min=1000*1000*1000;
		int res=0,sum=0;
		for (int i=0;i<n;i++)
		{
			int temp;
			cin>>temp;
			res^=temp;
			sum+=temp;
			if (temp<Min)
				Min=temp;
		}
		cout<<"Case #"<<curt<<": ";
		if (res)
		{
			cout<<"NO";
		}
		else
		{
			cout<<sum-Min;
		}
		cout<<endl;
	}

	


	 

	return 0;
}