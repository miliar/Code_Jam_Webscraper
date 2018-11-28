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
using namespace std;

//#define TEST
#define USE_FILE

#define pb(x) push_back(x)
#define FOR(i,a,b) for(int i = (a); i < (b); ++i) 

#define printval(x) cout << #x << " = " << (x) << endl;
#define printarray(x) \
	cout << #x << ": "; \
	for(int idx=0; idx<((x).size()); idx++) { cout << ((x)[idx]) << " "; } cout << endl;
#define printmatrix(x) \
	cout << #x << ": " << endl; \
	for(int idx=0; idx<((x).size()); idx++) { \
		for(int idx2=0; idx2<((x)[0].size()); idx2++) { cout << ((x)[idx][idx2]) << " "; } cout << endl; \
	} 

string szinput_s = "A-small-attempt0.in.txt";
string szinput_l = "A-large.in.txt";

string szoutput_s = "A-small.out.txt";
string szoutput_l = "A-large.out.txt";


class ClassName {
protected:

public:
	void Run() {
#ifdef USE_FILE
		//ifstream cin("sample.txt");
		//ifstream cin(szinput_s.c_str());
		//ofstream cout(szoutput_s.c_str());
		ifstream cin(szinput_l.c_str());
		ofstream cout(szoutput_l.c_str());

#endif
		int ncase;
		cin >> ncase;
		int P, K, L, temp;
		long long val;
		vector<int> F;
		FOR(i, 0, ncase) {
			F.clear();
			cin >> P >> K >> L;
			FOR(j, 0, L) {
				cin >> temp;
				F.pb(temp);
			}
			val = GetKeys(P, K, L, F);
			if(val == -1) {
				cout << "Case #" << i+1 << ": " << "Impossible" << endl;
			} else {
				cout << "Case #" << i+1 << ": " << val << endl;
			}
		}
	}

	long long GetKeys(int P, int K, int L, vector<int> F) {
		long long ret = 0;
		sort(F.begin(), F.end());
		reverse(F.begin(), F.end());

		long long k = 0;
		FOR(i, 0, F.size()) {
			if(i % K == 0) k += 1;
			if(k > P) return -1;
			ret += k*F[i];
			//printval(i);
			//printval(ret);
		}
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
