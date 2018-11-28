#include <string>
#include <iostream>
#include <vector>

using namespace std;

bool calc( string s, string p )
{	
	bool ok = false;
	int cnt = 0;
	string ss;
	vector<string> v;
	
	for ( int i = 0; i < p.size(); ++i )
	{
		if ( p[i] == '(' )
		{
			ok = true;
		}
		else if ( p[i] == ')' )
		{
			v.push_back(ss);
			ss = "";
			ok = false;
		}
		else if ( ok )
		{
			ss += p[i];
		}
		else if ( !ok )
		{
			ss += p[i];
			v.push_back(ss);
			ss = "";
		}
	}
	
	for ( int i = 0; i < s.size(); ++i )
	{
		for ( int j = 0; j < v[i].size(); ++j )
		{
			if ( v[i][j] == s[i] )
			{
				++cnt;
				break;
			}
		}
	}

	return cnt == s.size();
}

int main()
{
	int L, D, N;
	string s;
	vector<string> v1, v2;
	
	cin >> L >> D >> N;
	
	vector<int> asw(N, 0);
	
	for ( int i = 0; i < D; ++i )
	{
		cin >> s;
		v1.push_back(s);
	}
	
	for ( int i = 0; i < N; ++i )
	{
		cin >> s;
		v2.push_back(s);
	}
	
	for ( int i = 0; i < D; ++i )
	{
		for ( int j = 0; j < N; ++j )
		{
			if ( calc( v1[i], v2[j] ) )
			{
				asw[j]++;
			}
		}
	}
	
	for ( int j = 1; j <= N; ++j )
	{
		cout << "Case #" << j << ": " << asw[j-1] << endl;  
	}
	
	return 0;
}
