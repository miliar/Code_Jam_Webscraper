#include <iostream>
#include <fstream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <math.h>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <deque>
using namespace std;

typedef long long ll;
#define pb push_back
#define mp make_pair
const int inf = 2000000000;
const double eps = 1e-9, Pi = 2 * acos(0.0);

int main()
{
    ifstream cin ("input.txt");
    ofstream cout("output.txt");
    int T;
    cin >> T;
    for (int cc = 1; cc <= T; cc++)
    {
        int n, s, p;
        cin >> n >> s >> p;
        vector <int> a(n);
        int c1 = 0, c2 = 0;
        for (int i = 0; i < n; i++) {
            cin >> a[i];
            if (a[i] == 0) {
               if (p == 0) c1++;
            }
            else if (a[i] == 1) {
                 if (p <= 1) c1++;
            }
            else if (a[i] >= 3 * p - 2)
               c1++;
            else if (a[i] >= 3 * p - 4)
                 c2++;
        }
        cout << "Case #" << cc << ": " << c1 + min(c2, s) << endl;
    }
    return 0;
}


