#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <fstream>

using namespace std;

typedef vector <string> vs;
typedef vector <int> vi;
#define REP(a,b) for(long long a=0;a<(b);++a)
#define FOR(a,c,b) for(long long  a=c;a<(b);++a)


int main()
{
	int t;

	//ifstream fin("B-small.in");
	//ofstream fout("B-small.out");
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");

	fin >> t;

	string num;

	getline(fin,num);

	REP(tc,t) {
		fout <<"Case #"<<tc+1<<": ";	

		getline(fin,num);
		vector <char> v, v2;

		REP(i,num.size()) {
			v.push_back(num[i]);
		}

		if (next_permutation(num.begin(), num.end())) {
			REP(i,num.size()) {
				fout << num[i];
			}
			fout << endl;
		} else {
			int nz = 0;
			v2.clear();
			REP(i,num.size()) {
				if (v[i] != '0') v2.push_back(v[i]);
				else ++nz;
			}
			sort(v2.begin(), v2.end());
			fout << v2[0];
			REP(i,nz+1) fout << '0';
			FOR(i,1,v2.size()) fout << v2[i];
			fout << endl;
		}		
	}

	fin.close();
	fout.close();

	return 0;
}

