#define _CRT_SECURE_NO_DEPRECATE
#ifdef NDEBUG
	#define _SECURE_SCL 0
#endif
#include <iostream>
#include <memory>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <sstream>
#include <utility>
#include <functional>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;

struct node
{
	double P;
	string F;
	node* A, *B;
};

int NN, TT;
int N;

node* read_tree(stringstream& Str)
{
	node* Node = new node;
	char Ch;
	Str >> Ch >> Node->P;
	Node->A = Node->B = 0;
	Str >> Ch;
	if (Ch == ')') return Node;
	string S;
	if (Str.peek() >= 'a' && Str.peek() <= 'z') Str >> S;
	Node->F = Ch + S;
	Node->A = read_tree(Str);
	Node->B = read_tree(Str);
	Str >> Ch;
	return Node;
}

void erase_tree(node* Node)
{
	if (Node == 0) return;
	erase_tree(Node->A);
	erase_tree(Node->B);
	delete Node;
}

int main()
{
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		int L;
		cin >> L;
		string Line, Lines;
		getline(cin, Line);
		while (L-- > 0)
		{
			getline(cin, Line);
			Lines += " " + Line;
		}
		stringstream Str(Lines);
		node* Tree = read_tree(Str);
		cin >> N;
		printf("Case #%d:\n", TT);
		while (N-- > 0)
		{
			string S;
			set<string> Fs;
			int M;
			cin >> S >> M;
			while (M-- > 0)
			{
				cin >> S;
				Fs.insert(S);
			}
			node* Node = Tree;
			double P = 1;
			while (Node != 0)
			{
				P *= Node->P;
				if (Node->A != 0)
					if (Fs.find(Node->F) != Fs.end()) Node = Node->A;
					else Node = Node->B;
				else
					Node = 0;
			}
			printf("%.7f\n", P);
		}
	}
	return 0;
}