#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>

using namespace std;

struct t_node
{
	map<char, t_node*> m_nodes;
	
	~t_node()
	{
		if (!m_nodes.empty())
		{
			for (map<char, t_node*>::iterator it = m_nodes.begin(); it != m_nodes.end(); ++it)
			{
				delete it->second;
			}
		}
	}
};


ifstream fin("c:\\A-small-attempt0.in");
ofstream fout("c:\\A-small.out");

#define cin fin
#define cout fout

int main()
{
	int L;
	int D;
	int N;
	cin >> L >> D >> N;
	t_node root;
	t_node *p_node;
	// Build tree
	for (int d = 0; d < D; ++d)
	{
		string word;
		cin >> word;
		p_node = &root;
		for (int l = 0; l < L; ++l)
		{
			if (p_node->m_nodes.find(word[l]) == p_node->m_nodes.end())
			{
				// Insert char->node pair to m_nodes
				p_node->m_nodes[word[l]] = new t_node;
			}
			p_node = p_node->m_nodes[word[l]];
		}
	}
	// Matching cases
	for(int n = 0; n < N; ++n)
	{
		string line;
		cin >> line;
		queue<t_node *> possible_matches;
		possible_matches.push(&root);
		for (string::size_type pos = 0; !possible_matches.empty() && pos < line.length(); ++pos)
		{
			queue<t_node *>::size_type n_matches = possible_matches.size();
			vector<char> chars;
			char t = line[pos];
			if (t == '(')
			{
				// Look forward until meet ')'
				while ( (t = line[++pos]) != ')' )
				{
					chars.push_back(t);
				}
			}
			else
			{
				chars.push_back(t);
			}
			for (queue<t_node *>::size_type i = 0; i < n_matches; ++i)
			{
				t_node *this_node = possible_matches.front();
				possible_matches.pop();
				for (vector<char>::iterator it = chars.begin(); it != chars.end(); ++it)
				{
					if (this_node->m_nodes.find(*it) != this_node->m_nodes.end())
					{
						possible_matches.push(this_node->m_nodes[*it]);
					}
				}
			}
		}
		cout << "Case #" << n + 1 << ": " << possible_matches.size() << endl;
	}
	return 0;
}