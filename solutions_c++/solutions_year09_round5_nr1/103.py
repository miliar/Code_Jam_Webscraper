#define _CRT_SECURE_NO_DEPRECATE
#pragma warning(disable: 4018)
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

const int XXs[4] = {0, 1, 0, -1};
const int YYs[4] = {1, 0, -1, 0};

struct node
{
	vector<pair<char, char> > State;
	bool D;
	int Val;
};

int NN, TT;
int N, M, L;
char Map[15][15];
bool Goals[15][15];
int Buffer[15][15];
set<long long> Hash;
vector<node> List;

long long convert(const vector<pair<char, char> >& State, bool D)
{
	long long Result = 0;
	for (int I = 0; I < State.size(); I++)
	{
		Result = Result * 16 + State[I].first;
		Result = Result * 16 + State[I].second;
	}
	if (!D) return Result;
	return -Result;
}

bool nonoverlapping(const vector<pair<char, char> >& State)
{
	bool Result = true;
	for (int I = 0; I < State.size(); I++) Buffer[State[I].first][State[I].second] = I;
	for (int I = 0; I < State.size(); I++)
	{
		int& Temp = Buffer[State[I].first][State[I].second];
		if (Temp != I) Result = false;
		Temp = -1;
	}
	return Result;
}

bool connected(const vector<pair<char, char> >& State)
{
	for (int I = 0; I < State.size(); I++) Buffer[State[I].first][State[I].second] = I;
	int Queue[10];
	bool Marks[10] = {0};
	int Len = 0;
	Queue[Len++] = 0;
	Marks[0] = true;
	for (int Cursor = 0; Cursor < Len; Cursor++)
	{
		pair<char, char> A = State[Queue[Cursor]];
		for (int D = 0; D < 4; D++)
		{
			char X = A.first + XXs[D];
			char Y = A.second + YYs[D];
			int Next = Buffer[X][Y];
			if (Next >= 0 && !Marks[Next])
			{
				Queue[Len++] = Next;
				Marks[Next] = true;
			}
		}
	}
	for (int I = 0; I < State.size(); I++) Buffer[State[I].first][State[I].second] = -1;
	return Len == State.size();
}

bool is_goal(const vector<pair<char, char> >& State)
{
	for (int I = 0; I < State.size(); I++)
		if (!Goals[State[I].first][State[I].second]) return false;
	return true;
}

int main()
{
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		cin >> N >> M;
		memset(Map, 1, sizeof Map);
		memset(Goals, false, sizeof Goals);
		memset(Buffer, -1, sizeof Buffer);
		vector<pair<char, char> > State;
		for (int X = 1; X <= N; X++) for (int Y = 1; Y <= M; Y++)
		{
			char Ch;
			cin >> Ch;
			if (Ch != '#') Map[X][Y] = 0;
			if (Ch == 'o' || Ch == 'w') State.push_back(make_pair(X, Y));
			if (Ch == 'x' || Ch == 'w') Goals[X][Y] = true;
		}
		Hash.clear();
		node Node;
		sort(State.begin(), State.end());
		Node.State = State;
		Node.D = false;
		Node.Val = 0;
		List.clear();
		List.push_back(Node);
		int Found = -1;
		for (int Cursor = 0; Cursor < List.size(); Cursor++)
		{
			Node = List[Cursor];
			State = Node.State;
			if (is_goal(State))
			{
				Found = Node.Val;
				break;
			}
			bool Oks[10][4] = {false};
			for (int I = 0; I < State.size(); I++) Buffer[State[I].first][State[I].second] = I;
			for (int I = 0; I < State.size(); I++)
				for (int D = 0; D < 4; D++)
				{
					Oks[I][D] = Map[State[I].first + XXs[D]][State[I].second + YYs[D]] == 0 && Buffer[State[I].first + XXs[D]][State[I].second + YYs[D]] == -1 &&
						Map[State[I].first - XXs[D]][State[I].second - YYs[D]] == 0 && Buffer[State[I].first - XXs[D]][State[I].second - YYs[D]] == -1;
				}
			for (int I = 0; I < State.size(); I++) Buffer[State[I].first][State[I].second] = -1;
			for (int I = 0; I < State.size(); I++)
				for (int D = 0; D < 4; D++)
					if (Oks[I][D])
					{
						State = Node.State;
						State[I].first += XXs[D];
						State[I].second += YYs[D];
						bool D = !connected(State);
						if (!Node.D || !D)
						{
							sort(State.begin(), State.end());
							long long Key = convert(State, D);
							if (Hash.insert(Key).second)
							{
								List.push_back(node());
								List.back().State = State;
								List.back().D = D;
								List.back().Val = Node.Val + 1;
							}
						}
					}
		}
		printf("Case #%d: %d\n", TT, Found);
	}
	return 0;
}