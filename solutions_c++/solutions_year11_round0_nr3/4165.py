#include <stdio.h>

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
    __int64 t,xor,sum,min=-1,case_no=0,n,a;
    scanf("%I64d",&t);
    while(t--)
    {
        scanf("%I64d",&n);
        sum = 0;
        min = -1;
        xor = -1;
        while(n--)
        {
            scanf("%I64d",&a);
            sum += a;
            if( min == -1 ) min = a;
            else if( min > a  ) min = a;
            if( xor == -1 ) xor = a;
            else xor ^= a;
        }
        if( xor == 0 )
            printf("Case #%I64d: %I64d\n",++case_no,sum - min);
        else
            printf("Case #%I64d: NO\n",++case_no);
    }
    return 0;
}