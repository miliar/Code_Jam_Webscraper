// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;

#define FOR(i,a,b) for(int i = (a); i < (b); i++)
#define REP(i,n) FOR(i,0,n)

int t;
int n;
VS g;
double wps[105];
double owps[105];

double wp(int index)
{
    int win = 0, tot = 0;
    for (int i = 0; i < n; i++)
    {
        if (g[index][i] == '1') {win++; tot++;}
        else if (g[index][i] == '0') tot++;
    }
    return 1.0 * win / tot;
}

double wp2(int index, int out)
{
    int win = 0, tot = 0;
    for (int i = 0; i < n; i++)
    {
        if (i == out) continue;
        if (g[index][i] == '1') {win++; tot++;}
        else if (g[index][i] == '0') tot++;
    }
    return 1.0 * win / tot;
}

double owp(int index)
{
    int cnt = 0;
    double sum = 0;
    for (int i = 0; i < n; i++)
    {
        if (g[index][i] != '.') 
        {
            cnt++; 
            sum += wp2(i, index);
        }
    }
    return 1.0 * sum / cnt;
}

double oowp(int index)
{
    int cnt = 0;
    double sum = 0;
    for (int i = 0; i < n; i++)
    {
        if (g[index][i] != '.') {cnt++; sum += owps[i];}
    }
    return 1.0 * sum / cnt;
}

int main()
{
    //freopen("1.in", "r", stdin);
    //freopen("1.out", "w", stdout);

    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-small-attempt0.out", "w", stdout);

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    
    cin >> t;
    for (int cc = 1; cc <= t; cc++)
    {
        cin >> n;
        string str;
        g.clear();
        memset(wps, 0, sizeof(wps));
        memset(owps, 0, sizeof(owps));

        for (int i = 0; i < n; i++)
        {
            cin >> str;
            g.push_back(str);
        }

        for (int i = 0; i < n; i++)
        {
            wps[i] = wp(i);
        }

        for (int i = 0; i < n; i++)
        {
            owps[i] = owp(i);
        }

        printf("Case #%d: \n", cc);
        int sum = 0;
        for (int i = 0; i < n; i++)
        {
            double pri;
            pri = 0.25 * oowp(i) + 0.25 * wps[i] + 0.5 * owps[i];
            printf("%.12f\n", pri);
        }
    }

	return 0;
}

