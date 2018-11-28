#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
using namespace std;
#define se second
#define fi first
#define mp make_pair
#define pb push_back
#define forn(i, n) for (int i = 0; i < (int)(n); i++)

vector<vector<char> > opp;
vector<vector<pair<char, char> > > kill;
string cur;

void solve(int);
bool handle();

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) solve(i+1);
	return 0;
};
void solve (int I)
{
	kill.resize(0);kill.resize(300);
	opp.resize(0);opp.resize(300);
	
	int n;
	string s;
	cin >> n;
	forn(i, n)
	{
		cin >> s;
		kill[s[0]].pb(mp(s[1], s[2]));
		kill[s[1]].pb(mp(s[0], s[2]));
	}
	cin >> n;
	forn(i, n)
	{
		cin >> s;
		opp[s[0]].pb(s[1]);
		opp[s[1]].pb(s[0]);
	}
	cin >> n >> s;
	cur = "";
	forn(i, n)
	{
		cur += s[i];
		while (handle());
	}
	cout << "Case #" << I << ": ";
	//cout << cur << endl;
	string res = "[";
	forn(i, cur.length()) res += cur.substr(i,1) + ", ";
	if (res.length() > 1) res.resize(res.length()-2);
	cout << res << "]" << endl;
};
bool handle()
{
	//cout << "Handling '" << cur << "'\n";
	if (cur.length() < 2) return false;
	char last = cur[cur.length()-1], aft = cur[cur.length()-2];

	forn(i, kill[last].size()) if (kill[last][i].fi == aft)
	{
		cur.resize(cur.length()-2);
		cur += kill[last][i].se;
		//cout << "r1\n";
		return true;
	}
	forn(i, opp[last].size()) if (cur.find(opp[last][i]) != cur.npos)
	{
		cur = "";
		//cout << "r2\n";
		return true;
	}
	return false;
};
