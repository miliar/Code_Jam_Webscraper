#include <cstdio>
#include <set>
using namespace std;

int main2()
{
    int inf, sup;
    scanf("%d%d", &inf, &sup);
    
    int res = 0;
    for (int i=inf; i<sup; i++)
    {
        set<int> interdire;
        
        int p = 1;
        while (p <= i)
        {
            int a = i/p;
            int q = 1;
            while (q <= i/p) q*= 10;
            a += q*(i%p);
            
            if (inf <= i && i < a && a <= sup && interdire.count(a) == 0)
            {
                interdire.insert(a);
                res++;
            }
            
            p *= 10;
        }
    }
    
    printf("%d\n", res);
    
    return 0;
}

int main()
{
    int N;
    scanf("%d", &N);
    for (int i=0; i<N; i++)
    {
        printf("Case #%d: ", i+1);
        main2();
    }
}
