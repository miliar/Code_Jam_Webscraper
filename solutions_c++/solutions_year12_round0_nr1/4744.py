#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>

using namespace std;

string ss;

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    string s = "yhesocvxduiglbkrztnwjpfmaq";
    int n;
    scanf("%d\n", &n);
    for (int i = 1; i <= n; i++)
    {
        printf("Case #%d: ", i);
        getline(cin, ss);
        int nn = ss.length();
        for (int j = 0; j < nn; j++)
            if (ss[j] == ' ') cout << ' '; else cout << (s[ss[j] - 'a']);
        printf("\n");
    }
    return 0;
}
