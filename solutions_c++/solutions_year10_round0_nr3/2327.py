#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{

	ifstream file("C-small.in");
	int T;
	file>>T;
	for (int i=0;i<T;i++)
	{

		int R, k, N;
		file>>R>>k>>N;
		vector<int> groups;
		int g;
		for (int j=0;j<N;j++)
		{
			file>>g;
			groups.push_back(g);
		}
		groups = vector<int>(groups.rbegin(), groups.rend());
		int euros=0;
		for(int x=0;x<R;x++)
		{
			int c=0;
			int g=0;
			int n;
			while (c<k && g<groups.size())
			{
				int e=0;
				g++;
				n = groups.back();
				groups.pop_back();
				if(k>=c+n)
				{
					euros+=n;
					groups.insert(groups.begin(), n);
				}
				else {
					e=c;
					groups.push_back(n);
				}
				c+=n;
			}

		}
		cout<<"Case #"<<i+1<<": "<<euros<<endl;
	}
	return 0;

}
