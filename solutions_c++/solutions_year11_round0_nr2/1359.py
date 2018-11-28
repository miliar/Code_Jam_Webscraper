#include <vector>
#include <iostream>
#include <string>
#include <map>
#include <utility>
using namespace std;

inline int abs(int x) {	return x < 0 ? (-x):x; }
#define P pair<char,char>


int main(void)
{
	int T, C;
	string s;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cin >> C;
		map < P,char> Comb, Op;
		for (int c = 1; c <= C; c++)
		{
			cin >> s;
			Comb[P(s[0],s[1])] = Comb[P(s[1],s[0])] = s[2];
		}
		cin >> C;
		for (int c = 1; c <= C; c++)
		{
			cin >> s;
			Op[P(s[0],s[1])] = Op[P(s[1],s[0])] = 1;
		}
		cin >> C;
		string ans, l;
		for (int i = 0; i< C; i++)
		{
			char c;
			cin >> c; 
			if (ans == string())	ans += c;
			else if ( Comb.count(P(c,ans[ans.length()-1]) ) )	ans[ans.length()-1] = Comb[P(c,ans[ans.length()-1])];
			else
			{
				for (int j = 0; j<ans.length(); j++)
					if ( Op.count(P(c,ans[j]) ) )
					{
						ans.clear();
						goto nxt;
					}
				ans += c;
				nxt:;
			}
		}
		if ( ans == string() )
		{
			cout << "Case #" << t << ": []\n";
			continue;
		}
		cout << "Case #" << t << ": [";
		for (int i = 0; i + 1 < ans.length(); i++)
			cout << ans[i] << ", ";
		cout << ans[ans.length()-1] << "]\n";
	}	
	return 0;
}
