#include <iostream>
#include <queue>
#include <stdio.h>

int abs(int x)
{
    return (x<0?-x:x);
}

using namespace std;

int main()
{
    freopen("input.txt","rt",stdin);
    freopen("output.txt","wt",stdout);
    int t;
    cin>>t;
    for(int test_case=0;test_case<t;test_case++)
    {
        int n;
        cin>>n;
        int opos=1,bpos=1;
        int ot=0,bt=0;
        int ct=0;
        for(int i=0;i<n;i++)
        {
            char c;
            int x;
            cin>>c>>x;
            if(c=='O')
                {
                    int q=ct-ot;
                    if(q<abs(opos-x))ct+=abs(opos-x)-q;
                    ct++;
                    ot=ct;
                    opos=x;
                }
            else
                {
                    int q=ct-bt;
                    if(q<abs(bpos-x))ct+=abs(bpos-x)-q;
                    ct++;
                    bt=ct;
                    bpos=x;
                }
        }
        cout<<"Case #"<<test_case+1<<": "<<ct<<endl;
    }
    return 0;
}
