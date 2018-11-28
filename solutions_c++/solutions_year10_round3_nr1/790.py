#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int cases;
	cin>>cases;
	for(int cc = 1; cc <= cases; cc++)
	{
		cout<<"Case #"<<cc<<": ";
		int nn;
		cin>>nn;
		vector <int> left;
		vector <int> right;
		int ret = 0;
		for(int i = 0; i < nn; i++)
		{
			int l,r;
			cin>>l>>r;
			for(int j = 0; j < (int)left.size(); j++)
			{
				if( (left[j] - l) * (right[j] - r) < 0 )
					ret++;
			}
			left.push_back(l);
			right.push_back(r);
		}
		cout<<ret<<endl;

	}
	return 0;
}