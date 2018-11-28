#include <iostream>
using namespace std;
int f(int a,int p)
{
    int res=2;
    if (a%3==0)
       {
        if (a/3>=p)
           res=0;
        else if (1+(a/3)>=p)
                res=1;
       }
    else if (a%3==1 && (a/3)+1>=p)
            res=0;
    else if (a%3==2)
            if ((a/3)+1>=p)
               res=0;
            else if ((a/3)+2>=p)
                    res=1;
    if (3*a<p)
       res=2;
    return res;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    cin>>t;
    for (int i=1; i<=t; i++)
    {
        int n,s,res=0,p,a;
        cin>>n>>s>>p;
        for (int j=0; j<n; j++)
        {
            cin>>a;
            if (f(a,p)==0)
               res++;
            else if (f(a,p)==1)
            if (s>0)
                    {
                         res++;
                         s--;
                    }
        }
        cout<<"Case #"<<i<<": "<<res<<endl;
    }
    return 0;
}
