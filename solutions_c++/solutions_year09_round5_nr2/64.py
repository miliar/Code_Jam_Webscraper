#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std; 

#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define FOR2(i, a, b) for (int i = (a); i > (b); --i)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

const int INF = 1 << 29;
typedef long long ll;

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return n & two(b); }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=last_bit(n); return res; }

///////////////////////////////////////////////////////////////////////////////////////////////////////////////

//FILE * fin = fopen("vstup.txt", "r");
//FILE * fout = fopen("vystup.txt", "w");

ifstream fin("vstup.txt");
ofstream fout("vystup.txt");

const int MOD = 10009;

map<string, int> counts[11];
vector<string> dict;

void count_letters(const string & str, int * counts)
{
	FOR(i, 0, 26) counts[i] = 0;
	FOR(i, 0, str.size())
		++counts[str[i]-'a'];
}

//najde sumu pre K slov a zadany term
int go(string term, int K)
{	
	map<string, int>::iterator iter = counts[K].find(term);
	if (iter != counts[K].end())
		return iter->second;

	int res = 0;

	if (term.empty())
	{
		res = 1;
		FOR(i, 0, K) res *= dict.size();
	}
	//vyrata odpoved
	else if (K == 1) //len jedno slovo
	{
		//prejde rucne
		int counts[26];
		FOR(i, 0, dict.size())
		{
			count_letters(dict[i], counts);
			int temp = 1;
			FOR(j, 0, term.size()) temp = (temp * counts[term[j]-'a']) % MOD;
			res = (res + temp) % MOD;
		}
	}
	else //rozdeli si to na jedno slovo a K-1 slov
	{
		FOR(mask, 0, two(term.size()))
		{
			string term1, term2;
			FOR(i, 0, term.size())
				if (test(mask, i)) term1 += term[i];
				else term2 += term[i];
			res = (res + go(term1, K-1) * go(term2, 1)) % MOD;
		}
	}

	return counts[K][term] = res;
}

void Solve(int tc)
{
	//nacita vstupy
	string expr;
	fin >> expr;

	//nakuskuje vyraz na termy
	vector<string> terms;
	int index = 0;
	while (index < expr.size())
	{
		string temp;
		while (index < expr.size() && expr[index] != '+')
			temp += expr[index++];
		terms.push_back(temp);
		++index; //preskoci plus
	}

	int K, N;
	fin >> K >> N;

	dict.resize(N);
	FOR(i, 0, N)
		fin >> dict[i];

	//vymaze dynamiku
	FOR(i, 0, 11) counts[i].clear();

	vector<int> results(K+1, 0);
	//pre kazdy term pocita zvlast
	FOR(i, 0, terms.size())
		FOR(j, 1, K+1)
			results[j] = (results[j] + go(terms[i], j)) % MOD;

	fout << "Case #" << tc << ":";
	FOR(i, 1, K+1)
		fout << " " << results[i];
	fout << endl;
}

int main()
{
	int T;
	fin >> T;
	FOR(step, 0, T) Solve(step+1);

	return 0;
}