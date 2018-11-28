#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <cassert>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <iomanip>
#include <cmath>
#include <functional>
#include <complex>
using namespace std;

//#define TEST
#define USE_FILE

//string szfile_input = "sample.txt";
//string szfile_output = "sample.out.txt";
//string szfile_input = "A-small-attempt0.in";
//string szfile_output = "A-small.out.txt";
string szfile_input = "A-large.in";
string szfile_output = "A-large.out.txt";

#define pb(x) push_back((x))
#define mp(a, b) make_pair((a), (b))
#define FOR(i,a,b) for(int i = (a); i < (b); ++i) 
#define RFOR(i,a,b) for(int i = (a); i > (b); --i) 

#define printval(x) cout << #x << " = " << (x) << endl;
#define printarray(x) \
	cout << #x << ": "; \
	for(int idx=0; idx<((x).size()); idx++) { cout << ((x)[idx]) << " "; } cout << endl;
#define printmatrix(x) \
	cout << #x << ": " << endl; \
	for(int idx=0; idx<((x).size()); idx++) { \
	for(int idx2=0; idx2<((x)[0].size()); idx2++) { cout << ((x)[idx][idx2]) << " "; } cout << endl; \
	} 
#define printbit(x, n) \
	cout << #x << ": "; \
	for(int idx = (n)-1; idx >= 0; idx-=1) { cout << (((x) & (1<<idx)) != 0); } cout << endl;

typedef long long LL;
typedef pair<int, int> pii;

#define biton(a, nth) (((a) & (1LL<<(nth))) != 0)


char D[50][50];
int N;

class ClassName {
protected:

public:
	void Run() {
#ifdef USE_FILE
		ifstream cin(szfile_input.c_str());
		ofstream cout(szfile_output.c_str());

#endif
		int ncase;
		cin >> ncase;

		int value;
		int n;
		FOR(i, 0, ncase) {
			cin >> n;
			memset(D, 0, sizeof(D));
			FOR(j, 0, n) {
				FOR(k, 0, n) {
					cin >> D[j][k];
				}
			}
			value = getMinSwap(n);

		//	cout.precision(8);
			cout << "Case #" << i+1 << ": " << fixed << value << endl;
			printf("Case #%d: %ld\n", i+1, value);

		}
	}

	int getMinSwap(int n) {
		N = n;
		vector<int> V(N, 0);

		FOR(i, 0, N) {
			int cnt = 0;
			FOR(j, 0, N) {
				if(D[i][j] == '1') cnt = j;
			}
			V[i] = cnt;
		}

		int ret = go(V, 0);

		return ret;
	}

	int go(vector<int> V, int level) {
		if(level == N-1) return 0;

		int ret = 0;
		if(V[level] > level) {
			FOR(i, level+1, N) {
				if(V[i] <= level) {
					for(int j = i; j > level; j--) {
						swap(V[j], V[j-1]);
						ret++;
					}
					break;
				}
			}
		} 
		//printarray(V);
		ret += go(V, level+1);
	
		return ret;
	}

};

class ClassNameTest : public ClassName {
public:
	void Test() {
	}
};

int main()
{
#ifdef TEST
	ClassNameTest cnt;
	cnt.Test();
#else
	ClassName cn;
	cn.Run();
#endif
	return 0;
}