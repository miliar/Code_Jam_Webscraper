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

int NN, TT;
multimap<int, int> Map;

void add(int Pos)
{
	int Left = Pos;
	int Right = Pos;
	multimap<int, int>::iterator It = Map.upper_bound(Pos);
	if (It != Map.begin())
	{
		multimap<int, int>::iterator It2 = It;
		--It2;
		if (It2->second == Pos - 1)
		{
			Left = It2->first;
			Map.erase(It2);
		}
	}
	if (It != Map.end() && It->first == Pos + 1)
	{
		Right = It->second;
		Map.erase(It);
	}
	Map.insert(make_pair(Left, Right));
}

void remove(int Pos)
{
	multimap<int, int>::iterator It = Map.upper_bound(Pos);
	if (It != Map.begin()) --It;
	if (It->first < Pos)
		Map.insert(make_pair(It->first, Pos - 1));
	if (It->second > Pos)
		Map.insert(make_pair(Pos + 1, It->second));
	Map.erase(It);
}

long long put(int Pos)
{
	int Left = Pos;
	int Right = Pos;
	multimap<int, int>::iterator It = Map.upper_bound(Pos);
	if (It != Map.begin()) --It;
	if (It == Map.end() || It->first > Pos || It->second < Pos)
	{
		add(Pos);
		return 0;
	}
	Left = It->first;
	Right = It->second;
	add(Left - 1);
	add(Right + 1);
	remove(Left + Right - Pos);
	return (long long)(Right - Pos + 1) * (Pos - Left + 1);
}

int main()
{
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		long long Result = 0;
		Map.clear();
		int N;
		cin >> N;
		while (N-- > 0)
		{
			int Pos, V;
			cin >> Pos >> V;
			while (V-- > 0) Result += put(Pos);
		}
		cout << "Case #" << TT << ": " << Result << endl;
	}
	return 0;
}