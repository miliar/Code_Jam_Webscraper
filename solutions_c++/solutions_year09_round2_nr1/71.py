#include <vector>
#include <algorithm>
#include <math.h>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <utility>
#include <numeric>
#include <fstream>

using namespace std;

#define		ALL(c)	(c).begin(),(c).end()
#define		SZ(c)	int((c).size())
#define		LEN(s)	int((s).length())
#define		FOR(i,n)	for(int i=0;i<(n);++i)
#define		FORD(i,a,b)	for(int i=(a);i<=(b);++i)
#define		FORR(i,a,b)	for(int i=(b);i>=(a);--i)
#define		MP	make_pair
#define		PB	push_back

typedef istringstream iss;
typedef ostringstream oss;
typedef long double ld;
typedef long long i64;
typedef pair<int,int> pii;

typedef vector<i64> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<vvvi> vvvvi;

struct tnode
{
	double p;
	string s;
	int a, b;
	//tnode(double _p, string _s, int _a, int _b): p(_p), s(_s), a(_a), b(_b) {}
};

vector<tnode> T;
string s;
int idx;

void rec(int nid)
{
	while (idx < LEN(s) && s[idx] == ' ') ++idx;
	++idx;
	while (idx < LEN(s) && s[idx] == ' ') ++idx;

	stringstream ss;
	while (s[idx]=='.' || isdigit(s[idx])) ss << s[idx++];
	ss >> T[nid].p;
	T[nid].s = "";

	while (idx < LEN(s) && s[idx] == ' ') ++idx;

	if (s[idx] == ')')
	{
		T[nid].a = -1;
		T[nid].b = -1;
		++idx;
		return;
	}

	while (isalpha(s[idx])) T[nid].s += s[idx++];

	T[nid].a = SZ(T);
	T.push_back(tnode());
	rec(SZ(T)-1);

	T[nid].b = SZ(T);
	T.push_back(tnode());
	rec(SZ(T)-1);

	while (idx < LEN(s) && s[idx] == ' ') ++idx;
	++idx;
}

set<string> feat;


double go(int i)
{
	if (T[i].s.empty()) return T[i].p;
	if (feat.count(T[i].s))
		return T[i].p * go(T[i].a);
	return T[i].p * go(T[i].b);
}

int main()
{
	ifstream fin("A.in"); ofstream fout("A.out");
	int NN;
	fin >> NN;
	char buf[100];
	FOR(tt, NN)
	{
		int L;
		fin >> L;
		fin.getline(buf, 100);
		s.clear();
		FOR(i, L)
		{
			fin.getline(buf, 100);
			s += buf;
		}

		T.clear();
		T.push_back(tnode());
		idx = 0;
		rec(0);

		int A;
		fin >> A;

		fout << "Case #" << tt+1 << ":" << endl;
		cout << "Case #" << tt+1 << ":" << endl;

		FOR(i, A)
		{
			int n;
			fin >> s >> n;
			feat.clear();
			FOR(j, n)
			{
				fin >> s;
				feat.insert(s);
			}
			double r = go(0);
			fout << fixed << setprecision(10) << r << endl;
			cout << fixed << setprecision(10) << r << endl;
		}

	}
	return 0;	
}
