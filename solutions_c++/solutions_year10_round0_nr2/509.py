#include <stack>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <boost/assert.hpp>
#include <boost/foreach.hpp>
#include <boost/lexical_cast.hpp>
using namespace std;
using namespace boost;

class Big {
    static const unsigned UNIT = 6;
    static const unsigned RANGE = 1000000;
    static const unsigned SIZE = 10;
    unsigned data[SIZE];
public:
    Big () {}
    Big (const string &s) {
        
    }

    friend bool operator < (const Big &big1, const Big &big2) {
        for (int i = SIZE - 1; i >= 0; --i) {
            if (big1.data[i] < big2.data[i]) return true;
            if (big1.data[i] > big2.data[i]) return false;
        }
        return false;
    }

    friend bool operator == (const Big &big1, const Big &big2) {
        for (int i = 0; i < SIZE; ++i) {
            if (big1.data[i] != big2.data[i]) return false;
        }
        return true;
    }

    Big operator -= (const Big &big) {
        unsigned borrow = 0;
        for (int i = 0; i < SIZE; ++i) {
            unsigned sub = big.data[i] + borrow;
            borrow = 0;
            if (data[i] < sub) {
                data[i] += RANGE;
                borrow = 1;
            }
            data[i] -= sub;
        }
    }

    void x10 () {
        unsigned left = 0;
        for (int i = 0; i < SIZE; ++i) {
            data[i] *= 10;
            data[i] += left;
            left = data[i] / RANGE;
            data[i] = data[i] % RANGE;
        }
    }

    Big operator %= (Big big) {
        stack<Big> sub;
        while (! (*this < big)) {
            sub.push(big);
            big.x10();
        }
        while (!sub.empty()) {
            big = sub.top();
            sub.pop();
            while (!(*this < big)) {
                (*this) -= big;
            }
        }
    }

    friend istream & operator >> (istream &is, Big &big) {
        string str;
        is >> str;
        fill(big.data, big.data + Big::SIZE, 0);
        if (is) {
            unsigned i = 0;
            unsigned off = str.length();
            while (off > 0) {
                unsigned len = min(off, unsigned(Big::UNIT));
                off -= len;
                big.data[i] = lexical_cast<unsigned>(str.substr(off, len));
                ++i;
            }
        }
        return is;
    }

    friend ostream & operator << (ostream &os, const Big &big) {
        int i = Big::SIZE - 1;
        while ((big.data[i] == 0) && (i > 0)) --i;
        os << big.data[i];
        --i;
        while (i >= 0) {
            os << setw(Big::UNIT) << setfill('0') << right << big.data[i--];
        }
        return os;
    }

    friend Big operator - (const Big &b1, const Big &b2) {
        Big ret = b1;
        ret -= b2;
        return ret;
    }

    friend Big operator % (const Big &b1, const Big &b2) {
        Big ret = b1;
        ret %= b2;
        return ret;
    }

    bool zero () const {
        for (unsigned i = 0; i < SIZE; ++i) {
            if (data[i]) return false;
        }
        return true;
    }
};

int main () {
    unsigned N;
    cin >> N;
    for (unsigned i = 0; i < N; ++i) {
        unsigned M;
        cin >> M;

        vector<Big> list;
        for (unsigned j = 0; j < M; ++j) {
            Big b;
            cin >> b;
            list.push_back(b);
        }

        sort(list.begin(), list.end());
        list.resize(unique(list.begin(), list.end()) - list.begin());
        M = list.size();
#if  1
        cerr << "SORTED:" << endl;
        BOOST_FOREACH(const Big &b, list) {
            cerr << b << endl;
        }
#endif

        Big small = list.front();

        {
            vector<Big> diff(M-1);
            for (unsigned j = 0; j < M-1; ++j) {
                diff[j] = list[j+1] - list[j];
            }
            swap(diff, list);
            sort(list.begin(), list.end());
        }

        for(;;) {
#if 1
        cerr << "DIFF:" << endl;
        BOOST_FOREACH(const Big &b, list) {
            cerr << b << endl;
        }
#endif
            bool run = false;
            for (unsigned j = 1; j < list.size(); ++j) {
                list[j] %= list[0];
                if (!list[j].zero()) run = true;
                ++j;
            }
            if (!run) break;
            sort(list.begin(), list.end());
        }
        small %= list[0];
        if (small.zero()) small = list[0];
        list[0] -= small;
        cout << "Case #" << (i+1) << ": " << list[0] << endl;
    }
    return 0;
}
