#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <queue>

using namespace std;

int main() {
    string abeceda = "yhesocvxduiglbkrztnwjpfmaq";
    char test[105];
    string t;
    int n;
    scanf ("%d\n", &n);
    for (int i = 0; i < n; i++) {
        gets (test);
        t = test;
        for (int j = 0; j < t.size (); j++) {
            if (t[j] >= 'a' && t[j] <= 'z') {
                t[j] = abeceda[t[j] - 'a'];
            }
        }
        printf ("Case #%d: %s\n", i + 1, t.c_str ());
    }
    return 0;
}
