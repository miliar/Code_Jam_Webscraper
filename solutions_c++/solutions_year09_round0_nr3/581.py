#include <iostream>
#include <vector>
#include <string>
#include <cstdio>

using namespace std;

int main()
{
	int N;
	cin >> N;
	string t = "welcome to code jam";
	for(int n = 1; n <= N; n++)
	{
		string s;
		if( n == 1 )
			getline(cin, s);
		getline(cin, s);
		//cout << s << endl;

		vector< vector< int > > memo(s.size()+1, vector<int>( t.size() + 1, 0 ) );

		for(int i = 0; i < s.size(); i++)
		{
			memo[i][0] = 1;
			for(int j = 0; j < t.size(); j++)
			{
				memo[i+1][j+1] = memo[i][j+1];
				if( s[i] == t[j] )
				{
					memo[i+1][j+1] += memo[i][j];
				}
				memo[i+1][j+1] %= 10000;
			}
		}

		printf("Case #%d: %04d\n", n, memo[s.size()][t.size()]);
	}
}