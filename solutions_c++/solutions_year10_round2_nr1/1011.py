#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int T, N, M;
vector<string> dirs;
vector<string> existDir;

int main()
{
	ifstream cin("A-large.in");
	ofstream cout("A-large.out");
	cin>>T;
	for (int x=1; x<=T; x++)
	{
		existDir.clear();
		int count=0;
		cin>>N>>M;
		for (int i=0; i<N; i++)
		{
			string a;
			cin>>a;
			existDir.push_back(a);
		}
		sort(existDir.begin(), existDir.end());
		for (int i=0; i<M; i++)
		{
			string a;
			cin>>a;
			bool found=false;
			do
			{
				for (int j=existDir.size()-1; j>=0; j--)
				{
					if (a.compare(existDir[j])==0)
					{
						found = true;
						break;
					}
				}
				if (!found)
				{
					
					existDir.push_back(a);
					count++;
					int t = a.find_last_of("/");
					a = a.substr(0, t);
					if (a.empty())
						break;
				}
				else
					break;
			}
			while (1);
		}
		cout<<"Case #"<<x<<": "<<count<<endl;
	}
}
