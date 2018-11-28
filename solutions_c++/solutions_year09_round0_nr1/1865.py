#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<string> vs;
vector<char> *cs;
string s;

bool possible(string str, int x)
{
	if(x == str.length())
		return 1;
	for(int i = 0; i < cs[x].size(); i++)
		if(str[x] == cs[x][i])
			return possible(str, x + 1);
	return 0;
}

int l,d,n;

int main()
{
	cin>>l>>d>>n;
	{
		cs = new vector<char>[l];
		for(int i = 0; i < d; i++)
		{
			cin>>s;
			vs.push_back(s);
		}
		for(int c = 1; c <= n; c++)
		{
			cin>>s;
			int ind = 0;
			for(int i = 0; i < l; i++)
			{
				cs[i].clear();
				if(s[ind] == '(')
				{
					ind++;
					while(s[ind] != ')')
					{
						cs[i].push_back(s[ind]);
						ind++;
					}
				}else{
					cs[i].push_back(s[ind]);
				}
				ind++;
			}
			int ans = 0;
			for(int i = 0; i < d; i++)
				if(possible(vs[i], 0))
					ans++;
			cout<<"Case #"<<c<<": "<<ans<<endl;
		}
		delete []cs;
	}
	return 0;
}
