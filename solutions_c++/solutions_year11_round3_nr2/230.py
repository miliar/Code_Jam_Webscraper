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
#include <cassert>
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

typedef long long ll;

int main() {
    ll testCount = read<ll>();
    for (ll ttt = 1; ttt <= testCount; ++ttt) {
        cout << "Case #" << ttt << ": ";
        ll L = read<ll>();
        ll T = read<ll>();
        ll N = read<ll>();
        ll C = read<ll>();
        vector<ll> X;
        for (ll i: R(C)) {
            X.push_back(read<ll>());
        }
        vector<ll> D;
        D.push_back(0);
        D.push_back(X[0]);
        for (ll i: R(1ll, C)) D.push_back(D[i] + X[i]);
        ll group = D.back();
        auto findPoll = [&](ll d) -> pair<ll, ll> {
           ll r = -1;
           for (ll i: R(C + 1)) {
               if (D[i] > d) {
                   r = i;
                   break;
               }
           }
           assert(r != -1);
           assert(r != 0);
           --r;
           return make_pair(r, D[r + 1] - d);
        };
        map<ll, ll> counts;
        ll total = (N / C) * group + D[(N % C)];
        ll t = total * 2;
        if (T >= t) {
            cout << t << endl;
            continue;
        }
        ll np = ((T / 2) / group) * C;
        auto tmp = findPoll((T / 2) % group);
        ++counts[tmp.second];
        np += tmp.first + 1;
        while ((np < N) && (np % C)) {
            ++counts[X[(np++) % C]];
        }
        if (np < N) {
            ll fullGroup = (N - np) / C;
            for (ll i: R(C)) {
                counts[X[i]] += fullGroup;
            }
            np += ((N - np) / C) * C;
        }
        while (np < N) {
            ++counts[X[(np++) % C]];
        }
        while (L && counts.size()) {
            auto it = counts.end();
            --it;
            ll decr = min(L, it->second);
            L -= decr;
            it->second -= decr;
            t -= it->first * decr;
            if (!it->second) {
                counts.erase(it);
            }
        }
        cout << t << endl;
    } 
    return 0;
}

