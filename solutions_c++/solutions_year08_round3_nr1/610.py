////============================================================================
//// Name        : traintime.cpp
//// Author      : Lahiru Lakmal Priyadarshana
//// Version     :
//// Copyright   : 
//// Description : Train Timetable | Google Code Jam 2008
////============================================================================

#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;

typedef long long int64;
typedef vector<int> vii;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int,int> pii;
typedef vector<int64> vi;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define AllV(v) (v).begin(), (v).end()
#define AllA(a,l)  a, a+l

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

bool myfunction (int i,int j) { return (i>j); }

int main() {
	freopen("/home/lahiru/workstation/workspace/CodeJam/src/A-small.in", "rt", stdin);
	freopen("/home/lahiru/workstation/workspace/CodeJam/src/A-small.out", "wt", stdout);

	int t;
	cin >> t;
	For(test, 1, t) {
		
		int P,K,L;
		cin >> P >> K >> L;
		
		int64 keys[K][P];
		
		vector<vi> kk;
		
		Rep(i, K){
			vi vec;
			kk.push_back(vec);
		}
		
		int64 letters[L];
		
		Rep(i, L){
			cin >> letters[i];
		}
		
		sort(AllA(letters,L));
		
		int kx = 0;
		Rep(i, L){
			int64 l = letters[(L-i)-1];
			bool put = true;
			//int home = kx;
			do{
				int s = kk[kx].size();
				if( s < P){
					kk[kx].push_back(l);
					put = false;
				}
				kx++;
				if(kx>=K){
					kx=0;
				}
			}while(put);
		}
		
		int64 minpress = 0;
		
		Rep(i, K){
			Rep(ix, kk[i].size()){
				minpress += ( (kk[i][ix]) * (ix+1) );
			}
		}
		
		cout << "Case #" << test << ": " << minpress << endl;
	}

	exit(0);
}
