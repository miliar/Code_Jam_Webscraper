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

const double EPS = 1e-6;
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


int N;
int s[500];

vector<double> solve() {
    vector<double> res = vector<double>(N, 0.0);
    double X = 0;
    for (int i = 0; i < N; ++i) X += s[i];
//    for (int i = 0; i < N; ++i) {
////        int Min = INF;
////        for (int j = 0; j < N; ++j) if (j != i) Min = min(Min, s[j]);
//        double Min = X - s[i];
////        debug(X);
////        debug(Min);
//        int mem = 0;
//        
//        double a = (double)(X + Min - s[i] * (N-1)) / (N * X) * 100;
//        res.push_back(max(a,0.00000000));
//    }
    vector<pair<double, int> > S;
    for (int i = 0; i < N; ++i) S.push_back(make_pair((double)(s[i])/X,i));
    S.push_back(make_pair(100.0, N+1));
    sort(S.begin(), S.end());
    
    //cout << S;
    double amari = 1.0;
    
    while (amari > EPS) {
        int i = 0;
        while (abs(S[i+1].first - S[i].first) < EPS) ++i;
        double sa = S[i+1].first - S[i].first;
//                    debug(S);
//        debug(amari);
        for (int j = 0; j <= i; ++j) {
            S[j].first += min(sa, amari/(i+1));
            res[S[j].second] += min(sa*100, amari/(i+1)*100);
        }
                
        amari -= min(sa * (i+1), amari);
    }
        
    return res;
        
}

int main() {
    test();
    freopen( "/Users/macuser/Downloads/A-large.in", "r", stdin );
    freopen( "/Users/macuser/Downloads/AL.txt", "w", stdout );
    
    int T;
    scanf("%d", &T);
    for (int id = 1; id <= T; ++id) {
        memset(s, 0, sizeof(s));
        cin >> N;
        for (int i = 0; i < N; ++i) {
            int temp;
            cin >> temp;
            s[i] = temp;
        }
        
        printf("Case #%d:", id);
        vector<double> res = solve();
        for (int i = 0; i < res.size(); ++i) printf(" %8.6f", res[i]);
        printf("\n");
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
	
	int verify_case(int casenum, const vector<double> &expected, const vector<double> &received, clock_t elapsed) {
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
		case 0: {
			N = 2;
			int s_temp[] = {20,10};
			for (int AA = 0; AA < (int)(sizeof s_temp / sizeof s_temp[0]); ++AA) s[AA] = s_temp[AA];
			double expected__[] = {33.333333, 66.666667};

			clock_t start__  = clock();
			vector<double> received__ = solve();
			return verify_case(casenum__, vector<double>(expected__, expected__ + (sizeof expected__ / sizeof expected__[0])), received__, clock()-start__);
		}
		case 1: {
			N = 2;
			int s_temp[] = {10, 0};
			for (int AA = 0; AA < (int)(sizeof s_temp / sizeof s_temp[0]); ++AA) s[AA] = s_temp[AA];
			double expected__[] = {0, 100};

			clock_t start__  = clock();
			vector<double> received__ = solve();
			return verify_case(casenum__, vector<double>(expected__, expected__ + (sizeof expected__ / sizeof expected__[0])), received__, clock()-start__);
		}
		case 2: {
			N = 4;
			int s_temp[] = {25,25,25,25};
			for (int AA = 0; AA < (int)(sizeof s_temp / sizeof s_temp[0]); ++AA) s[AA] = s_temp[AA];
			double expected__[] = {25,25,25,25};

			clock_t start__  = clock();
			vector<double> received__ = solve();
			return verify_case(casenum__, vector<double>(expected__, expected__ + (sizeof expected__ / sizeof expected__[0])), received__, clock()-start__);
		}
		case 3: {
			N = 3;
			int s_temp[] = {24,30,21};
			for (int AA = 0; AA < (int)(sizeof s_temp / sizeof s_temp[0]); ++AA) s[AA] = s_temp[AA];
			double expected__[] = {34.666667, 26.666667, 38.666667};

			clock_t start__  = clock();
			vector<double> received__ = solve();
			return verify_case(casenum__, vector<double>(expected__, expected__ + (sizeof expected__ / sizeof expected__[0])), received__, clock()-start__);
		}
		case 4: {
			N = 9;
			int s_temp[] = {56, 57, 56, 1, 56, 1, 1, 1, 1};
			for (int AA = 0; AA < (int)(sizeof s_temp / sizeof s_temp[0]); ++AA) s[AA] = s_temp[AA];
			double expected__[] = {0};

			clock_t start__  = clock();
			vector<double> received__ = solve();
			return verify_case(casenum__, vector<double>(expected__, expected__ + (sizeof expected__ / sizeof expected__[0])), received__, clock()-start__);
		}
		default:
			return -1;
		}
	}
} local_test;
 
void test() {
    local_test.run_test();
}
