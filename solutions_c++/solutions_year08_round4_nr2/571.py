#include<iostream>
using namespace std;
int main()
{
    int casen,n,m,a;
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout); 
    scanf("%d",&casen);
    for (int casei=1;casei<=casen;casei++)
    {
        scanf("%d%d%d",&n,&m,&a);
        bool find=false;
        printf("Case #%d: ",casei);
        for (int x1=0; x1 <=n;x1++)
        {
            for (int x2=0;x2<=n;x2++)
            {
                for (int y1=0;y1<=m;y1++)
                {
                    for (int y2=0;y2<=m;y2++)
                      if (abs(x1*y2-x2*y1)==a)
                      {
                                         find=true;
                                         printf("%d %d %d %d %d %d\n",0,0,x1,y1,x2,y2);
                                         break; 
                      } 
                    if (find)break;
                }
                if (find)break;
            }
            if (find)break;
        }
        if (!find)printf("IMPOSSIBLE\n");
    }
    return 0;
} 
                                  
     
