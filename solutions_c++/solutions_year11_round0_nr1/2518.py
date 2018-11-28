#include <iostream>
#include <cmath>

using namespace std;

void solve()
{
	int n;
	cin>>n;
	int curro=1, currb=1, moaro=0, moarb=0;

	char c;
	int a;
	int t=0;

	int temp;
	for(int i=0;i<n;i++)
	{
		cin>>c;
		cin>>a;

		if(c=='O')
		{
			temp=(abs(curro-a)-moaro)+1;
			if(temp<1)
			{
				temp=1;
			}
			t+=temp;
			moarb+=temp;
			moaro=0;
			curro=a;
		}
		else //c=='B'
		{
			temp=(abs(currb-a)-moarb)+1;
			if(temp<1)
			{
				temp=1;
			}
			t+=temp;
			moaro+=temp;
			moarb=0;
			currb=a;
		}
	}
	cout<<t;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cout<<"Case #"<<i<<": ";
		solve();
		cout<<endl;
	}
	return 0;
}