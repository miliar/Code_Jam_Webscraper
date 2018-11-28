// Powered by FTH

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <iterator>
#include <functional>
#include <utility>
#include <numeric>
#include <complex>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <cassert>
#include <cstring>
using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define FOR(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define ALLOF(c) ((c).begin()), ((c).end())

#define MOD 10009

struct histgram_t {
    long long freq[4];
    histgram_t() {
        memset(freq, 0, sizeof(freq));
    }
    histgram_t(const histgram_t& a, const histgram_t& b) {
        REP(i, 4)
            freq[i] = a.freq[i] + b.freq[i];
    }
};
bool operator<(const histgram_t& a, const histgram_t& b) {
    REP(i, 4)
        if (a.freq[i] != b.freq[i])
            return (a.freq[i] < b.freq[i]);
    return false;
}

void go(const map<histgram_t, long long>& cur, map<histgram_t, long long>& next, const vector<histgram_t>& dic_term) {
    int n = dic_term.size();
    FOR(it, cur) {
        const histgram_t& cur_hist = it->first;
        long long cur_freq = it->second;
        REP(i, n) {
            histgram_t next_hist(cur_hist, dic_term[i]);
            next[next_hist] += cur_freq;
        }
    }
}

void solve(const vector<string>& terms, int nWords, const vector<string>& dic) {
    int n = dic.size();
    int nTerms = terms.size();
    vector<long long> res(nWords+1, 0);

    REP(iTerm, nTerms) {
        string term = terms[iTerm];
        int nVars = term.size();

        vector<histgram_t> dic_term(n);
        REP(iDic, n) {
            const string& dicword = dic[iDic];
            REP(i, nVars) REP(j, dicword.size())
                if (term[i] == dicword[j])
                    dic_term[iDic].freq[i]++;
        }
        map<histgram_t, long long> cur;
        cur[histgram_t()] = 1;
        REP(d, nWords) {
            {
                map<histgram_t, long long> next;
                go(cur, next, dic_term);
                cur.swap(next);
            }
            FOR(it, cur) {
                long long lo = it->second % MOD;
                REP(i, nVars)
                    lo = (lo * it->first.freq[i]) % MOD;
                res[d+1] = (res[d+1] + lo) % MOD;
            }
        }
    }
    REP(d, nWords)
        cout << " " << res[d+1];
    cout << endl;
}

int main() {

    int nCases;
    {
        string s;
        getline(cin, s);
        istringstream is(s);
        is >> nCases;
    }

    REP(iCase, nCases) {
        vector<string> terms;
        int nWords;
        for(;;) {
            char buf[256];
            scanf(" %[^+ \n]", buf);
            scanf("+");
            clearerr(stdin);
            string s(buf);
            if (isdigit(s[0])) {
                istringstream is(s);
                is >> nWords;
                break;
            }
            //cerr << s << endl;
            terms.push_back(s);
        }
        int n;
        cin >> n;
        vector<string> dic(n);
        REP(i, n)
            cin >> dic[i];
        cout << "Case #" << iCase+1 << ":";
        solve(terms, nWords, dic);
        /*
        REP(i, terms.size())
            cout << terms[i] << "+";
        cout << "(" << nWords << ")" << endl;
        cout << dic.size() << endl;
        REP(i, dic.size())
            cout << i << ": " << dic[i] << endl;
        cout << endl;
        */
    }

    return 0;
}
