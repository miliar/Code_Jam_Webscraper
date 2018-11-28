#include<stdio.h>
#include<algorithm>

using namespace std;

int main()
{
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);
    int cases,cc,per[22],k,i,an,aa;
    char ss[50005],s[50005];
    scanf("%d",&cases);
    
    for(cc=1;cc<=cases;cc++)
    {
        scanf("%d%s",&k,ss);
        for(i=0;i<k;i++)per[i]=i;
        an=222222;
        do
        {
            for(i=0;ss[i];i++)s[i]=ss[i-i%k+per[i%k]];
            s[i]=0;
            //fprintf(stderr,"s=%s\n",s);
            aa=1;
            for(i=0;s[i+1];i++)if(s[i]!=s[i+1])aa++;
            an<?=aa;
        }while(next_permutation(per,per+k));
        printf("Case #%d: %d\n",cc,an);
    }
    
    return 0;
}
