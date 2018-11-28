#include <iostream>
using namespace std;

struct node
{
	bool val, changeable, type;
} nodes[10001];

unsigned int num_nodos, interiors, root, changes;
inline bool value(unsigned int node);
bool change(unsigned int max, unsigned int curr, unsigned int node);

int main(void)
{
	unsigned int num_casos;

	cin >> num_casos;
	for(unsigned int c = 1; c <= num_casos; c++)
	{
		memset(nodes, 0, sizeof(node) * 10001);

		cin >> num_nodos >> root;

		interiors = (num_nodos - 1) / 2;
		changes = 9999999;
		for(unsigned int i = 1; i <= interiors; i++) cin >> nodes[i].type >> nodes[i].changeable;
		for(unsigned int i = interiors + 1; i <= num_nodos; i++) cin >> nodes[i].val;

		for(unsigned int i = interiors; i; i--) nodes[i].val = value(i);

		if(value(1) == root) changes = 0;
		else
		{
			for(unsigned int i = 1; i <= num_nodos; i++)
			{
				if(change(i, 0, 1))
				{
					changes = i;
					break;
				}
			}
		}

		cout << "Case #" << c << ": ";
		if(changes == 9999999) cout << "IMPOSSIBLE" << endl;	
		else cout << changes << endl;
	}
}

inline bool value(unsigned int node)
{
	if(node > interiors) return nodes[node].val;

	if(nodes[node].type) return (value(2 * node) && value(2 * node + 1));
	else return (value(2 * node) || value(2 * node + 1));
}
bool change(unsigned int max, unsigned int curr, unsigned int node)
{
	if(curr >= max) return false;
	for(unsigned int n = node; n <= num_nodos; n++)
	{
		if(nodes[n].changeable)
		{
			nodes[n].type = !nodes[n].type;
			if(value(1) == root) return true;
			if(curr < max && change(max, curr + 1, n + 1)) return true;
			nodes[n].type = !nodes[n].type;
		}
	}
	return false;
}
