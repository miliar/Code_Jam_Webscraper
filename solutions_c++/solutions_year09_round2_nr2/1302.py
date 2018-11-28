#include <iostream>
#include <algorithm>
#include <cstdio>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

int main()
{
    int T, kase, N;
    char str[1000];
    char ch;
    int i, len, idx;

    cin >> T;

    kase = 1;
    while (T--) {
        cin >> N;
        sprintf(str, "%d", N);
        len = strlen(str);
        cout << "Case #" << kase++ << ": " ;
        if (next_permutation(str, str+len) == 0) {
            str[len] = '0';
            str[len+1] = 0;
            len++;
            idx = -1;
            for (i = 0; i < len; i++) {
                if (str[i] != '0' && (idx == -1 || str[i] < str[idx])) {
                    idx = i; 
                }
            }
            ch = str[idx];
            str[idx] = str[0];
            str[0] = ch;
            sort(str+1, str+len);
            cout << str << endl;
        }
        else {
            cout << str << endl;
        }
    }
    return 0;
}
