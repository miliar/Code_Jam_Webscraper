/*
 * Author: code6
 * Created Time:  2011/6/4 23:32:20
 * File Name: B.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <ctime>
#include <string>

using namespace std;
#define out(v) cerr << #v << ": " << (v) << endl
#define SZ(v) ((int)(v).size())
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}
typedef long long ll;
const double PI=acos(-1.0);
const double eps=1e-6;

int R, C, D;
int v[505][505];
double sum[505][505];
double sum1[505][505];
double sum2[505][505];

double get(double arr[505][505], int x1, int y1, int x2, int y2)
{
    x1++;
    x2++;
    y1++;
    y2++;
    return  arr[x2][y2] - arr[x2][y1 -1] - arr[x1 -1][y2] + arr[x1 -1][y1 - 1];
}

bool zero(double v) 
{
    return fabs(v) < eps;
}

int main() {
    
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);
    
    int t, cas = 0;
    
    scanf("%d", &t);
    while (t--) {
        cas ++;
        scanf("%d%d%d", &R, &C, &D);
        int i, j, k;
        memset(sum, 0, sizeof(sum));
        memset(sum1, 0, sizeof(sum1));
        memset(sum2, 0, sizeof(sum2));
        for (i = 0; i < R; i++) {
            for (j = 0; j < C; j++) {
                scanf("%1d", &v[i][j]);
                v[i][j] += D;
                sum[i + 1][j + 1] = sum[i ][j + 1] + sum [i + 1][j] - sum[i][j] + v[i][j];
                sum1[i + 1][j + 1] = sum1[i ][j + 1] + sum1 [i + 1][j] - sum1[i][j] + v[i][j] * i;
                sum2[i + 1][j + 1] = sum2[i ][j + 1] + sum2 [i + 1][j] - sum2[i][j] + v[i][j] * j;
            }
        }
        
        int ans = 0;
        for (i = 0; i < R; i++) {
            for (j = 0; j < C; j++) {
                for (k = max(ans, 3); k <= min(R, C); k++) {
                    int i1, j1;
                    i1 = i + k - 1;
                    j1 = j + k - 1;
                    if (i1 >= R || j1 >= C) {
                        break;
                    }
                    
                    double mx, my;
                    mx = i + (k - 1) / 2.0;
                    my = j + (k - 1) / 2.0;
                    
                    //int x1, y1;
                    double tx, ty;
                    //for (x1 = i; x1 <= i1; x1++) {
                        //for (y1 = j; y1 <= j1; y1++) {
                            //tx += v[x1][y1] * (x1 - mx);
                            //ty += v[x1][y1] * (y1 - my);
                        //}
                    //}
                    
                    tx = get(sum1, i, j, i1, j1);
                    tx -= (v[i][j] + v[i][j1]) * i + (v[i1][j] + v[i1][j1]) * i1;
                    ty = get(sum2, i, j, i1, j1);
                    ty -= (v[i][j] + v[i1][j]) * j + (v[i][j1] + v[i1][j1]) * j1;
                    
                    tx -= get(sum, i, j, i1, j1) * mx;
                    tx += (v[i][j] + v[i][j1]) * mx + (v[i1][j] + v[i1][j1]) * mx;
                    
                    ty -= get(sum, i, j, i1, j1) * my;
                    ty += (v[i][j] + v[i1][j]) * my + (v[i][j1] + v[i1][j1]) * my;
                    
                    if (zero(tx) && zero(ty)) {
                        ans = max(ans, k);
                    }
                }
            }
        }
        
        printf("Case #%d: ", cas);
        if (ans == 0) {
            puts("IMPOSSIBLE");
        } else {
            printf("%d\n", ans);
        }
    }
    return 0;
}

