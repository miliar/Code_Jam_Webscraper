#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int k = 1;
map<string, int> m[1<<17];

void insert(int cur, vector<string> v)
{
    if (!v.size())
        return;
    string v0 = v[0];
    if (!m[cur].count(v0))
        m[cur][v0] = k++;
    v.erase(v.begin());
    insert(m[cur][v0], v);
}

void doit()
{
    string s;
    cin >> s;

    vector<string> v;
    string cur;
    for (int i=1; i<s.size(); i++)
        if (s[i] == '/')
        {
            v.push_back(cur);
            cur = "";
        }
        else
            cur += s[i];
    v.push_back(cur);
    insert(0, v);
}

int main()
{
    int t;
    cin >> t;
    for (int tt = 1; tt<=t; tt++)
    {
        int x, y;
        cin >> x >> y;
        for (int i=0; i<x; i++)
            doit();

        int tmp = k;
        for (int i=0; i<y; i++)
            doit();

        cout << "Case #" << tt << ": " << k-tmp << endl;

        for (int i=0; i<k; i++)
            m[i].clear();
        k = 1;
    }
    return 0;
}
