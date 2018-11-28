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
	ifstream fin("Al.in");
	ofstream fout("Al.out");
	int tests, n;
	fin >> tests;
	FOR (test, tests){
		fin >> n;
		vector <int> a, b;
		int val;
		FOR (i, n){
			fin >> val;
			a.pb(val);
		}
		FOR (i, n){
			fin >> val;
			b.pb(val);
		}
		sort(all(a));
		sort(all(b));
		long long ret = 0LL;
		FOR (i, a.sz)
			ret += (long long)(a[i]) * (long long)(b[b.sz - i - 1]);
		
/*		long long ret1 = 1LL << 61LL;
		vector <int> p1, p2;
		p1.clear();
		p2.clear();
		FOR (i, a.sz){
			p1.pb(i);
			p2.pb(i);
		}
		
		do{
			do{
				long long sum = 0;
				FOR (i, a.sz)
					sum += (long long)(a[p1[i]]) * (long long)(b[p2[i]]);
				ret1 = min(ret1, sum);
			}while (next_permutation(all(p2)));
		}while (next_permutation(all(p1)));
		if (ret1 != ret)
			cout << "Nije isto!" << endl;*/
		fout << "Case #" << (test + 1) << ": " << ret << endl;
	}
	fin.close();
	fout.close();
	system("pause");
	return 0;
}
