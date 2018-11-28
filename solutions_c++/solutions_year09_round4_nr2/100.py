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
	int X, Y, R, RR, D;
};

int NN, TT;
int N, M, MaxH;
int Map[11];
int Hash[11][7][64][64];
vector<node> Lists[60];
int Result;

int convert(int D)
{
	if (D < 0) return 0x7fffffff;
	return D;
}

void push_node(node Node)
{
	if (Node.D >= convert(Hash[Node.X][Node.Y][Node.R][Node.RR])) return;
	Hash[Node.X][Node.Y][Node.R][Node.RR] = Node.D;
	Lists[Node.D].push_back(Node);
}

int main()
{
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		cin >> N >> M >> MaxH;
		for (int X = 0; X < N; X++)
		{
			char S[51];
			cin >> S;
			int Temp = 0;
			for (int Y = 0; Y < M; Y++) if (S[Y] == '#') Temp |= 1 << Y;
			Map[X] = Temp;
		}
		Map[N] = (1 << M) - 1;
		memset(Hash, -1, sizeof Hash);
		for (int D = 0; D < 60; D++) Lists[D].clear();
		node Node;
		Node.X = 0;
		Node.Y = 0;
		Node.R = Map[0];
		Node.RR = Map[1];
		Node.D = 0;
		push_node(Node);
		Result = -1;
		for (int D = 0; D < 60; D++)
			for (int Cursor = 0; Cursor < (int)Lists[D].size(); Cursor++)
			{
				if (Result >= 0) break;
				Node = Lists[D][Cursor];
				if (Node.D != Hash[Node.X][Node.Y][Node.R][Node.RR]) continue;
				if (Node.X == N - 1)
				{
					Result = Node.D;
					break;
				}
				node NewNode;
				for (int Dir = -1; Dir <= 1; Dir++) if (Dir != 0)
				{
					int Y = Node.Y + Dir;
					if (Y < 0 || Y >= M) continue;
					if ((Node.R >> Y) & 1) continue;
					if ((Node.RR >> Y) & 1)
					{
						NewNode.X = Node.X;
						NewNode.Y = Y;
						NewNode.R = Node.R;
						NewNode.RR = Node.RR;
						NewNode.D = Node.D;
						push_node(NewNode);
						continue;
					}
					int X = Node.X + 1;
					while (!((Map[X + 1] >> Y) & 1)) X++;
					if (X - Node.X > MaxH) continue;
					NewNode.X = X;
					NewNode.Y = Y;
					NewNode.R = Map[X];
					if (X == Node.X + 1) NewNode.R = Node.RR;
					NewNode.RR = Map[X + 1];
					NewNode.D = Node.D;
					push_node(NewNode);
				}
				for (int Dir = -1; Dir <= 1; Dir++) if (Dir != 0)
				{
					int Y = Node.Y + Dir;
					if (Y < 0 || Y >= M) continue;
					if ((Node.R >> Y) & 1) continue;
					if (!((Node.RR >> Y) & 1)) continue;
					NewNode = Node;
					NewNode.RR ^= 1 << Y;
					NewNode.D = Node.D + 1;
					push_node(NewNode);
				}
			}

		printf("Case #%d: ", TT);
		if (Result < 0) printf("No\n");
		else printf("Yes %d\n", Result);
	}
	return 0;
}