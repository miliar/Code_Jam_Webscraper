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
#define read(a) rep(i, a.size()) cin >> a[i];
#define write(a) rep(i, a.size()) cout << a[i] << ' '; cout << endl;
#define fi first
#define se second
#define ll long long
const int inf = 2000000000, mod = 1000000007;
const double eps = 0.000001;

int main()
{
    ifstream cin ("input.txt");
    ofstream cout ("output.txt");
    int t;
    cin >> t;
    for (int count = 1; count <= t; count++)
    {
        cout << "Case #" << count << ": ";
        int n, l, h, res = -1;
        cin >> n >> l >> h;
        vector <int> a(n);
        for (int i = 0; i < n; i++)
            cin >> a[i];
        for (int x = l; x <= h; x++)
        {
            bool ok = true;
            for (int j = 0; j < n; j++)
                if (a[j] % x != 0 && x % a[j] != 0)
                   ok = false;
            if (ok) {
               res = x;
               break;
            }
        }
        if (res != -1)
           cout << res << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}








