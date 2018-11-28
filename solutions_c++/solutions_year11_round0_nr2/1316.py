#include <iostream>
#include <vector>
#include <map>
#include <set>
using namespace std;

map< string, char > comb;
map< char, set<char> > op;

int main()
{
	int T; cin >> T;
	for (int C = 1; C <= T; ++C)
	{
		comb.clear();
		op.clear();
	
		int c; cin >> c;
		string s;
		for (int i = 0; i < c; ++i)
		{
			cin >> s;
			comb[ s.substr(0,2) ] = s[2];
			swap(s[0], s[1]);
			comb[ s.substr(0,2) ] = s[2];
		}
		
		cin >> c;
		for (int i = 0; i < c; ++i)
		{
			cin >> s;
			op[ s[0] ].insert( s[1] );
			op[ s[1] ].insert( s[0] );
		}
		
		cin >> c;
		cin >> s;
		string ret = "";
		ret = s[0];
		//cout << s << endl;
		for (int i = 1; i < s.size(); ++i)
		{
			ret += s[i];
			if (ret.size() == 1) continue;
			//cout << ret << " " << endl;
			
			while ( ret.size() > 1 )
			{
				if ( comb.find( ret.substr( ret.size()-2, 2 ) ) == comb.end() ) break;
				char cc = comb[ret.substr( ret.size()-2, 2 )];
				ret = ret.substr(0, ret.size()-2);
				ret += cc;
			}
			//cout << "\t" << ret << endl;
			
			bool clean = 0;
			for (int j = 0; j < ret.size(); ++j)
				if ( op[ ret[ret.size()-1] ].count(ret[j]) )
				{
					clean = 1;
					break;
				}
			if (clean) ret = "";
		}
	
		cout << "Case #" << C << ": ";
		cout << "[";
		for (int i = 0; i < ret.size(); ++i)
		{
			if (i != 0) cout << ", ";
			cout << ret[i];
		}
		cout << "]" << endl;
	}
}

