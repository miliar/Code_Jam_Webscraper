#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int T;
int N, W, L;
int r[1005], id[1005];
int x[1005], y[1005];
int ansx[1005], ansy[1005];
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> T;
    for(int t = 1; t <= T; t++)
    {
        cin >> N >> W >> L;
        /*if (W < L)
        {
            int tmp = W; W = L; L = tmp;
        }*/
        for(int i = 0; i < N; i++)
        {
            cin >> r[i];
            id[i] = i;
        }
        for(int i = 0; i < N; i++)
            for(int j = i + 1; j < N; j++)
                if (r[i] > r[j])
                {
                    int tmp;
                    tmp = r[i]; r[i] = r[j]; r[j] = tmp;
                    tmp = id[i]; id[i] = id[j]; id[j] = tmp;
                }
        x[N - 1] = y[N - 1] = 0;
        for(int i = N - 2; i >= 0; i--)
        {
            vector<int> v;
            v.push_back(-r[i]);
            v.push_back(W - r[i]);
            for(int j = N - 1; j > i; j--)
            {
                if (x[j] - r[j] + r[i] >= 0) v.push_back(x[j] - r[j]);
                if (x[j] + r[j] - r[i] <= W) v.push_back(x[j] + r[j]);
            }
            bool flag = 0;
            for(int left = 0; left < v.size(); left++)
            {
                int s = v[left];
                if (s + r[i] > W) continue;
                int up = 0;
                for(int j = N - 1; j > i; j--)
                    if (x[j] + r[j] > s && x[j] - r[j] < s + 2 * r[i])
                    {
                        if (y[j] + r[j] > up) up = y[j] + r[j];
                    }
                if (up == 0 || up + r[i] <= L)
                {
                    int xx, yy;
                    if (s == 0) xx = 0; else xx = s + r[i];
                    if (up == 0) yy = 0; else yy = up + r[i];
                    if (!flag)
                    {
                        x[i] = xx; y[i] = yy;
                        flag = 1;
                    }
                    else
                    {
                        if (yy < y[i])
                        {
                            x[i] = xx;
                            y[i] = yy;
                        }
                    }
                }
            }
            //if (!flag) while (1);
        }
        printf("Case #%d:", t);
        for(int i = 0; i < N; i++)
        {
            ansx[id[i]] = x[i]; ansy[id[i]] = y[i];
        }
        for(int i = 0; i < N; i++) cout << " " << ansx[i] << " " << ansy[i];
        cout << endl;
    }
    //system("pause");
    return 0;
}
