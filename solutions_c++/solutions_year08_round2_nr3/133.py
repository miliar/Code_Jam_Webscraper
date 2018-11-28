#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <numeric>

using namespace std;

typedef signed long long i64;  
typedef unsigned long long u64;
typedef long double real;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef vector<VS> VVS;

#define forr(i,n0,n1) for(int i=(n0); i<(n1); i++)
#define forn(i,n) for(int i=0; i<(n); i++)
#define fors(i,s) forn(i, (int)s.length())
#define forv(i,v) forn(i, (int)v.size())
#define fore(t, it, obj) for (t :: iterator it = obj.begin(); it != obj.end(); it++)

#define two(n) (1 << (n))
#define hold(mask, i) (((mask) & two(i)) != 0)

#define pb push_back
#define all(v) v.begin(), v.end()
#define mp make_pair

template<class T> T str2t(string s, T dummy)
{
    stringstream ss; T res;
    ss << s, ss >> res;
    return res;
}

template<class T> string t2str(T ind)
{
    stringstream ss; string res;
    ss << ind, ss >> res;
    return res;
}

vector<string> tokenize(string s, string tokens)
{
    s = s + tokens[0];
    vector <string> res;
    string tmp;
    for (int i=0;i<s.length();i++)
        if (tokens.find(s[i]) != string::npos)
        {
            if (tmp != "")
                res.push_back(tmp), tmp = "";
        } else
            tmp += s[i];
    return res;
}

template<class T> vector<T> tokenize_t(const string& s, const string& tokens, T waste)
{
    vector<string> ress = tokenize(s, tokens);
    vector<T> res(ress.size());
    for (int i = 0; i < ress.size(); i++)
        res[i] = str2t(ress[i], waste);
    return res;
}

int n;
int m;
vector<int> idx;

vector<int> naive()
{
    vector<int> result(n);

    int now = 0;

    forn(i, n)
    {
        int count = 0;
        int off = -1;
        while (true)
        {
            off++;

            int j = (now + off) % n;

            if (result[j] == 0)
                count++;

            int left = n - i;

            int find = (i % left) + 1;

            if (count == find)
            {
                result[j] = i + 1;
                now = j;
                break;
            }
        }
    }

    vector<int> answer(m);

    forn(i, m)
        answer[i] = result[idx[i] - 1];

    return answer;
}

int main()
{
    freopen("input.txt", "rt", stdin);

    int testCount;

    cin >> testCount;

    forn(ta, testCount)
    {
        cin >> n >> m;
        idx = vector<int>(m);

        forn(i, m)
            cin >> idx[i];

        vector<int> result = naive();

        cout << "Case #" << ta + 1 << ":";// " << answer << endl;

        forn(i, m)
            cout << " " << result[i];
        cout << endl;
        //cout << "Case #" << ta + 1 << ": " << naive(a, b, P) << endl;
    }

    return 0;
}
