#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

using namespace std;
vector <string> Comb;
vector <string> Opp;
string s, res;
char IsBase(char a, char b)
{
	int n = Comb.size();
	for(int i = 0; i < n; i++)
		if(Comb[i][0] == a && Comb[i][1] == b || Comb[i][0] == b && Comb[i][1] == a)
		return Comb[i][2];
	return '0';
}
char IsOpp(char c)
{
	int n = Opp.size();
	for(int i = 0; i < n; i++)
	{
		if(Opp[i][0] == c)	return Opp[i][1];
		if(Opp[i][1] == c)	return Opp[i][0];
	}
	return '0';
}
bool Find(char c)
{
	int n = res.size();
	for(int i = 0; i < n; i++)
		if(res[i] == c) return true;
	return false;
}
int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int T, i, j, C, D, N;
	cin >> T;
	for(i = 0; i < T; i++)
	{
		res = "";
		Comb.clear();
		Opp.clear();
		cin >> C;
		for(j = 0; j < C; j++)
		{
			cin >> s;
			Comb.push_back(s);
		}
		cin >> D;
		for(j = 0; j < D; j++)
		{
			cin >> s;
			Opp.push_back(s);
		}
		cin >> N;
		cin >> s;
		res += s[0];
		for(j = 1; j < N; j++)
		{
			if(res == "") { res += s[j]; continue; }
			char c = IsBase(res[res.size()-1], s[j]);
			if(c != '0') res[res.size()-1] = c;
			else
			{
				c = IsOpp(s[j]);
				if(c == '0')	res += s[j];
				else if(Find(c))	res = "";
					 else res += s[j];
			}
		}
		int n = res.size();
		cout << "Case #" << i+1 << ": [";
		if(n > 0)
		{
			cout << res[0];
			for(j = 1; j < n; j++)
				cout << ", " << res[j];
		}
		cout << "]" << endl;
	}
    return 0;
}
