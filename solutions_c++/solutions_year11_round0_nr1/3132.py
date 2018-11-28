#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;
struct com
{
    char r;
    int pos;
};

com a[100];
int brob[100];
int orob[100];
int tm,on,bn,T,i,t,n,k1,k2,res;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    int opos=1, bpos=1;
    for (t=0; t<T; t++)
    {
        cin>>n;
        opos=bpos=1;
        on=bn=0;
        for (i=0; i<n;i++)
        {
            cin>>a[i].r>>a[i].pos;
            if (a[i].r=='O')
            {
             orob[on]=a[i].pos;
             on++;
            }else
            {
                brob[bn]=a[i].pos;
                bn++;
            }
        }
        k1=k2=0;
        res=0;
       for (i=0; i<n; i++)
        {
            if (a[i].r=='O')
            {
                tm=abs(opos-a[i].pos)+1;
                opos=a[i].pos;
                res+=tm;
                k1++;
                if (abs(bpos-brob[k2])<=tm) bpos=brob[k2];
                 else
                 if (bpos<brob[k2]) bpos+=tm;
                  else bpos-=tm;
            }else
            {
                tm=abs(bpos-a[i].pos)+1;
                bpos=a[i].pos;
                res+=tm;
                k2++;
                if (abs(opos-orob[k1])<=tm) opos=orob[k1];
                 else
                 if (opos<orob[k1]) opos+=tm;
                  else opos-=tm;
            }
        }
        cout<<"Case #"<<t+1<<": "<<res<<endl;
    }
    return 0;
}
