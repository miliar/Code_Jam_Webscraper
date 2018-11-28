#include<iostream>
#include<vector>
#include<string>

using namespace std;

class node
{
public:

	node * branch[26];

	node()
	{
		for(int i = 0; i < 26; ++i)
			branch[i] = 0;
	}
};

node root;

vector< vector<char> > pattern;
int K;

void count(node * n, int l)
{
	vector<char> & token = pattern[l];

	for(int i = 0, e = token.size(); i < e; ++i)
	{
		node * next = n->branch[token[i]];

		if(next)
			if(next == n)
				++K;
			else
				count(next, l + 1);
	}
}

int main()
{
	int L, D, N;
	cin >> L >> D >> N;

	pattern.resize(L);

	string line;

	for(int i = 0; i < D; ++i)
	{
		cin >> line;

		node * p = &root;

		for(int j = 0; j < L-1; ++j)
		{
			int b = line[j] - 'a';

			if(p->branch[b])
				p = p->branch[b];
			else
				p = p->branch[b] = new node();
		}

		p->branch[line[L-1] - 'a'] = p;
	}

	for(int X = 1; X <= N; ++X)
	{
		cin >> line;

		for(int t = 0, j = 0; t < L; ++t)
		{
			char c = line[j++];

			if(c == '(')
			{
				pattern[t].clear();

				while((c = line[j++]) != ')')
					pattern[t].push_back(c - 'a');
			}
			else
			{
				pattern[t].resize(1);
				pattern[t][0] = c - 'a';
			}
		}

		K = 0;
		count(&root, 0);
		cout << "Case #" << X << ": " << K << '\n';
	}

	return 0;
}