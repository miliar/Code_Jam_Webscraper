#include <stdio.h>
#include <algorithm>

using namespace std;

int n;
int data[40];

char buf[50];

int main ()
{
    int t, ct = 0;
    
    for (scanf("%d", &t); t > 0; t --)
    {
        scanf("%d", &n);
        for (int i = 0; i < n; i ++)
        {
            scanf("%s", buf);
            data[i] = -1;
            for (int j = 0; j < n; j ++)
                if (buf[j] == '1')
                    data[i] = j;
//            printf("%d: %d\n", i, data[i]);
        }
        
        int ans = 0;
        
        for (int i = 0; i < n; i ++)
        {
            for (int j = i; j < n; j ++)
                if (data[j] <= i)
                {
//                    printf("i = %d, j = %d\n", i, j);
                    for (int k = j; k > i; k --)
                        data[k] = data[k - 1];
                    ans += j - i;
                    break;
                }
        }
        
        printf("Case #%d: %d\n", ++ ct, ans);
    }
    
    return 0;
}
/*
10
2
10
11
3
001
100
010
4
1110
1100
1100
1000
*/
