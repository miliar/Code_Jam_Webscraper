#include<stdio.h>
#include<iostream>
#include<math.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    int N;
    char robot1,robot2;int button2,buttonO,buttonB;
    for(int i=1;i<=T;i++)
    {
        int to=0,tb=0;
        scanf("%d",&N);
        button2=buttonO=buttonB=1;
        for(int j=0;j<N;j++)
        {
           cin>>robot2>>button2;

           if(robot2=='O')
           {
               to+=(fabs(button2-buttonO)+1);
               if(to<=tb)
                 to=tb+1;
               buttonO=button2;
              //  printf("%d  %d\n",to,tb);
           }
           if(robot2=='B')
           {
               tb+=(fabs(button2-buttonB)+1);
               if(tb<=to)
                 tb=to+1;
               buttonB=button2;
              // printf("%d %d\n",to,tb);
           }
        }
        if(to>tb)
           tb=to;
        printf("Case #%d: %d\n",i,tb);

    }
    return 0;
}
