#include <stdio.h>
#include <cassert>
#include <algorithm>

int main()
{
    int Cases;
    scanf_s("%d", &Cases);
    for(int t=1; t<=Cases; t++)
    {
        printf("Case #%d: ", t);
        
        int N;
        scanf("%d", &N);
        
        int Sum=0, Xor=0, Min=1000001;
        for(int i=0; i<N; i++)
        {
            int c;
            scanf("%d", &c);
            Sum += c;
            Xor ^= c;
            Min = std::min(c, Min);
        }
        assert(Min <= 1000000);
        if(Xor != 0)
        {
            printf("NO\n");
        }
        else
        {
            printf("%d\n", Sum-Min);
        }
    }
    return 0;
}