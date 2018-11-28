#include <iostream>
#include <string>
#include <map>
#include <sstream>
#include <vector>

using namespace std;

string tostring(int a)
{
    stringstream bin;
    bin << a;
    string b;
    bin >> b;
    return b;
}

int toint(string a)
{
    stringstream bin;
    bin << a;
    int b;
    bin >> b;
    return b;
}

string re(string a, size_t k)
{
    string b;
    for (size_t i = k; i < a.size(); i++)
    {
        b += a[i];
    }
    for (size_t i = 0; i < k; i++)
    {
        b += a[i];
    }
    return b;
}

void cal(int a, vector<int> & vecb)
{
    vecb.clear();
    string sa = tostring(a);
    for (size_t i = 1; i < sa.size(); i++)
    {
        string sb = re(sa, i);
        int b = toint(sb);
        vecb.push_back(b);
    }
}

map <pair<int, int>, int> kv;
void run()
{
    kv.clear();
    int n, m;
    cin >> n >> m;
    vector<int> vecb;
    int ans = 0;
    for (int i = n; i <= m; i++)
    {
        cal(i, vecb);
        for (size_t j = 0; j < vecb.size(); j++)
        {
            if (vecb[j] != i && vecb[j] >= n && vecb[j] <= m)
            {
                int x = i, y = vecb[j];
                if (x > y)swap(x, y);
                if (kv[make_pair(x, y)] == 1)
                {
                }
                else
                {
                    ans++;
                    kv[make_pair(x, y)] = 1;
                }
            }
        }
    }
    cout << ans << endl;
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("c.out", "w", stdout);
    
    int N = 0;
    scanf("%d", &N);
    getchar();
    for (int k = 1; k <= N; k++)
    {
        printf("Case #%d: ", k);
        run();
    }
    return 0;
}
