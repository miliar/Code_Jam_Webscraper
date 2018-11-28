#include<cstdio>
#include<cstring>
#include<string>
#include<vector>
#include<algorithm>
#include<iostream>

using namespace std;

class Trie
{
public:
	bool word;
	Trie* child[256];

	Trie():word(0){ memset(child, 0, sizeof(child));}

	void insert(const string& c, int idx);
	int agg(const vector<string>& c, int idx);
};

void Trie::insert(const string& c, int idx)
{
	int len = c.length();
	if(idx == len)
	{
		word = 1;
		return ;
	}
	if(child[c[idx]] == NULL)
	{
		child[c[idx]] = new Trie();
	}
	child[c[idx]]->insert(c, idx+1);
}
int Trie::agg(const vector<string>& c, int idx)
{
	if(idx == c.size())
	{
		return word;
	}
	int ret = 0;

	for(int j=0; j<c[idx].length(); ++j)
	{
		if(child[c[idx][j]] != NULL)
		{
			ret += child[c[idx][j]]->agg(c, idx+1);
		}
	}

	return ret;
}
int L, D, N;

int main(void)
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	cin >> L >> D >> N;

	string buf;
	Trie dict;
	
	for(int i=0; i<D; ++i)
	{	
		cin >> buf;
		dict.insert(buf, 0);
	}
	vector<string> query;
	for(int i=0; i<N; ++i)
	{
		cin >> buf;
		query.clear();
		for(int j=0; j<buf.length(); j++)
		{
			string tmp="";
			if(buf[j] == '(')
			{
				j++;
				while(buf[j] != ')')
					tmp += buf[j++];
			}
			else
			{
				tmp += buf[j];
			}
			query.push_back(tmp);
		}
		int res = dict.agg(query, 0);
		cout << "Case #" << i+1 << ": " << res << endl;
	}
	
	return 0;
}
