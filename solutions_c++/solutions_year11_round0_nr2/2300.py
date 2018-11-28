#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

int n, tests, p[255][255];
char ans[1000];
bool b[255][255];
string s, t;

void solve(int test)
{
        cin >> n;
        for (int i = 0; i < n; i++)
        {
                cin >> t;
                p[t[0]][t[1]] = p[t[1]][t[0]] = t[2];
        }
        cin >> n;
        for (int i = 0; i < n; i++)
        {
                cin >> t;
                b[t[0]][t[1]] = b[t[1]][t[0]] = true;
        }
        cin >> n >> s;
        int cur_len = 0;
        for (int i = 0; i < n; i++)
        {
                char cur = s[i];
                if (cur_len > 0)
                {
                        char last = ans[cur_len-1];
                        if (p[cur][last] != 0)
                        {
                                ans[cur_len-1] = p[cur][last];
                                continue;
                        }
                        else
                                ans[cur_len++] = cur;
                }
                else
                        ans[cur_len++] = cur;
                for (int j = 0; j < cur_len; j++)
                        if (b[cur][ans[j]])
                                cur_len = 0;
        }
        cout << "Case #" << test << ": [";
        for (int i = 0; i < cur_len - 1; i++)
                cout << ans[i] << ", ";
        if (cur_len > 0)
                cout << ans[cur_len-1];
        cout << "]" << endl;
}

int main()
{
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
        cin >> tests;
        for (int test = 1; test <= tests; test++)
        {
                for (int i = 0; i < 255; i++)
                        for (int j = 0; j < 255; j++)
                                p[i][j] = 0, b[i][j] = false;
                solve(test);
        }
}