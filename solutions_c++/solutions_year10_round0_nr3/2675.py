#include <iostream>
#include <fstream>
#include <queue>
using namespace std;
int main()
{
	ifstream cin("C-small-attempt1.in");
	ofstream cout("C-small-attempt1.out");
	int t,r,n,k,tmp;
	cin>>t;
	for(int tt=1;tt<=t;tt++)
	{
		int sum=0;
		queue<int> g;
		cin>>r>>k>>n;
		for(int i=0;i<n;i++)
		{
			cin>>tmp;
			sum+=tmp;
			g.push(tmp);
		}
		if(sum<=k)
		{
			cout<<"Case #"<<tt<<": "<<sum*r<<endl;
			continue;
		}
		int left=k;
		int cost=0;
		int round=0;
		while(!g.empty()&&round<r)
		{
			
			int head=g.front();
			if(left>=head)
			{
				left-=head;
				g.pop();
				g.push(head);
			}
			else
			{
				cost+=k-left;
				left=k;
				round++;
			}
		}
		cout<<"Case #"<<tt<<": "<<cost<<endl;
	}
	system("pause");
	return 0;
}