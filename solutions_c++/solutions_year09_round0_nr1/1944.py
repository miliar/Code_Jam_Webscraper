#include <string>
#include <fstream>
#include <vector>
using namespace std;

const int C = 26;

class Node
{
	public:
		Node* nodes[C];
		Node()
		{
			for (int i = 0; i < C; i++)
				nodes[i] = NULL;
		}
};

int main()
{
	ifstream fin("test.txt");
	int L = 0, D = 0, N = 0;
	fin >> L >> D >> N;
	Node root = Node();
	Node* last;
	string word;
	int idx;
	for (int i = 0; i < D; i++)
	{
		fin >> word;
		// insert word
		last = &root;
		for (int j = 0; j < (int)word.size(); j++)
		{
			idx = word[j] - 'a';
			if (last->nodes[idx] == NULL)
			{
				last->nodes[idx] = new Node();
			}
			last = last->nodes[idx];
		}
	}
	ofstream fout("words.txt");
	for (int i = 0; i < N; i++)
	{
		fin >> word;
		vector<Node*> current(1, &root);
		for (int j = 0; j < (int)word.size(); j++)
		{
			if (word[j] == '(')
			{
				j++;
				vector<Node*> temp;
				for (; j < (int)word.size(); j++)
				{
					if (word[j] == ')')
						break;
					idx = word[j] - 'a';
					
					for (int k = 0; k < (int)current.size(); k++)
					{
						if (current[k]->nodes[idx] != NULL)
						{
							temp.push_back(current[k]->nodes[idx]);
						}
					}
				}
				current = temp;
			}
			else
			{
				idx = word[j] - 'a';
				vector<Node*> temp;
				for (int k = 0; k < (int)current.size(); k++)
				{
					if (current[k]->nodes[idx] != NULL)
					{
						temp.push_back(current[k]->nodes[idx]);
					}
				}
				current = temp;
			}
		}
		// parse word
		fout << "Case #" << i + 1 << ": " << (int)current.size() << endl;
	}
	fout.close();
	return 0;
}