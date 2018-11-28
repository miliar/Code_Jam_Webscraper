#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;
int main()
{
    int x,a,b,c,i,j;
    scanf("%d",&x);
    ofstream fout;
    fout.open("out.txt");
    for(j=0;j<x;j++)
    {
              scanf("%d%d%d",&a,&b,&c);
              int arr[a],y=0;
              for(i=0;i<a;i++)
              {
                              scanf("%d",&arr[i]);
                              if(arr[i]/3>=c)
                              y++;
                              else if(arr[i]/3==c-2)
                              {
                                   if(arr[i]%3==2 && b>0)
                                   {
                                                y++;b--;
                                   }
                              }
                              else if(arr[i]/3==c-1)
                              {
                                   if(arr[i]%3==0 && b>0 && arr[i]>0)
                                   {
                                                b--;y++;
                                   }
                                   else if(arr[i]%3==1 || arr[i]%3==2)
                                   y++;
                              }
              }
              fout<<"Case #"<<j+1<<": "<<y<<"\n";
    }
    fout.close();
    system("pause");
    return 0;
}
