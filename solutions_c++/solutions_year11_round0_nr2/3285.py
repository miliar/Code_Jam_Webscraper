#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <string>
#include <map>

using namespace std;

int T, C, D, N;
map <string, char> combine;
set <string> oppose;
string elements;

string solve()
{
	string ans="";
	for(int i=0; i<N; i++)
	{
		string c = ans.size() ? ans.substr(ans.size()-1)+elements[i] : "";
		if(combine.count(c))
			ans[ans.size()-1]=combine[c];
		else
		{
			bool clear=false;
			for(int j=0; j<ans.size(); j+=3)
				clear|=(oppose.find(ans.substr(j,1)+elements[i])!=oppose.end());
			if(clear)
				ans="";
			else
				ans+=(ans.size() ? ", " : "")+string(1,elements[i]);
		}
	}
	return ans;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> T;
	for(int t=1;  t<=T; t++)
	{
		combine.clear(), oppose.clear();
		cin >> C;
		for(int c=0; c<C; c++)
		{
			string s;
			cin >> s;
			combine[s.substr(0,2)] = s[2];
			swap(s[0], s[1]);
			combine[s.substr(0,2)] = s[2];
		}
		cin >> D;
		for(int d=0; d<D; d++)
		{
			string s;
			cin >> s;
			oppose.insert(s);
			swap(s[0], s[1]);
			oppose.insert(s);
		}
		cin >> N;
		cin >> elements;
		printf("Case #%d: [%s]\n", t, solve().c_str());
	}
	return 0;
}