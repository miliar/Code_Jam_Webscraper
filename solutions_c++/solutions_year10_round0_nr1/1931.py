#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <sstream>
#include <set>
#include <math.h>

#define N 1000000
 
int main ()
{
    int T, i = 1;
    scanf ("%d", &T);
 
    while (T) 
	{
		T --;
        int n;
        int k;
        scanf ("%d %d", &n, &k);
 
        if (n > 0 && ((k + 1) % (1 << n) == 0))
            printf ("Case #%d: ON\n", i);
        else
            printf ("Case #%d: OFF\n", i);

		i ++;
    }
 
    return 0;
}
