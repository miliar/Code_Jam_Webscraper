#include <cstdio>

bool test(unsigned int n, unsigned int k)
{
    for(unsigned int i = 0; i < n; ++i)
    {
        if(k % 2 == 0) return false;
        k /= 2;
    }
    
    return true;
}

int main()
{
    int T;
    scanf("%d", &T);
    
    for(int t = 1; t <= T; ++t)
    {
        unsigned int n, k;
        scanf("%d %d", &n, &k);
        printf("Case #%d: %s\n", t, test(n, k) ? "ON": "OFF");
    }
    
    return 0;
}
