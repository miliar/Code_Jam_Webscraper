#include<iostream>
#include<cmath>
#include<cstdio>
using namespace std;

int Abs(int k)
{
if(k<0)
return -k;
else return k;
}
int main()
{
    int num;
    int countB;
    char but;
    int butNum;
    scanf("%d",&num);
    int j=1;
    while(num--)
    {
       scanf("%d",&countB);
       int tb=0;
       int to=0;
       int bbut=1;
       int obut=1; 
       for(int i=0;i<countB;i++)
       {
               scanf(" %c %d",&but,&butNum);
               if(but=='B')
               {
                           tb+=Abs(butNum-bbut)+1;                
                           if(tb<=to)
                           tb=to+1;
                           bbut=butNum;
               }
               else if(but=='O')
               {
                           to+=Abs(butNum-obut)+1;
                           if(to<=tb)
                           to=tb+1;
                           obut=butNum; 
               }
       }
       if(tb>=to)
       printf("Case #%d: %d\n",j,tb);
       else
       printf("Case #%d: %d\n",j,to);
       j++;
    }
    cin.get();
    cin.get();
    return 0;
}
