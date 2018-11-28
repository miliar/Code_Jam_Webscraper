#include <iostream>
#include <fstream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <time.h>
#include <stdlib.h>
using namespace std;

#define mp make_pair
#define pb push_back
#define vi vector <int>
#define rep(i,n) for(int i = 0; i < n; i++)
#define read(a) rep(i, a.size()) fin >> a[i];
#define write(a) rep(i, a.size()) fout << a[i] << ' '; fout << endl;
#define fi first
#define se second
#define ll long long
const int inf = 2000000000, mod = 1000000007;
const double eps = 0.000001;

int main()
{
    ifstream fin ("input.txt");
    ofstream fout ("output.txt");
    int t;
    fin >> t;
    for (int count = 1; count <= t; count++)
    {
        int n, ans = 0;
        fin >> n;
        vector <int> a(n), sum(n, 0);
        for (int i = 0; i < n; i++)
        {
            fin >> a[i];
            if (i == 0)
               sum[i] = a[i];
            else
                sum[i] = sum[i - 1] + a[i];
            ans = (ans ^ a[i]);
        }
        if (ans != 0)
        {
           fout << "Case #" << count << ": " << "NO" << endl;
           continue;
        }
        int cur = 0;
        for (int i = 0; i < n; i++)
            ans = max(ans, max(a[i], sum[n - 1] - a[i]));
        fout << "Case #" << count << ": " << ans << endl;
    }
    return 0;
}








