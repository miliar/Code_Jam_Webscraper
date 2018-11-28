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

template<class T1, class T2> ostream& operator<<(ostream &s, pair<T1,T2> P){return s<<'<'<<P.first<<", "<<P.second<<'>';}
template<class T> ostream& operator<<(ostream &s, vector<T> P) {s<<"{ ";for(int i=0;i<P.size();++i){if(i>0)s<<", ";s<<P[i];}return s<<" }"<<endl;}
template<class T> ostream& operator<<(ostream &s, vector<vector<T> > P) {for(int i=0;i<P.size();++i){s<<i<<" : "<<P[i];}return s;}
template<class T> bool exist(vector<T> P, T num) {for(int i=0;i<P.size();++i){if(P[i]==num)return true;}return false;}


vector<int> digit(int a, int n) {
    int i;
    vector<int> res;
    for (i = 1; i < 1000000; ++i) {
        if (a < n) {
            res.push_back(a);
            break;
        }
        else {
            res.push_back(a%n);
            a /= n;
        }
    }
    return res;
}

int count(vint n, vint b) {
    int res = 0;

    
    reverse(n.begin(), n.end());
    reverse(b.begin(), b.end());
    
    vint on = n;
    
    for (int i = 0; i < n.size()-1; ++i) {
        vint Q;
        for (int j = 0; j < n.size(); ++j) {
            Q.push_back(n[(j+1)%(int)n.size()]);
        }
        n = Q;
        //cout << n;
        if (on < n && n <= b) ++res;
    }
    
    return res;
}


int main() {    
    freopen( "/Users/macuser/Downloads/C-small-attempt0.in", "r", stdin );
	freopen( "/Users/macuser/Documents/Programming/Contest/GCJ12_Qual_C_small.txt", "w", stdout );
    
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; ++i) {
        int A,B;
        cin >> A >>B;
        
        int res = 0;
        for (int j = A; j < B; ++j) {
            //cout << endl << j << " : ";
            int temp = count(digit(j,10), digit(B,10));
            //cout << "total:" << temp << endl;
            res += temp;
        }
        printf("Case #%d: ", i+1);
        printf("%d\n", res);
    }
    
	return 0;
}














