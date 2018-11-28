#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
char a[5][5];
int main()
{
    int t,i,j,k,ir,jr,ic,jc,k1,k2,count,flag;
    scanf("%d",&t);
    for(count=1;count<=t;++count)
    {
        for(i=0;i<4;++i) scanf("%s",a[i]);
        flag=0;
        for(ir=0;ir<4;++ir)
        {
            k1=k2=0;
            for(jr=0;jr<4;++jr)
            {
                if(a[ir][jr]=='X') ++k1;
                else if(a[ir][jr]=='O') ++k2;
                else if(a[ir][jr]=='T') { ++k1; ++k2; }
                else flag=1;
            }
            if(k1==4) 
            {
                printf("Case #%d: X won",count);
                break;
            }
            else if(k2==4)
            {
                printf("Case #%d: O won",count);
                break;
            }
        }
        if(ir==4)
        {
            for(jc=0;jc<4;++jc)
            {
                k1=k2=0;
                for(ic=0;ic<4;++ic)
                {
                    if(a[ic][jc]=='X') ++k1;
                    else if(a[ic][jc]=='O') ++k2;
                    else if(a[ic][jc]=='T') { ++k1; ++k2; }
                }
                if(k1==4) 
                {
                    printf("Case #%d: X won",count);
                    break;
                }
                else if(k2==4)
                {
                    printf("Case #%d: O won",count);
                    break;
                }
            }
            if(jc==4)
            {
                k1=k2=0;
                for(i=0;i<4;++i)
                {
                    if(a[i][i]=='X') ++k1;
                    else if(a[i][i]=='O') ++k2;
                    else if(a[i][i]=='T'){++k1; ++k2;}
                }
                if(k1==4) 
                {
                    printf("Case #%d: X won",count);
                }
                else if(k2==4)
                {
                    printf("Case #%d: O won",count);
                }
                else 
                {
                    k1=k2=0;
                    for(j=0;j<4;++j)
                    {
                        if(a[j][3-j]=='X') ++k1;
                        else if(a[j][3-j]=='O') ++k2;
                        else if(a[j][3-j]=='T'){++k1; ++k2;}
                    }
                    if(k1==4) 
                    {
                        printf("Case #%d: X won",count);
                    }
                    else if(k2==4)
                    {
                        printf("Case #%d: O won",count);
                    }    
                    else
                    {
                        if(flag==1) printf("Case #%d: Game has not completed",count);
                        else if(flag==0) printf("Case #%d: Draw",count);
                    }
                }
            }
        }
        
        printf("\n");
    }
    return 0;
}
