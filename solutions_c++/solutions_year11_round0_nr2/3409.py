#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

void solve()
{
	typedef map<pair<char,char>,char> combmaptype;
	combmaptype comb;
	set<pair<char,char> > opp;
	int combN;
	cin >> combN;
	int rulei;
	for( rulei = 1; rulei <= combN; ++rulei )
	{
		string rule;
		cin >> rule;
		comb[make_pair(rule[0],rule[1])] = rule[2];
		comb[make_pair(rule[1],rule[0])] = rule[2];
	}
	int oppN;
	cin >> oppN;
	for( rulei = 1; rulei <= oppN; ++rulei )
	{
		string rule;
		cin >> rule;
		opp.insert(make_pair(rule[0],rule[1]));
		opp.insert(make_pair(rule[1],rule[0]));
	}
	vector<char> ans;
	int N;
	cin >> N;
	string invoke;
	cin >> invoke;
	for( string::size_type ii = 0; ii < invoke.size(); ++ii )
	{
		ans.push_back(invoke[ii]);
		combmaptype::const_iterator iter;
		while( ( ans.size() >= 2 ) && ( comb.end() != ( iter = comb.find(make_pair(ans[ans.size()-1],ans[ans.size()-2])) ) ) )
		{
			ans.pop_back();
			ans.back() = iter->second;
		}
		
		for( vector<char>::size_type i = 0; i + 1 < ans.size(); ++i )
			if( opp.end() != opp.find(make_pair(ans[i],ans.back())) )
			{
				ans.clear();
				break;
			}
	}

	cout << '[';
	for( vector<char>::size_type i = 0; i < ans.size(); ++i )
	{
		if( i > 0 )
			cout << ", ";
		cout << ans[i];
	}
	cout << ']';
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int tests;
	cin >> tests;
	for( int x = 1; x <= tests; ++x )
	{
		cout << "Case #" << x << ": ";
		solve();
		cout << endl;
	}
	return 0;
}