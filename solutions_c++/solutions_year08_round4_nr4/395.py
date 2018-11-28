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
	ifstream fin("Ds.in");
	ofstream fout("Ds.out");
	int tests, k, idx1, idx, cnt;
	fin >> tests;
	string text, ntext;
	vector <int> perm;
	int ret;
	FOR (test, tests){
		fin >> k;
		fin >> text;
		ret = 1 << 30;
		perm.clear();
		FOR (i, k)
			perm.pb(i);
		do{
			ntext = "";
			FOR (i, text.sz / k)
				FOR (j, k)
					ntext += string() + text[perm[j] + i * k];
			// count blocks
			idx = 0;
			cnt = 0;
			while (idx < ntext.sz){
				cnt++;
				idx1 = idx + 1;
				while (idx1 < ntext.sz && ntext[idx1] == ntext[idx])
					idx1++;
				idx = idx1;
			}
			ret <?= cnt;
		}while (next_permutation(all(perm)));
		
		fout << "Case #" << (test + 1) << ": " << ret << endl;
		cout << "Case #" << (test + 1) << ": " << ret << endl;
	}
	system("pause");
	return 0;
}
