#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string.h>

int main()
{
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

    int n,k,t,cur,change;
    std::cin >> t;
    for (int tt = 1; tt <= t; tt++)
    {
        std::cin >> n >> k;
        cur = 0;
        for (int i = 0; i < n; i++)
            if ((k >> i) & 1)
                cur ^= (1 << i);
        std::cout << "Case #" << tt << ": " << ( (( cur & ((1<<n)-1)) == ((1<<n)-1) ) ? "ON" : "OFF") << "\n";
    }

	return 0;
}

