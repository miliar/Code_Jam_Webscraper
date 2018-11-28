#include <iostream>
#include <iomanip>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;

int x[50];
int v[50];

int MAX = 1000000000;
int fun(map<int, int> &ch, int k, int t)
{
    int re = 0;
    if(k == 0) return 0;
    for(map<int, int>::iterator it = ch.begin(); it != ch.end(); it++)
    {
        double t1 = it->second == 0 ? MAX : ((double)it->first) / it->second;
        if(t1 <= t)
        {
            k--;
            if(k == 0) return re;
        }
        else re += k;
    }
    return -1;
}
int main(int argc, char *argv[])
{
    int T, C, B, K, N;
    cin >> T;
    for(int ci = 1; ci <= T; ci++)
    {
        cin >> N >> K >> B >> C;
        for(int i = 0; i < N; i++) cin >> x[i];
        for(int i = 0; i < N; i++) cin >> v[i];
        map<int, int> ch;
        for(int i = 0; i < N; i++)
        {
            ch[B-x[i]] = v[i];
        }
        int re = fun(ch, K, C);
        cout << "Case #" << ci << ": ";
        if(re < 0) cout << "IMPOSSIBLE" << endl;
        else cout << re << endl;
    }
    return 0;
}
