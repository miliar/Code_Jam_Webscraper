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

/*class 
{
private:
	
public:
	
};*/

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return n & two(b); }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=last_bit(n); return res; }

///////////////////////////////////////////////////////////////////////////////////////////////////////////////

ifstream fin("A-large.in");
ofstream fout("vystup.txt");

struct Node
{
	Node() { FOR(i, 0, 26) next[i] = NULL; }
	Node * next[26];
};

int L, D, N;
int result;

void go(Node * node, const string & word, int index, int depth)
{
	if (depth == L) { ++result; return; }

	if (word[index] != '(')
	{
		if (node->next[word[index]-'a'])
			go(node->next[word[index]-'a'], word, index+1, depth+1);
	}
	else
	{
		int end = ++index;
		while (end < word.size() && word[end] != ')') ++end;

		FOR(i, index, end)
		{
			if (node->next[word[i]-'a'])
				go(node->next[word[i]-'a'], word, end+1, depth+1);
		}
	}
}

int main()
{
	fin >> L >> D >> N;

	Node * root = new Node();
	FOR(i, 0, D)
	{
		string word;
		fin >> word;
		
		Node * node = root;
		FOR(j, 0, L)
		{
			if (node->next[word[j]-'a'] == NULL)
				node->next[word[j]-'a'] = new Node();
			node = node->next[word[j]-'a'];
		}
	}

	FOR(step, 0, N)
	{
		string input;
		fin >> input;

		result = 0;
		go(root, input, 0, 0);
		fout << "Case #" << step+1 << ": " << result << endl;
	}

	return 0;
}
