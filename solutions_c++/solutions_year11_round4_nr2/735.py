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
    typedef decltype(e - e) D;
    return Range<T, T>{static_cast<T>(0), e, static_cast<D>(1)};
}

template <typename T>
Range<T, T> R(const T& b, const T& e) {
    typedef decltype(e - b) D;
    return Range<T, T>{b, e, static_cast<D>(1)};
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


typedef long long LL;

int main() {
    int testCount = read<int>();
    LL NAAAN = -1;
    for (auto TEST: R(1, testCount + 1)) {
        auto RR = read<LL>();
        auto CC = read<LL>();
        auto D = read<LL>();
        vector<vector<LL>> G(RR, vector<LL>(CC, D));
        for (int i: R(RR)) {
            auto s = read<string>();
            for (int j: R(CC)) {
                G[i][j] += (s[j] - '0');
            }
        }
        vector<vector<vector<LL>>> CI(min(RR, CC) + 1, vector<vector<LL>>(RR, vector<LL>(CC, NAAAN)));
        vector<vector<vector<LL>>> CJ(min(RR, CC) + 1, vector<vector<LL>>(RR, vector<LL>(CC, NAAAN)));
        vector<vector<vector<LL>>> MM(min(RR, CC) + 1, vector<vector<LL>>(RR, vector<LL>(CC, NAAAN)));
        for (int i: R(RR)) {
            for (int j: R(CC)) {
                int sFrom = 3;
                int sTo = min(RR - i, CC - j);
                if (sTo < 3) {
                    continue;
                }
                CI[sFrom][i][j] = 0;
                CJ[sFrom][i][j] = 0;
                MM[sFrom][i][j] = 0;
                for (int ii: R(i, i + 3))
                    for (int jj: R(j, j + 3)) {
                        CI[sFrom][i][j] += ii * G[ii][jj]; 
                        CJ[sFrom][i][j] += jj * G[ii][jj]; 
                        MM[sFrom][i][j] += G[ii][jj];
                    }

                for (int s: R(sFrom + 1, sTo + 1)) {
                    CI[s][i][j] = CI[s - 1][i][j];
                    CJ[s][i][j] = CJ[s - 1][i][j];
                    MM[s][i][j] = MM[s - 1][i][j];
                    for (int ii: R(i, i + s - 1)) {
                        int jj = j + s - 1;
                        CI[s][i][j] += ii * G[ii][jj]; 
                        CJ[s][i][j] += jj * G[ii][jj]; 
                        MM[s][i][j] += G[ii][jj];
                    }
                    for (int jj: R(j, j + s - 1)) {
                        int ii = i + s - 1;
                        CI[s][i][j] += ii * G[ii][jj]; 
                        CJ[s][i][j] += jj * G[ii][jj]; 
                        MM[s][i][j] += G[ii][jj];
                    }
                        int jj = j + s - 1;
                        int ii = i + s - 1;
                        CI[s][i][j] += ii * G[ii][jj]; 
                        CJ[s][i][j] += jj * G[ii][jj]; 
                        MM[s][i][j] += G[ii][jj];
                } 
            }
        }
        int res = -1;
        for (int s: R(min(RR, CC) + 1)) { 
            for (int i: R(RR)) {
                for (int j: R(CC)) {
                    if (CI[s][i][j] == NAAAN) continue;
                    int ic = -1 + s + 2 * i;
                    int jc = -1 + s + 2 * j;
                    int ii;
                    int jj;
                    ii = i;
                    jj = j;
                        CI[s][i][j] -= ii * G[ii][jj]; 
                        CJ[s][i][j] -= jj * G[ii][jj]; 
                        MM[s][i][j] -= G[ii][jj];
                    ii = i + s - 1;
                        CI[s][i][j] -= ii * G[ii][jj]; 
                        CJ[s][i][j] -= jj * G[ii][jj]; 
                        MM[s][i][j] -= G[ii][jj];
                    jj = j + s - 1;
                        CI[s][i][j] -= ii * G[ii][jj]; 
                        CJ[s][i][j] -= jj * G[ii][jj]; 
                        MM[s][i][j] -= G[ii][jj];
                    ii = i;
                        CI[s][i][j] -= ii * G[ii][jj]; 
                        CJ[s][i][j] -= jj * G[ii][jj]; 
                        MM[s][i][j] -= G[ii][jj];
                    CI[s][i][j] *= 2;
                    CJ[s][i][j] *= 2;
                    if (CI[s][i][j] % MM[s][i][j]
                        || CJ[s][i][j] % MM[s][i][j]
                        || (CI[s][i][j] / MM[s][i][j] != ic)
                        || (CJ[s][i][j] / MM[s][i][j] != jc))
                    {
                        continue;
                    } else {
                        res = s;
                    }
                }
            }
        }

end:
        cout << "Case #" << TEST << ": ";
        if (res != -1) {
            cout << res;
        } else {
cout << "IMPOSSIBLE";
        }
        cout << endl;
            
    } 
    return 0;
}

