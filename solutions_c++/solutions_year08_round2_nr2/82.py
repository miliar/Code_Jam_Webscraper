#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <stack>
#include <list>
#include <numeric>
#include <bitset>
#include <ext/algorithm>
#include <ext/numeric>
#include <fstream>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
typedef long long LL; using namespace std;

int main(){
	ifstream fin("Bs.in");
	ofstream fout("Bs.out");
	int tests;
	fin >> tests;
	vector <int> pp;
	// looking for all prime numbers
	bool prime[1001];
	SET(prime, 0);
	ffor (i, 2, 1001)
		if (!prime[i]){
			pp.pb(i);
			for (int j = 2 * i; j < 1001; j += i)
				prime[j] = true;
		}

	FOR (test, tests){
		int sidx = 0;
		int a, b, p;
		fin >> a >> b >> p;
		while (sidx < pp.sz && pp[sidx] < p)
			sidx++;

		int set[b + 1];
		ffor (i, a , b + 1)
			set[i] = i;
			
		ffor (i, a, b + 1)
			ffor (j, i + 1, b + 1){
				if (set[i] == set[j])
					continue;
				bool same = false;
				ffor (k, sidx, pp.sz)
					if (i % pp[k] == 0 && j % pp[k] == 0){
						same = true;
						break;
					}
				if (same){
					FOR (k, b + 1)
						if (set[k] == set[j])
							set[k] = set[i];
				}
			}
		int ret = 0;
		vector <int> aa;
		aa.clear();
		ffor (i, a, b + 1)
			aa.pb(set[i]);
		sort(all(aa));
		int idx = 0;
		while (idx < aa.sz){
			ret++;
			int j = idx + 1;
			while (j < aa.sz && aa[j] == aa[idx])
				j++;
			idx = j;
		}
		fout << "Case #" << (test + 1) << ": " << ret << endl;
	}
	fin.close();
	fout.close();
	system("pause");
	return 0;
}
