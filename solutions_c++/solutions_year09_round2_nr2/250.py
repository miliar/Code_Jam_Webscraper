#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int main(void)
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);

    int t_case,t0,n,i;char t,x[30];scanf("%d ",&t_case);
    for (t0=1;t0<=t_case;++t0)
    {
        printf("Case #%d: ",t0);gets(x);n=strlen(x);
        if (next_permutation(x,x+n))
            puts(x);
        else
        {
            for (i=0;x[i];++i)
                if (x[i]!='0')
                    break;
            t=x[0];x[0]=x[i];x[i]=t;
            putchar(x[0]);putchar('0');
            for (i=1;x[i];++i)
                putchar(x[i]);
            putchar('\n');
        }
    }


    fclose(stdin);fclose(stdout);
    return 0;
}
