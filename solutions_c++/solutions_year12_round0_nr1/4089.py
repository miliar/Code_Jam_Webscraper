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

char a[] = {"yeq ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv"};
char b[] = {"aoz our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up"};
char trans[255], f[255];
char s[100000];

int main() {
    freopen("a.txt", "r", stdin);
    freopen("a.out", "w", stdout);
    
    for (int i = 0; a[i]; ++i) {
        trans[a[i]] = b[i];    
        f[b[i]] = 1;
    }
    for (char i = 'a'; i <= 'z'; ++i)
        if (!f[i])
            for (char j = 'a'; j <= 'z'; ++j)
                if (!trans[j]) trans[j] = i;
    
    int n;
    cin >> n;
    gets(s);
    for (int i = 0; i < n; ++i) {
        gets(s);
        for (int j = 0; s[j]; ++j)
            s[j] = trans[s[j]];
        cout << "Case #" << i + 1 << ": " << s << endl;
    }
}
