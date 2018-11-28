#include <algorithm>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <stack>
#include <sstream>
#include <string>
#include <vector>
#include <queue>

using namespace std;
fstream inp, out;
const int oo = 1000000;

struct State
{
    int a[4];
    State ()
    {
        for (int i = 0; i < 4; ++i) a[i] = 0;
    }
    bool operator < (const State &s) const
    {
        for (int i = 0; i < 4; ++i) if (a[i] != s.a[i]) return a[i] < s.a[i];
        return false;
    }
    void add(const State &s)
    {
        for (int i = 0; i < 4; ++i) a[i] += s.a[i];
    }
};

const int MOD = 10009;
inline int mod(int a) 
{
    if (a < MOD) return a;
    return a-MOD;
}

int calc(map<State, int> &d, int *cnt)
{
    int res = 0;
    for (map<State, int>::iterator it = d.begin(); it != d.end(); ++it)
    {
        State s = it->first;
        int c = it->second;
        int p = 1;
        for (int i = 0; i < 4; ++i)
        {
            int x = s.a[i];
            for (int j = 0; j < cnt[i]; ++j)
                p = (p * x) % MOD;
        }
        res = (res + p*c) % MOD;
    }
    return res;
}

vector<int> compute(string term, vector<string> words, int K)
{
    map<State, int> d[11];
    vector<State> xs;
    int idx[26];
    int cnt[4];
    memset(cnt, 0, sizeof(cnt));
    memset(idx, -1, sizeof(idx));
    int c = 0;
    for (int i = 0; i < term.size(); ++i)
    {
        int k = term[i] - 'a';
        if (idx[k] == -1)
        {
            idx[k] = c++;
            cnt[idx[k]] = 1;
        }
        else cnt[idx[k]]++;
    }
    for (int i = 0; i < words.size(); ++i)
    {
        State s;
        for (int j = 0; j < words[i].size(); ++j)
        {
            int k = words[i][j] - 'a';
            if (idx[k] == -1) continue;
            s.a[idx[k]]++;
        }
        xs.push_back(s);     
    }
    for (int i = 0; i < xs.size(); ++i)
        d[1][xs[i]] += 1;
    vector<int> results;
    results.push_back(calc(d[1], cnt));
    for (int k = 2; k <= K; ++k)
    {
         for (map<State, int>::iterator it = d[k-1].begin(); it != d[k-1].end(); ++it)
         {
            for (int i = 0; i < xs.size(); ++i)
            {
                State s = it->first;
                s.add(xs[i]);
                d[k][s] = mod(d[k][s] + it->second);
            }
         } 
         results.push_back(calc(d[k], cnt));
    }
    return results;
}

int main(int argc, char *argv[])
{
    if (argc != 2) { cout << "specify input/output" << endl; return -1;}
    inp.open ((string(argv[1]) + string(".in")).c_str(), fstream::in);
    out.open ((string(argv[1]) + string(".out")).c_str(), fstream::out);
    int T;
    inp >> T;
    for (int cs = 1; cs <= T; ++cs)
    {
        cout << "processing case " << cs << endl;
        string s;
        int n, K;
        vector <string> words;
        inp >> s >> K;
        inp >> n;
        for (int i = 0; i < n; ++i)
        {
            string w;
            inp >> w;
            words.push_back(w);
        }
        vector<string> terms;
        s += string("+");
        string t;
        for (int i = 0; i < s.size(); ++i)
        {
            if (s[i] == '+') { terms.push_back(t); t = "";}
            else t += string(1, s[i]);
        }
        vector<int> results(K, 0);
        for (int i = 0; i < terms.size(); ++i)
        {
            cout << "doing term " << terms[i] << endl;
            vector<int> temp = compute(terms[i], words, K);
            for (int j = 0; j < K; ++j)
                results[j] = (results[j] + temp[j]) % MOD;
            for (int i = 0; i < temp.size(); ++i)
                cout << " " << temp[i];
            cout << endl;
        }
        
        out << "Case #" << cs << ":";
        for (int i = 0; i < results.size(); ++i)
            out << " " << results[i];
        out << endl;
    }
    return 0;
}