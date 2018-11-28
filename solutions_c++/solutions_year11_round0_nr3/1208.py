//In the name of Allah
//
//
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
vector <int> list;
int n,t;
int main()
{
	ios::sync_with_stdio(false);
	cin>>t;
	for (int c=0;c<t;c++)
	{
		int xs=0;
		cin>>n;
		list.clear();
		for (int i=0;i<n;i++)
		{
			int a;
			cin>>a;
			xs^=a;
			list.push_back(a);
		}
		if (xs!=0)
		{
			cout<<"Case #"<<c+1<<": NO"<<endl;
			continue;
		}
		sort(list.begin(),list.end());
		int tot=0;
		for (int i=1;i<n;i++)
			tot+=list[i];
		cout<<"Case #"<<c+1<<": "<<tot<<endl;
	}
	return 0;
}
