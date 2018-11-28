#include <iostream>
using namespace std;

int K, N, ans;
string S;
bool usd[10];
int p[10];

int calc()
{
    int ret = 0;
    char last = '.', now;
    for (int i = 0; i<N/K; i++)
        for (int j = 0; j<K; j++)
        {
            now = S[i*K+p[j+1]-1];
            ret += now != last;
            last = now;
        } 
    return ret;
}

void search(int o)
{
    if (o > K)
    {
        ans <?= calc();
        return;
    }
    for (int i = 1; i<=K; i++)
    if (!usd[i])
    {
        p[o] = i;
        usd[i] = true;
        search(o+1);
        usd[i] = false;
    }
}

int main()
{
        freopen("D-small-attempt0.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int task;
    cin >> task;
    for (int cc = 1; cc<=task; ++cc)
    {
        cout << "Case #" << cc << ": ";
        cin >> K >> S;
        N = S.size();
        
        ans = N;
        memset(usd, 0, sizeof(usd));
        search(1);
        cout << ans << endl;
    }
}
