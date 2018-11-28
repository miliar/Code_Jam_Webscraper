#include <stdio.h>
#include <time.h>
#include <vector>
#include <list>
#include <set>
#include <string>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <queue>
#include <map>
#include <iomanip>
#include <cmath>
#include <stack>
#include <numeric>
#include <iterator>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cfloat>
#include <utility>
#include <memory>
#include <functional>
#include <complex>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef vector<LL> VL;

#define FORE(it, c, T) for(T::iterator it = c.begin(); it != c.end(); it++)
#define FORI(i, n) for(int i = 0; i < (n); i++)
#define FORIS(i, s, n) for(int i = (s); i < (n); i++)
#define CLEAR(a) memset(a, 0, sizeof(a))
#define SORT(a) sort(a.begin(), a.end())
#define REVERSE(a) reverse(a.begin(), a.end())
#define PB(n) push_back(n)
#define SZ(a) int((a).size())
#define IPOW(a,b) ((long long) pow((double)(a),(double)(b)))
#define PI M_PI
#define EPS 1e-13
#define INF 0x7f7f7f7f

#define DEBUG 1
#define DBG(a) if (DEBUG) cout <<"DEBUG::: " <<a <<endl;
#define DBG2(a, b) if (DEBUG) cout <<"DEBUG::: " <<a <<"=" <<b <<endl;

int main() {
    int T;
    cin >>T;
    cin.ignore();

    for(int t=1; t<=T; t++) {

        int N;
        cin >>N;

        vector<int> x(N, 0);
        FORI(i, N-1) cin >>x[i];

        bool impossible = false;
        LL y_max = 999999995;
        vector<LL> y(N, 0);
        vector<int> st;
        FORI(i, N-1) {
            int i_view = x[i] - 1;
            int i_next_top = (SZ(st)>0) ? st.back() : -1;

            if (i == i_next_top) {
                st.pop_back();
                i_next_top = (SZ(st)>0) ? st.back() : -1;
            }
            else {
                y[i] = y[i-1] - 100000;
            }

            if (i_next_top < 0) {
                y[i]      = y_max;
                y[i_view] = y_max;
                st.PB(i_view);
            }
            else if (i_next_top < i_view) {
                impossible = true;
                break;
            }
            else if (i_next_top == i_view) {
            }
            else {
                double tmp = y[i] * (i_next_top - i_view)
                           + y[i_next_top] * (i_view - i);
                tmp /= (double)(i_next_top - i);
                y[i_view] = (int)tmp;
                y[i_view]++;
                st.PB(i_view);
            }
        }

        if (impossible) {
            cout <<"Case #" <<t <<": Impossible" <<endl;
        }
        else {
            // TEST CODE
//            FORI(i, N-1) {
//                int i_view = x[i] - 1;
//                FORIS(j, i+1, i_view) {
//                    if ((i_view - i) * (y[j] - y[i])
//                      >= ((j - i) * (y[i_view] - y[i]))) {
//                        cout <<"ERROR:::  i  j  i_view = " <<i <<" " <<j <<" " <<i_view <<endl;
//                        cout <<"ERROR::: yi yj yi_view = " <<y[i] <<" " <<y[j] <<" " <<y[i_view] <<endl;
//                    }
//                }
//                FORIS(j, i_view+1, N) {
//                    if ((i_view - i) * (y[j] - y[i])
//                      > ((j - i) * (y[i_view] - y[i]))) {
//                        cout <<"ERROR::: i j i_view = " <<i <<" " <<j <<" " <<i_view <<endl;
//                        cout <<"ERROR::: yi yj yi_view = " <<y[i] <<" " <<y[j] <<" " <<y[i_view] <<endl;
//                    }
//                }
//            }

            cout <<"Case #" <<t <<": ";
            FORI(i, N) cout <<" " <<y[i];
            cout <<endl;
        }
    }
    return 0;
}
