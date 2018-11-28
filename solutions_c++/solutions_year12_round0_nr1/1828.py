/*
 * 2012-04-14  Martin  <Martin@Martin-desktop>

 * 
 */
#include <climits>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstdarg>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <exception>
#include <stdexcept>
#include <memory>
#include <locale>
#include <bitset>
#include <deque>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <algorithm>
#include <iterator>
#include <functional>
#include <string>
#include <complex>
#include <valarray>

using namespace std;

template <class T> inline T checkmin(T &a, T b)
{
	return (a < b) ? a : a = b;
}

template <class T> inline T checkmax(T &a, T b)
{
	return (a > b) ? a : a = b;
}

template <class T> T GCD(T a, T b)
{
	if (a < 0)
		return GCD(- a, b);
	if (b < 0)
		return GCD(a, - b);
	return (a == 0) ? b : GCD(b % a, a);
}

template <class T> T LCM(T a, T b)
{
	if (a < 0)
		return LCM(- a, b);
	if (b < 0)
		return LCM(a, - b);
	return (a == 0 || b == 0) ? 0 : a / GCD(a, b) * b;
}

template <class T> T ExtGCD(T a, T b, T &x, T &y)
{
	if (a < 0)
	{
		T c = ExtGCD(- a, b, x, y);
		x = - x;
		return c;
	}
	if (b < 0)
	{
		T c = ExtGCD(a, - b, x, y);
		y = - y;
		return c;
	}
	if (a == 0)
	{
		x = 0, y = 1;
		return b;
	}
	else
	{
		T c = ExtGCD(b % a, a, y, x);
		x -= b / a * y;
		return c;
	}
}

template <class T> inline T sqr(T X)
{
	return X * X;
}

#define tr(i, x) for (typeof(x.begin()) i = x.begin(); i != x.end(); ++ i)
#define rep(i, n) for (int i = 0; i < n; ++ i)
#define pii pair <int, int>
#define mp make_pair
#define pb push_back
#define x first
#define y second
#define ll long long

namespace Poor
{
	const int MaxiT = 33;
	const int MaxiG = 150;
	
	int TestCase;
	int Best;
	char St[MaxiT][MaxiG];
	char Perm[26], Now[26];
	set <string> Set[MaxiG];
	
	void LoadDict()
	{
		FILE *fin = fopen("A.dict.txt", "r");
		char Word[100];
		while (fscanf(fin, "%s", Word) != EOF)
		{
			bool Flag = 1;
			int L = strlen(Word);
			rep (i, L)
			{
				if (isupper(Word[i]))
					Word[i] += (int) 'a' - 'A';
				if (!islower(Word[i]))
					Flag = 0;
			}
			if (Flag)
				Set[L].insert(Word);
		}
		fclose(fin);
	}
	
	map <string, int> Map;
	
	void Update(int Flag = 0)
	{
		int res = 0;
		tr (it, Map)
		{
			string S;
			tr (eit, it->x)
				S.pb(Now[*eit - 'a']);
			if (Set[S.size()].count(S))
				res += it->y;
		}
		if (res >= Best)
		{
			Best = res;
			memcpy(Perm, Now, sizeof(Perm));
		}
		else
		{
			if (rand() % 100 < 40 || res < Best / 2 || Flag)
				memcpy(Now, Perm, sizeof(Perm));
		}
	}
	
	void Change(int i, char x)
	{
		if (Now[i] == x)
			return;
		rep (k, 26)
			if (Now[k] == x)
			{
				swap(Now[i], Now[k]);
				return;
			}
	}
	
	void Work()
	{
		Best = - 1;
		rep (i, 26)
			Now[i] = 'a' + i;
		rep (i, 26)
		{
			int x = rand() % 26;
			swap(Now[i], Now[x]);
		}
		Update();
		rep (i, TestCase)
		{
			stringstream SS;
			SS << St[i];
			string S;
			while (SS >> S)
				++ Map[S];
		}
		int MaxAppear = 0;
		tr (it, Map)
			checkmax(MaxAppear, it->y);
		map <string, vector <string> > Candidate;
		tr (it, Map)
		{
			int L = it->x.size();
			if (Set[L].empty())
				continue;
			tr (sit, Set[L])
			{
				map <char, char> Ha;
				rep (i, L)
					Ha[it->x[i]] = (*sit)[i];
				bool Able = 1;
				rep (i, L)
					if (Ha[it->x[i]] != (*sit)[i])
					{
						Able = 0;
						break;
					}
				if (!Able)
					continue;
				Candidate[it->x].pb(*sit);
				if (rand() % (120 * MaxAppear) < (100 * it->y))
				{
					rep (i, L)
						Change(it->x[i] - 'a', (*sit)[i]);
					Update();
					break;
				}
			}
		}
		rep (tt, 3)
		{
			rep (t, 600)
			{
				tr (it, Map)
					if (Candidate.count(it->x) && rand() % (120 * MaxAppear) < (100 * it->y))
					{
						vector < pair <int, string> > List;
						rep (k, 5)
						{
							string S = Candidate[it->x][rand() % Candidate[it->x].size()];
							int Same = 0;
							rep (i, (int) S.size())
								Same += (Now[it->x[i] - 'a'] == S[i]);
							List.pb(mp(Same, S));
						}
						sort(List.begin(), List.end());
						string S = List.back().y;
						rep (i, (int) S.size())
							Change(it->x[i] - 'a', S[i]);
						Update();
					}
			}
			memcpy(Now, Perm, sizeof(Perm));
			rep (fff, 10)
				rep (a, 26)
					rep (b, a)
					{
						swap(Now[a], Now[b]);
						Update(1);
					}
		}
	}
	
	string Print(int i)
	{
		string S;
		int L = strlen(St[i]);
		rep (j, L)
		{
			if (islower(St[i][j]))
				S.pb(Perm[St[i][j] - 'a']);
			else
				S.pb(St[i][j]);
		}
		return S;
	}
	
	void Run()
	{
		scanf("%d\n", &TestCase);
		rep (i, TestCase)
			gets(St[i]);
		LoadDict();
		Work();
		for (int i = 1; i <= TestCase; ++ i)
			printf("Case #%d: %s\n", i, Print(i - 1).c_str());
	}
}

int main()
{
	Poor::Run();
	return 0;
}
