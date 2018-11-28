#include <iostream>
#include <vector>
#include <string>

using namespace std;

int Matches( string &s, vector< vector< bool > > &rules )
{
	for(int i = 0; i < s.size(); i++)
	{
		if( !rules[i][ s[i] - 'a'] )
			return 0;
	}
	return 1;
}

void ReadRules(vector< vector< bool > > &rules)
{
	for(int i = 0; i < rules.size(); i++)
	{
		char c;
		cin >> c;
		if( c == '(' )
		{
			cin >> c;
			while( c != ')' )
			{
				rules[i][c - 'a'] = true;
				cin >> c;
			}
		}
		else
		{
			rules[i][c - 'a'] = true;
		}
	}
}

int main()
{
	int L, D, N;
	cin >> L >> D >> N;

	vector<string> vs(D);
	for(int i = 0; i < D; i++)
		cin >> vs[i];

	for(int i = 0; i < N; i++)
	{
		vector< vector< bool > > rules(L, vector<bool>(26, false) );

		ReadRules(rules);

		int res = 0;
		for(int j = 0; j < D; j++)
		{
			if( Matches(vs[j], rules) )
				res++;
		}
		cout << "Case #" << i+1 << ": " << res << endl;
	}
}
