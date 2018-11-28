#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;


int main()
{
    int cases;
    int googlers,special,p,result,withoutspecial,withspecial,temp,input;

    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);


    scanf("%d",&cases);

    for (int m=1;m<=cases;++m)
    {
        scanf("%d %d %d",&googlers,&special,&p);

        result=0;

        temp=p-1;
        if (temp<0)
            temp=0;
        withoutspecial=p+temp*2;
        temp=p-2;
        if (temp<0)
            temp=0;
        withspecial=p+temp*2;


        for (int i=0;i<googlers;++i)
        {
            scanf("%d",&input);

            if (input>=withoutspecial)
                ++result;
            else if (input>=withspecial && special)
            {
                ++result;
                --special;
            }
        }

        printf("Case #%d: %d\n",m,result);
    }
    return 0;
}
