#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int K;
string s;

string apply_perm(const string& s, const vector<int>& p)
{
    string res = s;

    for (int i=0; i < s.size(); i+=p.size())
    {
        for (int j=0; j < p.size(); j++)
            res[i+j] = s[i+p[j]];
    }

    return res;
}

int calc_size(const string& s)
{
    int res = 1;
    for (int i=1; i < s.size(); i++)
        if (s[i] != s[i-1])
            res++;
    return res;
}

int solve()
{
    vector<int> p(K);

    for (int i=0; i < K; i++)
        p[i] = i;

    int res = s.size();

    do
    {
        string s1 = apply_perm(s, p);
        res = min(res, calc_size(s1));
    }
    while (next_permutation(p.begin(), p.end()));

    return res;
}

int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);

    int T;
    cin >> T;
    for (int i=1; i <= T; i++)
    {
        cin >> K >> s;
        cout << "Case #" << i << ": " << solve() << endl;
    }

}
