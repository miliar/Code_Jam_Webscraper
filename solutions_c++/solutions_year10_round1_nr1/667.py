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
void rotate(VS &a) {
        int n = sz(a);
        for (int i = 0; i < n; ++i) {
                if (count(all(a[i]), '.') == n) {
                        continue;
                }
                string s;
                for (int j = 0; j < n; ++j) {
                        if (a[i][j] != '.') {
                                s += a[i][j];
                        }
                }
                int k = sz(s);
                
                a[i] = string(n - k, '.') + s;
        }
        
        VS b(n);
        for (int i = 0; i < n; ++i) {
                for (int j = n - 1; j >= 0; --j) {
                        b[i] += a[j][i];
                }
        }

        a = b;
}

bool valid(VS &a, char c, int K) {
        int n = sz(a);
        for (int i = 0; i < n; ++i) {
                for (int j = 0; j <= n - K; ++j) {
                        bool find = true;
                        for (int k = 0; k < K; ++k) {
                                if (a[i][j + k] != c) {
                                        find = false;
                                        break;
                                }
                        }
                        if (find) {
                                return true;
                        }
                }
        }
        for (int i = 0; i < n; ++i) {
                for (int j = 0; j <= n - K; ++j) {
                        bool find = true;
                        for (int k = 0; k < K; ++k) {
                                if (a[j + k][i] != c) {
                                        find = false;
                                        break;
                                }
                        }
                        if (find) {
                                return true;
                        }
                }
        }
        for (int i = 0; i <= n - K; ++i) {
                for (int j = 0; j <= n - K; ++j) {
                        bool find = true;
                        for (int k = 0; k < K; ++k) {
                                if (a[i + k][j + k] != c) {
                                        find = false;
                                        break;
                                }
                        }
                        if (find) {
                                return true;
                        }
                }
                
        }
        for (int i = n - 1; i >= K - 1; --i) {
                for (int j = 0; j <= n - K; ++j) {
                        bool find = true;
                        for (int k = 0; k < K; ++k) {
                                if (a[i - k][j + k] != c) {
                                        find = false;
                                        break;
                                }
                        }
                        if (find) {
                                return true;
                        }
                }
        }
        
        return false;
}

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
                VS a(N);
                for (int j = 0; j < N; ++j) {
                        ifs >> a[j];
                }
                rotate(a);
                bool red = valid(a, 'R', K);
                bool blue = valid(a, 'B', K);

                if (red && blue) {
                        ofs << "Case #" << i << ": Both" << endl;
                }
                else if (red) {
                        ofs << "Case #" << i << ": Red" << endl;
                }
                else if (blue) {
                        ofs << "Case #" << i << ": Blue" << endl;
                }
                else {
                        ofs << "Case #" << i << ": Neither" << endl;
                }
        }
        return 0;
}
