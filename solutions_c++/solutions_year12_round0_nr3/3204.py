#include<stdio.h>
inline long next(long inp,long br)
{
    return inp/br + (inp-(inp/br)*br)*10;
}
int main()
{
    long T,tc,A,B,C,dig,br,I,num;
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    scanf("%ld",&T);
    for(tc=1;tc<=T;tc++)
    {
        C = 0;
        scanf("%ld %ld",&A,&B);
        for(br=1,num=A;num!=0;num/=10)
            br *= 10;
        br /= 10;
        if(br==1)
        {
            printf("Case #%ld: %ld\n",tc,0);
            continue;
        }
        for(I=A;I<=B;I++)
        {
            num = next(I,br);
            while(num != I)
            {
                if(A <= num && num <= B)
                    C++;
                num = next(num,br);
            }

        }
        C = C/2;
        printf("Case #%ld: %ld\n",tc,C);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
