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
// G++
template<class T1, class T2> ostream& operator<<(ostream &s, map<T1,T2> P) {
    s << "{ ";
	for(typeof(P.begin()) it = P.begin(); it != P.end(); ++it) {
        if (it != P.begin()) s << ", ";
        s << '<' << it->first << "->" << it->second << '>';
    }
	return s<< " }" << endl;
}

void test();

int N;
long long S[1000];

int solve() {
}

int main() {
    //test();
    freopen( "/Users/macuser/Downloads/C-small-attempt0.in", "r", stdin );
    freopen( "/Users/macuser/Downloads/C.txt", "w", stdout );
    
    int T;
    scanf("%d", &T);
    for (int id = 1; id <= T; ++id) {
        memset(S, 0, sizeof(S));
        cin >> N;
        for (int i = 0; i < N; ++i) {
            long long temp;
            cin >> temp;
            S[i] = temp;
        }
                printf("Case #%d: \n", id);
        
        //sort(S, S+N);
        map<long long, vint> M;
        bool ok = false;
        for (int i = 0; i < 1<<N; ++i) {
            long long temp = 0LL;
            vector<int> tv;
            for (int j = 0; j < N; ++j) {
                if (i & (1<<j)) {
                    temp = temp + S[j];
                    tv.push_back(S[j]);
                }
            }
            //cout << M;
            if (M[temp].size() != 0) {
                ok = true;
                for (int j = 0; j < M[temp].size(); ++j) cout << M[temp][j] << ' ';
                            cout << '\n';
                for (int j = 0; j < tv.size(); ++j) cout << tv[j] << ' ';
                            cout << '\n';
                break;
            }
            M[temp] = tv;
            
        }
        
        if (!ok) {
        printf("Impossible");
        printf("\n");
        }

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
