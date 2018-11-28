#include<iostream>
#include <map>
#include<string>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int cnt = 0;
	while(t--)
	{
		int n,m;
		map<string,bool>mm;
		cin>>n>>m;
		int ans = 0;
		for(int i=0;i<n;++i)
		{
			string path; 
			cin>>path;
			mm[path] = true;
			while (path.find_last_of("/") != string::npos)
			{ 
				size_t  pos = path.find_last_of("/");
				string temp = path.substr(0, pos);
				path = temp;
				mm[temp] = true;
			}
		}
		for(int i=0; i<m; ++i)
		{
			string input;
			cin>>input;
			if(!mm[input])
			{
				ans++;
				mm[input] = true;
				while (input.find_last_of("/") != string::npos)
				{ 
					size_t  pos = input.find_last_of("/");
					string temp = input.substr(0, pos);
					input = temp;
					if(!mm[temp] && !input.empty())
					{
						ans++;
						mm[temp] = true;
					}
					else
						break;
				}
			}
		}
		cout<<"Case #"<<++cnt<<": "<<ans<<endl;
	}
	return 0;
}