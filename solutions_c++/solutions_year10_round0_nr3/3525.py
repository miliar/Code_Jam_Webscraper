#include<iostream>
#include<fstream>
#include<queue>

using namespace std;
int main()
{
	
	ifstream cin("C-small-attempt0.in");
	ofstream cout("roller.txt");
	int t,r,k,n;
	
	cin>>t;

	for(int q=1;q<=t;q++)
	{
		queue<int> grp;
		int profit=0;
		cin>>r>>k>>n;

		for(int i=0;i<n;i++)
		{
			int temp;
			cin>>temp;
			grp.push(temp);
		}

		int qq=k;
		for(int i=1;i<=r;i++)
		{
			int count=0;
			while(grp.front()<=k && count<n)
			{
				int temp=grp.front();
				profit+=temp;
				k=k-grp.front();
				grp.pop();
				grp.push(temp);
				count++;

			}
			k=qq;
		}

		cout<<"Case #"<<q<<": "<<profit<<endl;

	}

	return 0;
}