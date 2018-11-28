#include <stdio.h>
int T, cas = 1;

int N, K;


int main()
{    
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

    scanf("%d", &T);
    while(T--)
    {
        scanf("%d %d", &N, &K);        
        K %= (1<<N);        

        printf("Case #%d: %s", cas++, (K == ((1<<N)-1)) ? "ON\n":"OFF\n");        
    }
    return 0;
}

