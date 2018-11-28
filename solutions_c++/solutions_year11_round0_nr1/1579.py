#include<cstdio>
#include<cstdlib>
#include<algorithm>
using namespace std;
int N,T,x,nowA,nowB,ta,tb,all;
char temp0;
int main()
{
    freopen("test.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for(int r =1;r<=T;r++)
    {
        scanf("%d",&N);
        nowA = 1;nowB = 1;
        ta = 0;tb = 0;
        for(int i=0;i<N;i++)
        {
            scanf(" %c %d",&temp0,&x); 
            if(temp0=='O')
            {
               ta += abs(nowA-x)+1;
               ta = max(ta,tb+1);
               nowA = x;              
            }
            else
            {
               tb += abs(nowB-x)+1;
               tb = max(ta+1,tb);
               nowB = x;    
            }
        }
        printf("Case #%d: ",r);
        printf("%d",max(ta,tb));
          printf("\n");
    }//system("pause");
    return 0;
}
