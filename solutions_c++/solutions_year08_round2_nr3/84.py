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

int bit[1000010];

int read(int idx){
	int ret = 0;
	while (idx){
		ret += bit[idx];
		idx -= (idx & (-idx));
	}
	return ret;
}

void add(int idx, int val){
	while (idx <= 1000000){
		bit[idx] += val;
		idx += (idx & (-idx));
	}
}

int pos[1000000 + 1], rret[1000000 + 1], gh[1000000 + 1];

int main(){
	ifstream fin("Cl.in");
	ofstream fout("Cl.out");
	int tests, n, k, rr;
	fin >> tests;
	FOR (test, tests){
		cout << test << endl;
		fin >> n;
		fin >> rr;
		FOR (i, rr)
			fin >> gh[i];
		SET(pos, 255);
		int cnt = 0, idx = 1;
		SET(bit, 0);		
		FOR (i, n)
			add(i + 1, 1);
		add(1, -1);
		pos[1] = 1;
		rret[1] = 1;
		ffor (i, 2, n + 1){
			int sum = read(n), go = i, before = read(idx);
			int after = sum - before;

			if (go > sum)
				go %= sum;
			if (go == 0)
				go = sum;
			int fsearch;
			if (after >= go)
				fsearch = before + go;
			else
				fsearch = go - after;
			int s = 1, e = n, ret, val;
			
			while (s <= e){
				int mid = (s + e) / 2;
				val = read(mid);
				if (val == fsearch){
					ret = mid;
					e = mid - 1;
				}
				else if (val > fsearch)
					e = mid - 1;
				else
					s = mid + 1;
			}
			idx = ret;
			pos[i] = idx;
			rret[idx] = i;
			add(idx, -1);
		}
		fout << "Case #" << (test + 1) << ":";
		FOR (i, rr)
			fout << " " << rret[gh[i]];

		fout << endl;
	}
	fin.close();
	fout.close();
	return 0;
}
