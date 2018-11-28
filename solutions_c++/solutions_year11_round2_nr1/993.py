#include <iostream>
#include <vector>
#include <utility>
#include <set>
#include <map>
#include <algorithm>
#include <limits>
#include <sstream>
#include <string>
#include <numeric>
#include <iterator>
#include <iomanip>
using namespace std;

#define PRINT(E)\
do {\
    cerr << #E ": " << (E) << endl;\
}\
while(0)

#define PRINTR(E)\
do {\
    cerr << #E ": [";\
    for (const auto& i: (E)) cerr << i << " ";\
    cerr << "]" << endl;\
}\
while(0)

template <class T, class D>
class Range {
    class It {
    public:
        It(const T& v,
           const T& e,
           const D& s)
        : v_(v),
          e_(e),
          s_(s),
          end_(false)
        {
            checkEnd();
        };

        T operator*() {
            return v_;
        }

        It& operator++() {
            if (!end_) {
                v_ += s_;
                checkEnd();
            }
            return *this;
        }

        It operator++(int) {
            It r = *this;
            ++r;
            return r;
        }

        bool operator!=(const It& o) const {
            return (end_ && !o.end_) || (!end_ && o.end_) 
                   || (!end_ && (v_ != o.v_));
        }
    private:
        void checkEnd() {
            bool pos = (s_ > static_cast<D>(0));
            bool eq = v_ == e_;
            bool more = v_ > e_;
            end_ = eq || (more && pos) || (!more && !pos);
        }
        T v_;
        T e_;
        D s_;
        bool end_;
    };
public:
    Range(const T& b, const T& e, const D& s): b_(b), e_(e), s_(s) {};
    It begin() const { return It{b_, e_, s_}; }
    It end() const { return It{e_, e_, s_}; }
private:
    T b_;
    T e_;
    D s_;
};

template <typename T>
Range<T, T> R(const T& e) {
    return Range<T, T>{static_cast<T>(0), e, static_cast<T>(1)};
}

template <typename T>
Range<T, T> R(const T& b, const T& e) {
    return Range<T, T>{b, e, static_cast<T>(1)};
}

template <typename T, typename D>
Range<T, D> R(const T& b, const T& e, const D& d) {
    return Range<T, D>{b, e, d};
}

template <class T>
T read() {
    T r;
    cin >> r;
    return r;
}


int main() {
    int testCount = read<int>();
    for (int t = 1; t <= testCount; ++t) {
        int N = read<int>();
        vector<vector<int>> table(N, vector<int>(N, 0));
        vector<double> WP(N, 0);
        vector<double> OWP(N, 0);
        vector<double> OOWP(N, 0);
        vector<double> RA(N, 0);
        vector<int> G(N, 0);
        for (int i: R(N)) {
            string s = read<string>();
            for (int j: R(N)) {
                char c = s[j];
                if (c == '1') table[i][j] = 1;
                else if (c == '0') table[i][j] = 0;
                else table[i][j] = -1;
            }
        }
            for (int i: R(N)) {
                for (int j: R(N)) {
                    if (table[i][j] != -1) {
                        ++G[i];
                        WP[i] += table[i][j];
                    }
                }
                WP[i] /= G[i];
            }
            for (int i: R(N)) {
                for (int j: R(N)) {
                    if (table[i][j] != -1) {
                        OWP[i] += (WP[j] * G[j] - double(table[j][i])) / (G[j] - 1);
                    }
                }
                OWP[i] /= G[i];
            }
            for (int i: R(N)) {
                for (int j: R(N)) {
                    if (table[i][j] != -1) {
                        OOWP[i] += OWP[j];
                    }
                }
                OOWP[i] /= G[i];
            }
            for (int i: R(N)) {
                RA[i] = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i];
            }
        
        cout << "Case #" << t << ": " << endl;
        for (int i: R(N)) {
            cout << fixed << setprecision(10) << RA[i] << endl;
        }
    } 
    return 0;
}

