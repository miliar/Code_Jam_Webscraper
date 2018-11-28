#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <cctype>
#include <stack>
#include <queue>
#include <sstream>

using namespace std;

#define REP(i, T) for(int (i)=0; (i) < T; (i) ++)
#define FOR(i, L, R) for(int (i)=L; (i) < R; (i) ++)
#define PB push_back
#define ERS(v, i) (v).erase((v).begin()+(i))
#define ALL(v) v.begin(), v.end()
#define SORT(v) sort(ALL(v))
#define SZ(v) (int)v.size()
#define FILL(a, i) memset((a), (i), sizeof(a))
#define MAX(a, b) (((a)>(b))?(a):(b))
#define MIN(a, b) (((a)<(b))?(a):(b))

#define vi vector<int>
#define vs vector<string>
#define ll long long
#define pii pair<int, int>
#define pis pair<int, string>
#define psi pair<string, int>

#define INF 999999999
#define PI 3.141592654

int main(void)
{
	int T, n;
	cin >> T;
	for(int caso=1; caso<=T; caso++) {
		cin >> n;
		string row;
		vi v;
		REP(i, n) {
			cin >> row;
			int k=0;
			REP(j, SZ(row)) if(row[j]=='1') k=j;
			v.PB(k+1);	
		}
		
		int tot=0;
		REP(i, SZ(v)) {
			if(v[i]<=i+1) continue;
			int j=i+1;
			while(v[j]>i+1) j++;
			tot+=j-i;
			while(j>i) {
				int tmp=v[j];
				v[j] = v[j-1];
				v[j-1]=tmp;
				j--;
			}
		}
		
		cout << "Case #" << caso <<": " << tot << endl;
		
	}

	return 0;
}
