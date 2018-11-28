#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

int pd;
int pg;
long long n;
int main()
{
    freopen("A-large (1).in","r",stdin);
    freopen("out2.txt","w",stdout);
    int t;
    cin>>t;
    int cas = 1;
    while(t--)
    {
       cin>>n>>pd>>pg;
       if(pg==100)
       {
           if(pd==100)
           {
               cout<<"Case #"<<cas++<<": Possible"<<endl;
               continue;
           }
           else
           {
               cout<<"Case #"<<cas++<<": Broken"<<endl;
               continue;
           }
       }
       if(pd==0)
       {
           cout<<"Case #"<<cas++<<": Possible"<<endl;
           continue;
       }
       if(pg==0&&pd!=0)
       {
           cout<<"Case #"<<cas++<<": Broken"<<endl;
           continue;
       }
       bool flag = false;
       long long minnumber = min(n,(long long)100);
       for(int i =1;i<=minnumber;i++)
       {
           if((pd*i)%100==0)
           {
               flag = true;
               break;
           }
       }
       if(flag)
       {
           cout<<"Case #"<<cas++<<": Possible"<<endl;
           continue;
       }
       else
       {
           cout<<"Case #"<<cas++<<": Broken"<<endl;
           continue;
       }
    }
    return 0;
}
