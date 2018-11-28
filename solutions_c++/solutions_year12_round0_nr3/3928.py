#include <cstdio>
#include <cctype>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <utility>
#define MPI 3.141592653589793238462643
#define eps 1e-8
#define inf ((int)1e9)
#define pb push_back
#define mp make_pair
#define FI first
#define SE second
#define FF(i, s, e) for(i = s; i <= e; i++)
#define FB(i, s, e) for(i = s; i >= e; i--)
#define Ff(i, s, e) for(i = s; i < e; i++)
#define Fb(i, s, e) for(i = s; i > e; i--)
#define pos(x, y) ((x + y ) | (x != y))
#define sdis(x1, y1, x2, y2) ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
using namespace std;

long long P[] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000};
long long test(long long n)
{
    int res = 0;
    while(n / P[res]) res++;
    return res;
}
long long shift_left(long long n, int len)
{
    return (n / 10) + (n % 10) * P[len - 1];
}
bool vis[10000001];
long long res[10];
int main()
{
    int t, len, i, k;
    long long A, B, j, temp, ans;
    ios::sync_with_stdio(false);
    cin >> t;
    FF(i, 1, t)
    {
        ans = 0;
        cin >> A >> B;
        len = test(A);
        FF(j, A, B)
        {
            temp = j;
            Ff(k, 1, len)
            {
                temp = shift_left(temp, len);
                res[k] = temp;
                if(temp / P[len - 1] == 0 || vis[temp]) continue;
                vis[temp] = 1;
                if(temp > j && temp <= B) ans++;
            }
            Ff(k, 1, len) vis[res[k]] = 0;
        }
        cout << "Case #" << i << ": " << ans << endl;
    }
}
