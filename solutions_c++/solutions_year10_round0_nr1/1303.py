#include<iostream>
#include<cmath>
using namespace std;


int main()
{
      freopen("A-large.in","r",stdin);
      freopen("A-large.out","w",stdout);
     long long test,cnt,snap,i,times,ca=1;
     cin>>test;
    while(test--)
    {
       cin>>snap>>times;
       cnt=(1<<snap);
       i=times%cnt;
       if(i==(cnt-1))
        printf("Case #%lld: ON\n",ca++);
       else
        printf("Case #%lld: OFF\n",ca++);
    }

    return 0;
}
