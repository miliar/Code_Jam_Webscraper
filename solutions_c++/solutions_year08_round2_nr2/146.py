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

int answer;

map<long long, set<long long> > pa;

long long P;

void ft(long long n)
{
    long long was = n;
    long long p = 2;
    for (; p * p <= n; p++)
    {
        if (n % p == 0)
        {
            while (n % p == 0)
            {
                n /= p;
                if (p >= P)
                    pa[p].insert(was);
            }
        }
    }
    if (n >= p)
        pa[n].insert(was);
}

int index(const vector<long long>& nums, long long value)
{
    return lower_bound(all(nums), value) - nums.begin();
}

vector<int> dsu;

int leader(int i)
{
    if (i != dsu[i])
        dsu[i] = leader(dsu[i]);
    return dsu[i];
}

bool merge(int a, int b)
{
    int la = leader(a);
    int lb = leader(b);

    if (la != lb)
    {
        if (rand() % 2)
            swap(la, lb);

        //ut << "merge " << a << " " << b << endl;

        dsu[la] = lb;

        return true;
    }
    else
        return false;
}

bool prime(int n)
{
    if (n <= 1)
        return false;

    int d = 0;

    forn(i, n)
        if (n % (i + 1) == 0)
            d++;

    return d == 2;
}

int has(int a, int b)
{
    for (int i = P; i <= min(a, b); i++)
        if (prime(i) && a %i == 0 && b % i == 0)
            return true;
    return false;
}

bool g[1000][1000];
bool used[1000] = {0};

int naive(int a, int b, int p)
{
    int n = b - a + 1;

    memset(g, 0, sizeof(g));
    memset(used, 0, sizeof(used));

    for (int i = a; i <= b; i++)
    {
        g[i][i] = true;
        for (int j = a; j <= b; j++)
            if (has(i, j))
            {
                g[i - a][j - a] = true;
                //cout << i <<  " " << j << endl;
            }
    }

    forn(t, n)
        forn(i, n)
            forn(j, n)
                g[i][j] = g[i][j] || (g[i][t] && g[t][j]);

    int answer = 0;

    forn(i, n)
    {
        if (!used[i])
            answer++;
        forn(j, n)
            if (g[i][j])
                used[j] = true;
    }

    return answer;
}

int main()
{
    freopen("input.txt", "rt", stdin);

    int testCount;

    cin >> testCount;

    forn(ta, testCount)
    {
        answer = 0;

        long long a, b;

        cin >> a >> b >> P;

        pa.clear();

        vector<long long> nums;

        int n = b - a + 1;

        for (long long i = a; i <= b; i++)
        {
            ft(i);
            nums.push_back(i);
        }

        dsu = vector<int>(n);

        forn(i, n)
            dsu[i] = i;

        answer = n;

        for (map<long long, set<long long> >::iterator i = pa.begin();
            i != pa.end(); i++)
        {
            vector<long long> s(all(i->second));

            forn(j, s.size())
            {
                if (j + 1 < s.size() && i->first >= P)
                {
                    int a = index(nums, s[j]);
                    int b = index(nums, s[j + 1]);

                    answer -= merge(a, b);
                }
            }
        }

        cout << "Case #" << ta + 1 << ": " << answer << endl;
        //cout << "Case #" << ta + 1 << ": " << naive(a, b, P) << endl;
    }

    return 0;
}
