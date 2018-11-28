#include<stdio.h>
#include<memory.h>
#include<set>
#include<map>
#include<vector>
#include<string.h>
#include<string>
#include<iostream>
using namespace std;

int n1,i1;
int x1,x2,x3,Y1,y2,y3,n,m,a,p;

int main()
{
    scanf("%d",&n1);
    for(i1=1;i1<=n1;i1++)
    {
        scanf("%d %d %d",&n,&m,&a);
        printf("Case #%d: ",i1);
        x1=0;
        p=0;
        for(Y1=0;Y1<=m;Y1++)
        {
            for(x2=0;x2<=n;x2++)
            {
                for(y2=0;y2<=m;y2++)
                {    
                    for(x3=x2;x3<=n;x3++)
                    {    
                        for(y3=0;y3<=m;y3++)
                        {
                            if(abs((x2-x1)*(y3-Y1)-(y2-Y1)*(x3-x1))==a)
                            {
                                p=1;
                                printf("%d %d %d %d %d %d\n",x1,Y1,x2,y2,x3,y3);
                                break;
                            }
                        }
                        if(p==1)
                            break;
                    }
                        if(p==1)
                            break;
                }
                        if(p==1)
                            break;
            }
                        if(p==1)
                            break;
        }                
        if(p==0)
            printf("IMPOSSIBLE\n");
    }    
    return 0;
}
