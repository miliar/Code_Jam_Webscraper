#pragma warning(disable:4786)

#include <vector>
#include <string>
#include <map>
#include <set>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <sstream>
#include <iostream>
#include <math.h>
#include <fstream>

using namespace std;

#define VT vector
typedef VT<int> VI;
typedef VT<VI> VVI;
typedef VT<string> VS;
typedef VT<double> VD;
typedef pair<int,int> PII;
#define REP(i,n) for (int i = 0; i < (n); i++)
#define ALL(c) c.begin(),c.end()
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz size()

ifstream ifs;
ofstream ofs;

typedef long long ll;

int n, k;
VVI t;

ll res;

void go(int v, int p) {

	int s = 0;
	if (p != -1)
		s = t[p].sz;

	REP(i, t[v].sz)
		if (t[v][i] != p) {
			res = res * (k-s);
			res %= 1000000009;

			s++;

			go(t[v][i], v);
		}
}


void testcase(int tst)
{
	ifs >> n >> k;

	t.assign(n, VI());

	REP(i, n-1) {
		int v1, v2;
		ifs >> v1 >> v2;
		v1--;
		v2--;

		t[v1].pb(v2);
		t[v2].pb(v1);
	}


	res = 1;
	go(0, -1);

	char buf[100];
	sprintf(buf, "%ld", res);
	ofs << "Case #" << tst+1 << ": " << buf << endl;
}

int main()
{
	ifs.open("input.txt");
	ofs.open("output.txt");
	
	int t;
	ifs >> t;
	REP(tn, t)
	{
		testcase(tn);
	}

	return 0;
} 
