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
string szfile_input = "B-small-attempt0.in";
string szfile_output = "B-small-attempt0.out.txt";
//string szfile_input = "C-large-practice.in";
//string szfile_output = "C-large-practice.out.txt";


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

		long long N;
		string value;
		FOR(i, 0, ncase) {
			cin >> N;
			value = getNextNum(N);
			cout.precision(8);
			cout << "Case #" << i+1 << ": " << fixed << value << endl;
			printf("Case #%d: %s\n", value.c_str(), value);

		}
	}

	string getNextNum(long long N) {
		long long t = N;
		V.assign(20, 0);
		int c = 0;
		while(t>0) {
			V[c++] = t%10;
			t/=10;
		}
		reverse(V.begin(), V.end());

		printarray(V);
		next_permutation(V.begin(), V.end());
		printarray(V);

		string ret = "";
		RFOR(i, V.size()-1, -1) {
			ret.push_back(V[i]+'0');
		}
		reverse(ret.begin(), ret.end());
		while(ret[0] == '0')
			ret = ret.substr(1);
		printval(ret);
		return ret;	
	}

};

class ClassTest : public A_1 {
public:
	void Test() {
		printval(getNextNum(123));
		printval(getNextNum(223311));
		printval(getNextNum(11111));
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
