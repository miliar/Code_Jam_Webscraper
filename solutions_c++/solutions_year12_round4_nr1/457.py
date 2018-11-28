#include <iostream>
#include <vector>
#include <utility>
#include <set>
#include <iomanip>
#include <map>
#include <algorithm>
#include <limits>
#include <sstream>
#include <string>
#include <queue>
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

int abs(int a) {
    return a > 0 ? a : -a;
}

int main() {
    int testCount = read<int>();
    for (auto TEST: R(1, testCount + 1)) {
        int N = read<int>();
        vector<int> ds;
        vector<int> ls;
        for (int i: R(N)) {
            ds.push_back(read<int>());
            ls.push_back(read<int>());
        }
        int D = read<int>();
        vector<int> hs(N, -1);
        hs[0] = ds[0];
        queue<int> toUp;
        toUp.push(0);
        set<int> inQueue;
        inQueue.insert(0);
        while (!toUp.empty()) {
            int i = toUp.front();
            toUp.pop();
            inQueue.erase(i);
            for (int j: R(i + 1, N)) {
                if (ds[j] - ds[i] > hs[i]) break;
                int d = ds[j] - ds[i];
                int r;
                if (ls[j] >= d) {
                    r = d;
                } else {
                    r = ls[j];
                }
                if (r > hs[j]) {
                    hs[j] = r;
                    if (!inQueue.count(j)) {
                        inQueue.insert(j);
                        toUp.push(j);
                    }
                }
            }
            for (int j: R(i - 1, -1, -1)) {
                if (ds[i] - ds[j] > hs[i]) break;
                int d = ds[i] - ds[j];
                int r;
                if (ls[j] >= d) {
                    r = d;
                } else {
                    r = ls[j];
                }
                if (r > hs[j]) {
                    hs[j] = r;
                    if (!inQueue.count(j)) {
                        inQueue.insert(j);
                        toUp.push(j);
                    }
                }
            }
        }
        string ans = "NO";
        for (int i: R(N)) {
            if (hs[i] >= (D - ds[i])) {
                ans = "YES";
                break;
            }
        }
        cout << "Case #" << TEST << ": " << ans << endl;

    } 
    return 0;
}

