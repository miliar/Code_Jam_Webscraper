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

int try_fill(int W, int L, const vector<pair<int, int>>& rs, vector<pair<int, int>>& res) {
    res.resize(rs.size());
    int i = 0; 
    int prevMax = -1;
    while (i != rs.size()) {
        int curMax = -1;
        int l = -rs[i].first;
        while (i != rs.size()) {
            int r = rs[i].first;
            if (l + r > L) break;
            if (prevMax < 0) {
                curMax = max(curMax, r);
                res[rs[i].second] = make_pair(0, l + r);
            } else if (prevMax + r > W) {
                return i;
            } else {
                curMax = max(prevMax + 2 * r, curMax);
                res[rs[i].second] = make_pair(prevMax + r, l + r);
            }
            l += 2 * r;
            ++i;
        }
        prevMax = curMax;
    }
    return i;
}

int main() {
    int testCount = read<int>();
    for (auto TEST: R(1, testCount + 1)) {
        int N, W, L;
        cin >> N >> W >> L;
        vector<pair<int, int>> rs;
        for (int i: R(N)) {
            rs.push_back(make_pair(read<int>(), i));
        }
        sort(rs.rbegin(), rs.rend());
        vector<pair<int, int>> res;
        while (1) {
            if (try_fill(W, L, rs, res) == N) {
                break;
            }
            if (try_fill(L, W, rs, res) == N) {
                for (auto& p: res) {
                    swap(p.first, p.second);
                }
                break;
            }
            random_shuffle(rs.begin(), rs.end());
        }
        cout << "Case #" << TEST << ":";
        for (int i: R(N)) {
            cout << " " << res[i].first << " " << res[i].second;
        }
        cout << endl;
    } 
    return 0;
}

