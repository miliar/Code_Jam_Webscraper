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
        ifs.open("C-large.in");
        ofstream ofs;
        ofs.open("out.txt");
        int T;
        ifs >> T;
        for (int i = 1; i <= T; ++i) {
                int R, k, N;
                ifs >> R >> k >> N;
                vector<long long> g;
                for (int j = 0; j < N; ++j) {
                        long long m;
                        ifs >> m;
                        g.pb(m);
                }
                if (accumulate(all(g), 0LL) <= k) {
                        ofs << "Case #" << i << ": " << accumulate(all(g), 0LL) * R << endl;
                        continue;
                }
                vector<long long> a;
                vector<long long> b;
                int curr = 0;
                while (sz(a) < R) {
                        long long sum = 0;
                        for (int j = 0; j < N; ++j) {
                                if (sum + g[(curr + j)% N] <= k) {
                                        sum += g[(curr + j) % N];
                                }
                                else {
                                        a.pb(curr);
                                        b.pb(sum);
                                        curr = (curr + j) % N;
                                        break;
                                }
                        }
                        if (sz(a) == R || count(all(a), curr) == 1) {
                                break;
                        }
                }
                if (sz(a) == R) {
                        ofs << "Case #" << i << ": " << accumulate(all(b), 0LL) << endl;
                        continue;
                }
                long long sum = 0;
                int d = 0;
                for (int j = 0; j < sz(a); ++j) {
                        if (a[j] != curr) {
                                d++;
                        }
                        else {
                                break;
                        }
                }

                for (int j = 0; j < d; ++j) {
                        sum += b[j];
                }
                R -= d;
                long long d2 = 0;
                for (int j = d; j < sz(a); ++j) {
                        d2 += b[j];
                }
                
                sum += (R / (sz(a) - d)) * d2;
                for (int j = 0; j < (R % (sz(a) - d)); ++j) {
                        sum += b[j + d];
                }
                
                ofs << "Case #" << i << ": " << sum << endl;
        }
        
        
        return 0;
}
