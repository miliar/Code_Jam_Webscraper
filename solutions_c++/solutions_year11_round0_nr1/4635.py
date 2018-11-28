#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("nhap.out","w",stdout);
    int Test,tmp;
    char c;
    int Orange,Blue,TimeOrange,TimeBlue,Time,n;
    int Position;
    cin>>Test;
    for (int j=1;j<=Test;j++)
    {
          Orange=Blue=1;
          TimeOrange=TimeBlue=0;
          cin>>n;
          Time=0;
          for (int i=1;i<=n;i++)
             {
                   do{
                       cin>>c;
                   } while (!(c=='O'||c=='B'));
                   cin>>Position;
                   if (c=='O'){
                       tmp=(int) abs(Orange-Position);
                       Orange=Position;
                       if (tmp<=TimeOrange) tmp=0; else tmp=tmp-TimeOrange;
                       TimeOrange=0;
                       tmp++;
                       Time+=tmp;
                       TimeBlue+=tmp;
                   }
                   else 
                   if (c=='B'){
                       tmp=(int) abs(Blue-Position);
                       Blue=Position;
                       if (tmp<=TimeBlue) tmp=0; else tmp=tmp-TimeBlue;
                       TimeBlue=0;
                       tmp++;
                       Time+=tmp;
                       TimeOrange+=tmp;
                   }
                   //cout<<c<<endl;
             }
             cout<<"Case #"<<j<<": "<<Time<<endl;
    }
    return 0;
}
