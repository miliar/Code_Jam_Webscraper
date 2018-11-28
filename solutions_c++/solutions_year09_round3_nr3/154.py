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
using namespace std;

//#define TEST
#define USE_FILE

#define pb(x) push_back(x)
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

//string szfile_input = "sample.txt";
//string szfile_output = "sample_output.txt";

//string szfile_input = "C-small-attempt0.in";
//string szfile_output = "C-small-attemp0.out.txt";

string szfile_input = "C-large.in";
string szfile_output = "C-large.out.txt";


class C_1 {
protected:
	vector<vector<int> > D;

public:
	void Run() {
#ifdef USE_FILE
		ifstream cin(szfile_input.c_str());
		ofstream cout(szfile_output.c_str());

#endif
		int ncase;
		cin >> ncase;

		int p, q;
		string szline;
		vector<int> Q;
		int val;
		FOR(i, 0, ncase) {
			Q.clear();
			cin >> p >> q;
			int tmp;
			FOR(j, 0, q) {
				cin >> tmp;
				Q.push_back(tmp);
			}
			val = getMinCost(p, Q);
			cout << "Case #" << i+1 << ": " << val << endl;
		}
	}

	int getMinCost(int p, vector<int> Q) {
		int ret;

		vector<int> R(p+1, -1);
		D.assign(p+1, R);

		ret = GO(1, p, Q);
		
		printval(ret);

		return ret;	
	}

	int GO(int st, int ed, vector<int> Q) {
		if(st >= ed) return 0;
		if(D[st][ed] != -1) return D[st][ed];
		
		int ret = 100000;
		FOR(i, 0, Q.size()) {
			int cost = 0;
			if(Q[i] >= st && Q[i] <= ed) {
				cost = Q[i]-st + ed-Q[i];
				cost += GO(st, Q[i]-1, Q) + GO(Q[i]+1, ed, Q);
				if(ret > cost) ret = cost;
			}
		}
		
		if(ret == 100000) ret = 0;
		D[st][ed] = ret;
		return ret;
	}


};

class TestClass : public C_1 {
public:
	void Test() {
	}
};

int main()
{
#ifdef TEST
	TestClass cnt;
	cnt.Test();
#else
	C_1 cn;
	cn.Run();
#endif
	return 0;
}
