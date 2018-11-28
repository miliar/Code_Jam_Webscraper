#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

using namespace std;
int main() {
    int t;
    int a[50];
    int b[50];
    int min_a, max_b;
    int i, j;
    int ans[50];
    scanf("%d", &t);
    min_a = 2000000;
    max_b = 0;
    for(i = 0 ; i < t ; i++) {
        scanf("%d %d", &a[i], &b[i]);
        if(a[i] < min_a) min_a = a[i];
        if(b[i] > max_b) max_b = b[i];
    }
    
    memset(ans, 0, sizeof(ans));

    //char st[10] = itoa(min_a);
    int dec_num = floor(log10(min_a));
    int bound = pow(10, dec_num);
    for(i = min_a ; i <= max_b ; i++)
    {
        if(i > bound)
        {
            dec_num++;
            bound *= 10;
        }
        int temp = i;
        int check[10];
        int check_len = 0;
        for(j = 1 ; j < dec_num ; j++)
        {
            int m = temp % 10;
            temp /= 10;
            temp += m * (bound / 10);

            if(temp <= i) continue;

            bool flag = false;
            for(int k = 0 ; k < check_len ; k++)
                if(temp == check[k]) {
                    flag = true;
                    break;
                }
            if(flag)
                continue;
            check[check_len++] = temp;
            //printf("%d %d\n", i, temp);
            for(int k = 0 ; k < t ; k++)
                if(i >= a[k] && temp <= b[k])
                {
                    ans[k]++;
                   // if(k == 3)
                    //    printf("%d %d\n", i, temp);
                    
                }
        }
    }

    for(int k = 0 ; k < t ; k++)
        printf("Case #%d: %d\n", k+1, ans[k]);
    return 0;
}
