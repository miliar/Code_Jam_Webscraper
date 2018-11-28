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
        int r = read<int>();
        int c = read<int>();
        vector<vector<char>> f(r, vector<char>(c));
        for (int i: R(r)) {
            auto s = read<string>();
            for (int j: R(c)) {
                f[i][j] = s[j];
            } 
        }
        auto isMatch = [=](int i, int j) {return (i >= 0) && (i < r)
                                                 && (j >= 0) && (j < c);};
        auto isBlue = [&](int i, int j) {return isMatch(i, j) && f[i][j] == '#';};
        auto findCorner = [&]() -> pair<int, int> {
            for (int i: R(r))
                for (int j: R(c))
                   if (isBlue(i, j) 
                       && !isBlue(i - 1, j)
                       && !isBlue(i, j - 1))
                       return make_pair(i, j);
            return make_pair(-1, -1);
        };
        bool pos = true;
        pair<int, int> p;
        while ((p = findCorner()).first != -1) {
            int x = p.first;
            int y = p.second;
            if (isBlue(x + 1, y) && isBlue(x, y + 1) && isBlue(x + 1, y + 1)) {
                f[x][y] = f[x + 1][y + 1] = '/';
                f[x + 1][y] = f[x][y + 1] = '\\';
            } else {
                pos = false;
                break;
            }
        } 
        cout << "Case #" << t << ":" << endl;
        if (pos) {
            for (int i: R(r)) {
                for (int j: R(c)) {
                    cout << f[i][j];
                }
                cout << endl;
            }
        } else {
            cout << "Impossible" << endl;
        }
        
    } 
    return 0;
}

