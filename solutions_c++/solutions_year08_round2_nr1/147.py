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

vector<int> x;
vector<int> y;
int n;

int r[3][3];

long long find(int a, int b, int count)
{
    if (count == 0)
        return 1;
        
    if (r[a][b] < count)
        return 0;
    else
    {
        long long result = 1;

        long long f = 1;

        forn(i, count)
        {
            result *= (r[a][b] - i);
            f *= (i + 1);
        }

        result /= f;

        return result;
    }
}

long long answer;

typedef pair<int,int> pt;

map<pt,int> ca;

set< map<pt,int> > was;

void rec(int idx, pt now)
{
    if (idx == 3)
    {
        pt result;

        for (map<pt,int>::iterator i = ca.begin(); i != ca.end(); i++)
        {
            result.first = (result.first + i->first.first * i->second) % 3;
            result.second = (result.second + i->first.second * i->second) % 3;
        }

        long long add = 1;
        bool findOne = false;

        if (result == pt(0,0))
        {
            for (map<pt,int>::iterator i = ca.begin(); i != ca.end(); i++)
            {
                if (i->second > 0)
                {
                    findOne = true;
                    //cout << i->first.first << ", " << i->first.second << ": " << i->second << endl;
                }
                add *= find(i->first.first, i->first.second, i->second);
            }

            //cout << endl;
        }

        if (was.count(ca) == 0 && findOne)
            answer += add,
            was.insert(ca);

        //cout << answer << endl;
    }
    else
    {
        forn(i, 3)
            forn(j, 3)
            {
                pt next(i, j);

                if (next >= now)
                {
                    ca[next]++;

                    rec(idx + 1, next);

                    ca[next]--;
                }
            }
    }
}

int main()
{
    freopen("input.txt", "rt", stdin);

    int testCount;

    cin >> testCount;

    forn(ta, testCount)
    {
        long long a, b, c, d;
        long long x0, y0;
        long long m;

        cin >> n >> a >> b >> c >> d;
        cin >> x0 >> y0;
        cin >> m;

        long long x_ = x0;
        long long y_ = y0;

        x = vector<int>(n);
        y = vector<int>(n);

        memset(r, 0, sizeof(r));

        forn(i, n)
        {
            x[i] = x_;
            y[i] = y_;

            r[x_ % 3][y_ % 3]++;

            x_ = (a * x_ + b) % m;
            y_ = (c * y_ + d) % m;
        }

        ca.clear();
        was.clear();

        answer = 0;

        rec(0, pt(0, 0));

        long long naive = 0;
        /*
        forn(i, n)
            forn(j, i)
                forn(k, j)
                {
                    int xa = x[i] + x[j] + x[k];
                    int ya = y[i] + y[j] + y[k];

                    if (xa % 3 == 0 && ya % 3 == 0)
                        naive++;
                }
        */
        cout << "Case #" << ta + 1 << ": " << answer << endl;
        //cout << "Case #" << ta + 1 << ": " << naive << endl;
    }

    return 0;
}
