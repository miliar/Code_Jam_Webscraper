#include<iostream>
using namespace std;

const int MAXN = 1024;

int piles[MAXN];
int n;

int main()
{
    int t,test = 1;
    scanf("%d", &t);
    while(t >= test)
    {
            scanf("%d", &n);
            
            int can = 0;
            int sum = 0;
            int mini = MAXN*MAXN*MAXN;
            
            for(int i = 0; i < n; i++)
            {
                    scanf("%d", &piles[i]);
                    can ^= piles[i];
                    sum += piles[i];
                    
                    if(mini > piles[i]) mini = piles[i];
            }
            
            printf("Case #%d: ", test);
            if(can) printf("NO\n");
            else printf("%d\n", sum - mini);
            
            test++;     
    }
    
    return 0;
}
