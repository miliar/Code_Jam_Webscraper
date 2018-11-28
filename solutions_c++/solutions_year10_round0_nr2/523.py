#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;

#define PB push_back
#define MP make_pair

typedef int Big[200];
Big L[200], G, T, ans, T1, tmp, B[200], A, tmp2, tmp3[200];
int tt, n;
int compe(Big &a, Big &b)
    {
        if (a[0] > b[0])
            return 1;
        else
        if (a[0] < b[0])
            return -1;
        for (int i = a[0]; i; i--)
            if (a[i] < b[i])
                return -1;
            else
            if (a[i] > b[i])
                return 1;
        return 0;
    }
void sub(Big &a, Big &b, Big &c)
    {
        memset(c, 0, sizeof(c));
        c[0] = max(a[0], b[0]);
        for (int i = 1; i <= c[0]; i++)
            c[i] = a[i] - b[i];
        for (int i = 1; i <= c[0]; i++)
            if (c[i] < 0)
                {
                    c[i + 1]--;
                    c[i] += 10;
                }
        while (c[0] && c[c[0]] == 0)
            c[0]--;
    }
void undo(Big &a, int dep)
    {
        if (compe(a, B[dep]) < 0)
            return;
        memcpy(B[dep + 1], B[dep], sizeof(B[dep]));
        for (int i = 1; i <= B[dep][0]; i++)
            B[dep + 1][i] += B[dep][i];
        for (int i = 1; i <= B[dep + 1][0]; i++)
            if (B[dep + 1][i] >= 10)
                {
                    B[dep + 1][i] -= 10;
                    B[dep + 1][i + 1]++;
                    B[dep + 1][0] = max(B[dep + 1][0], i + 1);
                }
        undo(a, dep + 1);
        if (compe(a, B[dep]) < 0)
            return;
        sub(a, B[dep], tmp2);
        memcpy(a, tmp2, sizeof(a));
    }
void mod(Big &a, Big &b, Big &c)
    {
        memset(c, 0, sizeof(c));
        memcpy(A, a, sizeof(A));
        memcpy(B[0], b, sizeof(B[0]));
        undo(A, 0);
        memcpy(c, A, sizeof(A));
    }
void gcd(Big &a, Big &b, Big &c, int de)
    {
        if (b[0] == 0)
            memcpy(c, a, sizeof(tmp));
        else
            {
                mod(a, b, tmp3[de]);
                gcd(b, tmp3[de], c, de + 1);
            }
    }
int main()
    {
        freopen("B-small-attempt1.in", "r", stdin);
        freopen("B-small-attempt1.out", "w", stdout);
        cin >> tt;
        for (int nu = 1; nu <= tt; nu++)
            {
                memset(L, 0, sizeof(L));
                cin >> n;
                char ch;
                for (int i = 0; i < n; i++)
                    {
                        cin >> ch;
                        L[i][0] = 0;
                        while (ch != ' ' && ch != '\n')
                            {
                                L[i][0]++;
                                L[i][L[i][0]] = ch - '0';
                                ch = ' ';
                                ch = getchar();
                            }
                        for (int j = 1; j < L[i][0] - j + 1; j++)
                            swap(L[i][j], L[i][L[i][0] - j + 1]);
                    }
                memset(G, 0, sizeof(G));
                G[0] = 0;
                for (int i = 0; i < n; i++)
                    for (int j = i + 1; j < n; j++)
                        if (compe(L[i], L[j]) != 0)
                            {
                                if (compe(L[i], L[j]) > 0)
                                    {
                                        sub(L[i], L[j], T);
                                        if (G[0] == 0)
                                            memcpy(G, T, sizeof(G));
                                        else
                                            {
                                                gcd(T, G, T1, 0);
                                                memcpy(G, T1, sizeof(G));
                                            }
                                    }
                                else
                                    {
                                        sub(L[j], L[i], T);
                                        if (G[0] == 0)
                                            memcpy(G, T, sizeof(G));
                                        else
                                            {
                                                gcd(T, G, T1, 0);
                                                memcpy(G, T1, sizeof(G));
                                            }
                                    }
                            }
                mod(L[0], G, ans);
                if (ans[0] != 0)
                    {
                        sub(G, ans, T);
                        memcpy(ans, T, sizeof(T));
                    }
                printf("Case #%d: ", nu);
                for (int i = ans[0]; i; i--)
                    printf("%d", ans[i]);
                if (ans[0] == 0)
                    cout << '0';
                cout << endl;
            }
    }
