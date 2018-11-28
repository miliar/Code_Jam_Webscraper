#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
template<class T> string toString(T n) { ostringstream ost; ost << n; ost.flush(); return ost.str();}
LL toInt64(string s) {LL r = 0; istringstream sin(s); sin >> r; return r;}
int main()
{
        ifstream ifs;
        ifs.open("A-large.in");
        ofstream ofs;
        ofs.open("out.txt");
        int T;
        ifs >> T;
        for (int i = 1; i <= T; ++i) {
                int N, K;
                
                ifs >> N >> K;
                vector<int> a(N + 1);
                a[1] = 1;
                for (int j = 2; j <= N; ++j) {
                        a[j] = 2 * a[j - 1] + 1;
                }
                if (K % (a[N] + 1) == a[N]) {
                        ofs<< "Case #" << i << ": ON" << endl;
                }
                else {
                        ofs<< "Case #" << i << ": OFF" << endl;
                }
        }
        return 0;
}
