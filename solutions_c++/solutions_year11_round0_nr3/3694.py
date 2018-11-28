#include<cstdio>
#define MAXN 1000
int T, N;

int tab[MAXN];

int main()
{
    scanf("%d", &T);
    for(int i=0;i<T;i++)
    {
            int sum=0;
            int xorsum=0;
            int min=100000001;
            
            scanf("%d", &N);
            for(int j=0;j<N;j++)
            {
                    scanf("%d", &tab[j]);    
                    if(tab[j]<min) min=tab[j];
                    sum+=tab[j];
                    if(j>0) xorsum = xorsum ^ tab[j];
                    else xorsum = tab[j];    
             //       printf("xorsum: %d, sum: %d, tab[%d]: %d\n", xorsum, sum, j, tab[j]);
            }
            if(xorsum != 0) printf("Case #%d: NO\n", i+1);
            else printf("Case #%d: %d\n", i+1,  sum - min);       
    }
  //  scanf("%d", T);
}
