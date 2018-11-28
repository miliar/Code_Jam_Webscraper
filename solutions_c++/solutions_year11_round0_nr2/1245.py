#include <iostream>
#include <string>
#include <map>
using namespace std;

class Problem
{
    map<char, char> op;
    map<string, string> comb;
    string inp;
public:
	void ReadData()
	{
	    comb.clear();  op.clear();
	    string s;
	    int C; cin >> C;
	    for (int i=0; i<C; ++i)
	    {
	        cin >> s;
	        comb[s.substr(1, 1)+s[0]] = comb[s.substr(0, 2)] = s[2];
	    }
	    int D; cin >> D;
	    for (int i=0; i<D; ++i)
	    {
	        cin >> s;
	        op[s[0]] = s[1];
	        op[s[1]] = s[0];
	    }
	    int N; cin >> N;
	    cin >> inp;
	}
	void Solve(int nCase)
	{
		ReadData();
		
		string res;
		for (int i=0; i<inp.length(); ++i)
		{
		    res += inp[i];
		    if (res.length()>=2)
		    {
		        map<string, string>::const_iterator icomb = comb.find(res.substr(res.length()-2));
		        if (icomb!=comb.end())
		            res = res.substr(0, res.length()-2) + icomb->second;
		        map<char, char>::const_iterator iop = op.find(res[res.length()-1]);
		        if (iop!=op.end() && res.find(iop->second)!=string::npos)
		            res = "";
		    }
		}

		cout << "Case #" << nCase << ": [";
		for (int i=0; i<res.length(); ++i )  cout << (i?", ":"") << res[i];
		cout << "]" << endl;
	}
};

int main()
{
	int T;  cin >> T;
	Problem sol;	for (int i=1; i<=T; ++i)  sol.Solve(i);
	return 0;
}