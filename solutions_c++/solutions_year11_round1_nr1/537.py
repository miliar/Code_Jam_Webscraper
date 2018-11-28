/*
 * File:   main.cpp
 * Author: acfast
 *
 * Created on 2011年5月21日, 上午9:23
 */

#include<ctime>
#include<cmath>
#include<cstdio>
#include<vector>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

typedef long long int64;

int64 ca,n,pd,pg;

int gcd(int a, int b)
{
    if (a%b==0) return b; else return gcd(b,a%b);
}

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    cin>>ca;
    for (int i=1; i<=ca; i++)
    {
        cout<<"Case #"<<i<<": ";
        cin>>n>>pd>>pg;
        if (pg==100)
        {
            if (pd!=100) cout<<"Broken"<<endl; else cout<<"Possible"<<endl;
        } else
        if (pg==0)
        {
            if (pd!=0) cout<<"Broken"<<endl; else cout<<"Possible"<<endl;
        } else
        if (pd==0)
        {
            cout<<"Possible"<<endl;
        } else
        {
            int d=100/gcd(100,pd);
            if (d<=n) cout<<"Possible"<<endl; else cout<<"Broken"<<endl;
        }
    }
    return 0;
}

