#include<iostream>
//#include<conio.h>
#include<algorithm>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int m,k,l,test,su,tt,count=0,cou=0;
    while(cou<n)
    {
cou++;
count=0;
    cin>>m>>su>>test;
    int a[m];
    for(int i=0;i<m;i++)
    {
            cin>>tt;
            
            a[i]=tt;
            }
    sort(a,a+m);
 for(int i=0;i<m;i++)
 {
         if((su!=0)&&(a[i]>2)&&((a[i]==(test*3-3))||(a[i]==(test*3-4))))
         {
  //                 cout<<a[i]<<" "<<su<<endl;
                                                          su--;
                                                          count++;
                                                          }
         else
         {
             if(a[i]>=(test*3-2))
             {
                                 count++;
                                 }
             }
         }
 cout<<"Case #"<<cou<<": "<<count<<endl;
}
//    getch();
    return(0);
    }
