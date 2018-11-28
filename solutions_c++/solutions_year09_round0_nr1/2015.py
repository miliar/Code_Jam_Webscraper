#include<map>
#include<vector>
#include<string>
#include<iostream>

using namespace std;

int L, D, N;
vector<string> test;
map<int, map<char, int>> dic;

void init()
{ map<char, int> m; dic[0] = m; }

void add(string s)
{
	int vernum = 0;
	for(int i = 0; i < L; i++)
		if(dic[vernum].find(s[i]) != dic[vernum].end())
			vernum = dic[vernum][s[i]];
		else
		{
			map<char, int> m;
			dic[vernum][s[i]] = dic.size();
			vernum = dic.size();
			if (i != L - 1) dic[vernum] = m;
		}
}

vector<string> parse(string s)
{
	int i = 0, j, l = s.length();
	vector<string> res;
	while(i < l)
	{
		if(s[i] != '(')
		{ res.push_back(s.substr(i, 1)); i++; }
		else
		{
			for(j = i + 1; s[j] != ')'; j++) ;
			res.push_back(s.substr(i + 1, j - i - 1));
			i = j + 1;
		}
	}
	return res;
}

int findCount(int v, int num)
{
	int res = 0;
	for(int i = 0; i < test[num].length(); i++)
		if(dic[v].find(test[num][i]) != dic[v].end())
		{
			if (num + 1 == L) 
				res += 1;
			else
				res += findCount(dic[v][test[num][i]], num + 1);
		}
	return res;
}

int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	string s;
	cin >> L >> D >> N;
	for(int i = 0; i < D; i++)
	{ cin >> s;	add(s); }
	for(int i = 0; i < N; i++)
	{
		cin >> s;
		test = parse(s);
		cout << "Case #" << i + 1;
		cout << ": " << findCount(0, 0) << endl;
	}
	return 0;
}
