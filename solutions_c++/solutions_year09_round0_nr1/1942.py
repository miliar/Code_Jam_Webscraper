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
 
 
ifstream fin("C:\\A-small.in");
ofstream fout("C:\\A-small.out");
 
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
			int chars_begin = pos;
			int chars_end;
			if (line[pos] == '(')
			{
				chars_begin++;
				chars_end = line.find_first_of(')', chars_begin);
				pos = chars_end;
			}
			else
			{
				chars_end = chars_begin + 1;
			}
			for (queue<t_node *>::size_type i = 0; i < n_matches; ++i)
			{
				t_node *this_node = possible_matches.front();
				possible_matches.pop();
				for (int char_pos = chars_begin; char_pos != chars_end; ++char_pos)
				{
					char ch = line[char_pos];
					if (this_node->m_nodes.find(ch) != this_node->m_nodes.end())
					{
						possible_matches.push(this_node->m_nodes[ch]);
					}
				}
			}
		}
		cout << "Case #" << n + 1 << ": " << possible_matches.size() << endl;
	}
	return 0;
}
