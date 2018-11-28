#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int t,n,s,p,i,j;
    scanf("%d",&t);
    ofstream ef;
    ef.open("output.txt");
    for(j=0;j<t;j++)
    {
              scanf("%d%d%d",&n,&s,&p);
              int a[n],y=0;
              for(i=0;i<n;i++)
              {
                              scanf("%d",&a[i]);
                              if(a[i]/3>=p)
                              y++;
                              else if(a[i]/3==p-2)
                              {
                                   if(a[i]%3==2 && s>0)
                                   {
                                                y++;s--;
                                   }
                              }
                              else if(a[i]/3==p-1)
                              {
                                   if(a[i]%3==0 && s>0 && a[i]>0)
                                   {
                                                s--;y++;
                                   }
                                   else if(a[i]%3==1 || a[i]%3==2)
                                   y++;
                              }
              }
              ef<<"Case #"<<j+1<<": "<<y<<"\n";
    }
    ef.close();
    system("pause");
    return 0;
}
