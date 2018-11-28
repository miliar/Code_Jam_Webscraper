#include<iostream>
#include<string>
#include<sstream>
#include<set>
#include<fstream>
using namespace std;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int tc;
    cin >> tc;
    for (int sss = 1; sss <= tc; sss++)
    {
	int one, two;
	cin >> one >> two;
	stringstream sstrm;
	string small, large;
	sstrm << one << " " << two;
	sstrm >> small >> large;
	int rett = 0;
	for (int ii = one; ii <= two; ii++)
	{
	    stringstream ss1;
	    string s;
	    ss1 << ii;
	    ss1 >> s;
	    set<string>sett;
	    for (int i = 0; i < s.size(); i++)
	    {
		string ans = "";
		if (s[i] == '0')
		    continue;
		for (int j = 0; j < s.size(); j++)
		{
		    int pos = (i + j) % s.size();
		    ans += s[pos];
		}
		if (ans >= small && ans <= large && ans != s && ans < s && sett.find(ans) == sett.end())
		{
		    sett.insert(ans);
		    rett++;
		}
	    }
	}
	cout << "Case #" << sss << ": " << rett << "\n";
    }
    return 0;
}
