/**********************************************************************
Author: littlekid
Created Time: Thu 17 Jul 2008 09:27:15 AM CST
File Name: 
Description: 
**********************************************************************/
#include <iostream>
#include <fstream>
using namespace std;
#define out(x) printf("%s %lld\n", #x, (long long)(x))
const int maxint=0x7FFFFFFF;

template <class T> void get_max(T& _a, const T &_b) {_b > _a? _a = _b:1;}
template <class T> void get_min(T& _a, const T &_b) {_b < _a? _a = _b:1;}

const int MAXN = 102;

int na, nb, t, n;
int arr[MAXN][2], brr[MAXN][2];
int map[MAXN*2][MAXN*2];

void get_input()
{
    cin >> t;
    cin >> na >> nb;
    n = na+nb;
    int hr, mi;
    for (int ix = 1; ix <= na; ++ ix)
    {
        cin >> hr; getchar();
        cin >> mi;
        arr[ix][0] = hr*60+mi;
        cin >> hr; getchar();
        cin >> mi;
        arr[ix][1] = hr*60+mi;
    }
    for (int ix = 1; ix <= nb; ++ ix)
    {
        cin >> hr; getchar();
        cin >> mi;
        brr[ix][0] = hr*60+mi;
        cin >> hr; getchar();
        cin >> mi;
        brr[ix][1] = hr*60+mi;
    }
}

void make_graph()
{
    memset(map, 0, sizeof(map));
    for (int ix = 1; ix <= na; ++ ix)
    {
        for (int jx = 1; jx <= nb; ++ jx)
        {
            if (arr[ix][1]+t <= brr[jx][0])
            {
                map[ix][jx+na] = 1;
            }
            if (arr[ix][0] >= brr[jx][1]+t)
            {
                map[jx+na][ix] = 1;
            }
        }
    }
}

int flag[MAXN*2], mark1[MAXN*2], mark2[MAXN*2];

int dfs(int u)
{
    for (int i = 1; i <= n; ++ i)
    {
        if (!flag[i] && map[u][i])
        {
            flag[i] = true;
            if (!mark2[i] || dfs(mark2[i]))
            {
                mark1[u] = i; mark2[i] = u;
                return 1;
            }
        }
    }
    return 0;
}

int maxmatch()
{
    int res = 0;
    memset(mark1, 0, sizeof(mark1));
    memset(mark2, 0, sizeof(mark2));
    for (int u = 1; u <= n; ++ u)
    {
        memset(flag, 0, sizeof(flag));
        res += dfs(u);
    }
    return res;
}

int main()
{
    //ofstream fout("B.out");
    int T; cin >> T;
    int ansa, ansb;
    for (int ca = 1; ca <= T; ++ ca)
    {
        get_input();
        make_graph();
        ansa = 0, ansb = 0;
        maxmatch();
        for (int ix = 1; ix <= n; ++ ix)
        {
            if (mark2[ix] == 0)
            {
                if (ix <= na) ++ ansa;
                else ++ ansb;
            } 
        }
        cout << "Case #" << ca << ": " << ansa << " " << ansb << endl;///
    }
    return 0;
}

