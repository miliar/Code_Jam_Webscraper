#include <stdio.h>
#include <string.h>
#include <math.h>

int main()
{
	freopen("GCJB.in","r",stdin);
	freopen("GCJB.out","w",stdout);
	long long T,n,L,P,C,i,j,x,k,t;
	scanf("%I64d",&T);
	for(t=1;t<=T;t++){
	scanf("%I64d%I64d%I64d",&L,&P,&C);
	i=1,j=0;
	int TT=L*C;
    while(TT<P)
    {
        TT*=C;
        i++;
    }
    for(k=0;;k++)
    {
        if(1<<k>=i)
        break;
    }
    printf("Case #%I64d: %I64d\n",t,k);

	}
	return 0;
}
