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
FILE * fout = fopen("vystup.txt", "w");
//ofstream fout("vystup.txt");

struct Node
{
	Node(): prob(0.0), left(NULL), right(NULL) { }
	double prob;
	string feature;
	Node * left, * right;
};

void skip_white(const string & input, int & index)
{
	while (isspace(input[index])) ++index;
}

//index ukazuje na lavu otvaraciu zatvorku -> vrati index za lavu zatvorku
Node * construct(const string & input, int & index)
{
	Node * node = new Node();

	//preskoci zatvorku
	++index;

	//nacita pp.
	string str_pp;
	skip_white(input, index);
	while (isdigit(input[index]) || input[index] == '.') str_pp += input[index++];

	istringstream is(str_pp);
	is >> node->prob;

	skip_white(input, index);
	//ak dosiel na koniec
	if (input[index] == ')')
	{
		++index;
		return node;
	}

	//inak nacita feature
	while (isalpha(input[index])) node->feature += input[index++];

	//nacita lavy strom
	skip_white(input, index);
	node->left = construct(input, index);
	//nacita pravy strom
	skip_white(input, index);
	node->right = construct(input, index);
	//najde si pravu zatvorku
	skip_white(input, index);
	++index; //skoci za zatvorku
	return node;
}

void destroy(Node * node)
{
	if (node->left)
	{
		destroy(node->left);
		destroy(node->right);
	}
	delete node;
}

void solve(int T)
{
	int L; //pocet riadkov
	fin >> L;

	string tree, line;
	getline(fin, line);
	FOR(i, 0, L)
	{
		getline(fin, line);
		tree += line;
	}

	int index = 0;
	Node * root = construct(tree, index);

	//vypise uvod
	//fout << "Case #" << T << ":" << endl;
	fprintf(fout, "Case #%d:\n", T);

	int A; //pocet zvierat
	fin >> A;
	FOR(step, 0, A)
	{
		string animal;
		int N;
		set<string> feature;

		fin >> animal >> N;
		FOR(i, 0, N)
		{
			fin >> line;
			feature.insert(line);
		}

		//vyrata pp.
		Node * node = root;
		double prob = 1.0;

		while (1)
		{
			prob *= node->prob;
			if (node->feature == "") break;
			if (feature.find(node->feature) != feature.end())
				node = node->left;
			else
				node = node->right;
		}

		fprintf(fout, "%.9lf\n", prob);
	}

	destroy(root);
}

int main()
{
	int N;

	fin >> N;
	FOR(step, 0, N)
		solve(step+1);

	return 0;
}
