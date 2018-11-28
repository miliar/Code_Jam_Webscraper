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
//string szfile_input = "A-small-attempt0 (1).in";
//string szfile_output = "A-small-attempt0.out.txt";
string szfile_input = "A-large (1).in";
string szfile_output = "A-large.out.txt";


class A_1 {
protected:
	vector<int> V;

public:
	void Run() {
#ifdef USE_FILE
		ifstream cin(szfile_input.c_str());
		ofstream cout(szfile_output.c_str());

#endif
		int ncase;
		cin >> ncase;

		string N;
		long long value;
		FOR(i, 0, ncase) {
			cin >> N;
			value = getNum(N);
			cout << "Case #" << i+1 << ": " << value << endl;
			printf("Case #%d: %ld\n", i+1, value);
		}
	}

	long long getNum(string N) {
		long long ret = 0;

		map<char, int> M;
		M[N[0]] = 1;
		FOR(i, 1, N.size()) {
			if(M.find(N[i]) == M.end()) {
				M[N[i]] = 0;
				break;
			}
		}		
		int c = 2;
		FOR(i, 2, N.size()) {
			if(M.find(N[i]) == M.end()) {
				M[N[i]] = c;
				c++;
			}
		}
		c = max(c, 2);
		printval(c);
		FOR(i, 0, N.size()) {
			ret += M[N[i]];
			if(i != N.size()-1) ret *= c;
			assert(ret < (1LL<<62));
		}

		return ret;	

	}


};

class ClassTest : public A_1 {
public:
	void Test() {
		printval(getNum("11111"));
	}
};

int main()
{
#ifdef TEST
	ClassTest cnt;
	cnt.Test();
#else
	A_1 cn;
	cn.Run();
#endif
	return 0;
}
