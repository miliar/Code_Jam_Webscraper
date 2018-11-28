/*
  ID: nigo1
  LANG: C++
  TASK: A
*/
#include <iostream>
#include <cstring>
#include <ctime>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <cstring>
#include <map>
#include <queue>
#include <set>
#include <stack>

#define TIME pf("%f", (double)clock()/CLOCKS_PER_SEC);

using namespace std;

int N;

int used[256];
int main()
{
	freopen ("A.in", "r", stdin);
	freopen ("A.out", "w", stdout);

    string a = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvqz";
    string b = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upzq";

    for (int i = 0; i < a.size(); i++) {
        used[a[i]] = b[i];
    }

    scanf ("%d\n", &N);
    for (int test = 1; test <= N; test++) {
        printf ("Case #%d: ", test);
        char c;
        while ((c = getchar()) != '\n') {
            printf ("%c", char (used[c]));
        }
        printf ("\n");
    }

    return 0;
}
