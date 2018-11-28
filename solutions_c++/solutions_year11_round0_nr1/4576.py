#include <stdio.h>
#define IFBS(a) ((a)>(0)?(a):(-1)*(a))
char s[10010];
int n;
int main()
{
    int t;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &t);
    int ca = 1;
    while (t--)
    {
        scanf("%d ", &n);
        int tot = 0;
        int pos_o=1;
        int pos_b=1;
        char p;
        int k;
        int tot_help = 0;
        char pre='x';
        int cost = 0;
        for (int i=0; i<n; i++)
        {
            scanf(" %c %d",&p,&k);
            if (p == 'O')
            {
                cost = IFBS(k-pos_o);
                pos_o = k;
            }
            else
            {
                cost = IFBS(k-pos_b);
                pos_b = k;
            }
            //printf("tot_help = %d cost=%d\n",tot_help, cost);
            if (pre == p)
            tot_help+=cost+1,tot+=cost+1;
            else
            {
                if (cost < tot_help)
                tot+= 1,tot_help=1;
                else
                tot=tot+ cost-tot_help +1,tot_help = cost-tot_help +1;
            }
            pre=p;
        }
        printf("Case #%d: %d\n",ca++,tot);
    }
    return 0;
}
