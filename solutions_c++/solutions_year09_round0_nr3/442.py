#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <vector>
#include <string>
#include <cstring>
using namespace std;
#define sz(x) (int)x.size()
char mod[22] = " welcome to code jam";
char s[510];
int d[30];
const int Mod = 10000;
int main() {  freopen("Cbig.out", "w", stdout);
    int t;
    scanf("%d\n", &t);
    for(int Case = 1; Case <= t; Case++)  {
        gets(s + 1);
        s[0] = '#';
        //cout << s << endl;
        int n = strlen(s);
        memset(d, 0, sizeof(d));
        for(int i = 1; i < n; i++)  {
            for(int j = 1; j <= 19; j++)  {
                if(s[i] == mod[j])  {
                    if(j == 1)  d[j] = (d[j] + 1) % Mod;
                    else  d[j] = (d[j] + d[j - 1]) % Mod;
                }
            }
        }
        printf("Case #%d: %04d\n", Case, d[19]);
    }
	return 0;
}
