#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <queue>

using namespace std;

#define VALUE 2
#define AND_GATE 1
#define OR_GATE 0


const int IMPOSSIBLE = 40000;

struct Node
{
	bool Value;
	short Type;
	bool CanChange;
	Node(short _Type, bool _CanChange = false, bool _Value = 0):CanChange(_CanChange),Type(_Type), Value(_Value)
	{

	}
	Node()
	{
		Value = Type = CanChange = 0;

	}
};

vector <vector <int> > Children;
vector <Node> All;



bool Eval(int Node)
{
	switch (All[Node].Type)
	{
	case VALUE:
		return All[Node].Value;
		break;
	case AND_GATE:
		return (Eval(Children[Node][0]) && Eval(Children[Node][1]));
		break;
	case OR_GATE:
		return (Eval(Children[Node][0]) || Eval(Children[Node][1]));
		break;
	}
	return false;
}

int GetLeast(int Node, bool V)
{
	if (Eval(Node) == V)
	{
		return 0;
	}
	int C1,C2;

	switch (All[Node].Type)
	{
	case VALUE:
		if (All[Node].Value == V)
			return 0;
		if (All[Node].CanChange)
			return 1;
		else
			return IMPOSSIBLE;
		break;
	case AND_GATE:
		C1 = Children[Node][0];
		C2 = Children[Node][1];
		if (All[Node].CanChange)
		{
			if (V)
			{
				return 1 + min(GetLeast(C1, true), GetLeast(C2, true));
			}
		}
		if (V)
		{
			return GetLeast(C1, true) + GetLeast(C2, true);
		}
		else
		{
			return min(GetLeast(C1, false), GetLeast(C2, false));
		}
		break;
	case OR_GATE:
		C1 = Children[Node][0];
		C2 = Children[Node][1];
		if (All[Node].CanChange)
		{
			if (!V)
			{
				return 1 + min(GetLeast(C1, false), GetLeast(C2, false));
			}
		}
		if (V)
		{
			return min(GetLeast(C1, true), GetLeast(C2, true));
		}
		else
		{
			return GetLeast(C1, false) + GetLeast(C2, false);
		}
		break;
	}
}

/*
  G and C, each being either 0 or 1. If G is 1 then the gate for this node is an AND gate,
   otherwise it is an OR gate. If C is 1 then the gate for this node is changeable, otherwise
   it is not. Interior node X has nodes 2X and 2X+1 as children.
 * */
int main()
{
	ifstream cin ("A.in");
	ofstream cout ("A.Out");

	int nCases;
	cin >> nCases;
	for (int iCase = 1; iCase <= nCases; ++iCase)
	{
		Children.clear();
		All.clear();
		int M, V;
		cin >> M >> V;
		Children.resize(M);
		All.resize(M);
		queue <int> Nodes;
		Nodes.push(0);

		bool G, C;
		cin >> G>>C;
		All[0] = Node(G,C,0);

		for (int i=1; i < (M-1)/2; ++i)
		{

			int Current = Nodes.front();
			if (Children[Current].size() == 2)
			{
				Nodes.pop();
				Current = Nodes.front();
			}
			cin >> G >> C;
			All[i] = Node(G,C,0);
			//Children[Current].push_back(Node(G, C, 0));
			Children[Current].push_back(i);
			Nodes.push(i);
		}
		for (int i=0; i < (M+1)/2; ++i)
		{
			int v;
			int Current = Nodes.front();
			if (Children[Current].size() == 2)
			{
				Nodes.pop();
				Current = Nodes.front();
			}
			cin >> v;
			//Children[Current].push_back(Node(VALUE, false, v));
			All[i+(M-1)/2] = Node(VALUE, false, v);
			Children[Current].push_back(i+(M-1)/2);
		}


		cout << "Case #" << iCase <<": ";
		int Res = GetLeast(0, V);
		if (Res >= IMPOSSIBLE)
			cout << "IMPOSSIBLE"<<endl;
		else cout << Res << endl;
	}
	return 0;
}
