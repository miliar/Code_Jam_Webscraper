#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <climits>
#include <cfloat>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <numeric>
#include <complex>
#include <utility>
#include <memory>
#include <iomanip>
#include <algorithm>
#include <functional>
#include <sstream>
#include <assert.h>
using namespace std;

const double EPS = 1e-9;
const int INF = 100000000;
const int MOD = 1000000007;

typedef vector<int> vint;
typedef vector<vint> vvint;
typedef vector<string> vst;
typedef pair<int,int> pint;
typedef long long ll;

#define debug(x) cout<<#x<<" = "<<(x)<<" (L"<<__LINE__<<")"<<endl
template<class T1, class T2> ostream& operator<<(ostream &s, pair<T1,T2> P){return s<<'<'<<P.first<<", "<<P.second<<'>';}
template<class T> ostream& operator<<(ostream &s, vector<T> P) {s<<"{ ";for(int i=0;i<P.size();++i){if(i>0)s<<", ";s<<P[i];}return s<<" }"<<endl;}
template<class T> ostream& operator<<(ostream &s, vector<vector<T> > P) {for(int i=0;i<P.size();++i){s<<i<<" : "<<P[i];}return s;}

void test();

int T;
int A, B;
double p[200000];

int main() {
    //test();
    freopen( "/Users/macuser/Downloads/A-large.in", "r", stdin );
    freopen( "/Users/macuser/Documents/Programming/Contest/GCJ12 Round1A A large.txt", "w", stdout );
  
    scanf("%d", &T);
    
    for (int id = 1; id <= T; ++id) {
        scanf("%d%d", &A, &B);
        for (int i = 0; i < 200000; ++i) p[i] = 0.0;
        
        for (int i = 0; i < A; ++i) {
            double temp = 0.0;
            cin >> temp;
            p[i] = temp;
        }
        
        double dp[200000] = {0.0};
        double ichi = 1.0;
        for (int i = 0; i < A; ++i) {
            ichi *= p[i];
        }
        dp[0] += ichi * (B - A + 1);
        dp[0] += (1 - ichi) * (2 * B - A + 2);
        
        double all = (double)(B + 2);
        

        for (int i = 1; i <= A; ++i) {
            ichi = 1.0 - p[A-i];
            for (int j = 0; j < A-i; ++j) {
                ichi *= p[j];
            }
            dp[i] = dp[i-1] + 2 - ichi * (B + 1);
        }
        
        double res = all;
        for (int i = 0; i < A; ++i) {
            res = min(res, dp[i]);
        }
        
//        cout << endl;
//        for (int i = 0; i <= A; ++i) {
//            cout << i << " : ";
//            debug(dp[i]);
//        }
//        debug(all);
        
        printf("Case #%d: %f\n", id, res);
        
    }
    
    return 0;
}

struct LocalTest {
	void run_test() {		
		int correct = 0, total = 0;
		for (int i=0;i<=100; ++i) {
			int x = run_test_case(i);
			if (x == -1) {
				if (i >= 100) break;
				continue;
			}
			correct += x;
			++total;
		}
		
		if (total == 0) {
			cerr << "No test cases run." << endl;
		} else if (correct < total) {
			cerr << "Some cases FAILED (passed " << correct << " of " << total << ")." << endl;
		} else {
			cerr << "All " << total << " tests passed!" << endl;
		}
	}
	
	int verify_case(int casenum, const int &expected, const int &received, clock_t elapsed) {
		cerr << "Example " << casenum << "... "; 
		
		string verdict;
		vector<string> info;
		char buf[100];
		
		if (elapsed > CLOCKS_PER_SEC / 200) {
			sprintf(buf, "time %.2fs", elapsed * (1.0/CLOCKS_PER_SEC));
			info.push_back(buf);
		}
		
        if (expected == received) verdict = "PASSED";
        else verdict = "FAILED";
		
		cerr << verdict;
		if (!info.empty()) {
			cerr << " (";
			for (int i=0; i<(int)info.size(); ++i) {
				if (i > 0) cerr << ", ";
				cerr << info[i];
			}
			cerr << ")";
		}
		cerr << endl;		
    cerr << "    Expected: " << expected << endl; 
    cerr << "    Received: " << received << endl; 
		
		return verdict == "PASSED";
	}

	int run_test_case(int casenum__) {
		switch (casenum__) {
/*		case 0: {
			N = 5;
			int expected__ = 3;

			clock_t start__  = clock();
			int received__ = solve();
			return verify_case(casenum__, expected__, received__, clock()-start__);
		}
*/
/*
		case 1: {
			int N;
			int expected__;

			clock_t start__  = clock();
			int received__ = solve();
			return verify_case(casenum__, expected__, received__, clock()-start__);
		}
*/
		default:
			return -1;
		}
	}
} local_test;
 
void test() {
    local_test.run_test();
}
