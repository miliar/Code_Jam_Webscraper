#include <vector>
#include <iostream>
using namespace std;

long long A, B, P;

int fa[100000];
bool fact[10000][1000];
vector<int> ve[1001];

int find(int i)
{
    if (i==fa[i]) return i;
    return (fa[i] = find(fa[i]));
}

void merge(int i, int j)
{
    i = find(i);
    j = find(j);
    fa[j] = i;
}

void solve()
{
    int A, B;
    cin >> A >> B >> P;
    for (int i = A; i<=B; i++)
    {
        fa[i] = i;
    }
    for (int i = A; i<=B; i++)
        for (int j = i +1 ; j<=B; j++)
        {
            bool have = false;
            for (int k = 0; k<ve[i].size() && !have; k++)
                if (ve[i][k]>=P)
                for (int l = 0; l<ve[j].size(); l++)
                    if (ve[i][k]==ve[j][l])
                    {
                        have = true;
                        break;
                    }
            if (have) merge(i, j);
        }
    int ret = 0;
    for (int i = A; i<=B; i++)
        if (fa[i]==i)
            ret ++;
    cout << ret << endl;
}

void init()
{
  //  ve[1].push_back(1);
//    fact[1][1] = true;
    for (int i = 2; i<=1000; i++)
    {
        int j = i;
        for (int k = 2; k*k <= j; k++)
        {
            if (j % k==0)
            {
                if (k >= P) 
                {
                    fact[i][k] = true;
                    ve[i].push_back(k);
//                    cout << i << ' ' << k << endl;
                }
                while (j %k==0) j /=k;
            }
        }
            if (j>1) {
                fact[i][j] = true;
                ve[i].push_back(j);
  //              cout << i << ' ' << j << endl;
            }
    }
}

int main()
{
    init();
    freopen("B-small-attempt0.in", "r", stdin);
//    freopen("A.out", "w", stdout);
    int task;
    cin >> task;
    for (int cs = 1; cs<=task; cs++)
    {
        cout << "Case #" << cs << ": ";
        solve();
    }
//    system("pause");

}
