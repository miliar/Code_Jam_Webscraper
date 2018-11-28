#include <iostream>
#include <cmath>
#include <string.h>
#include <stdio.h>
#include <utility>
#include <vector>
using namespace std;

bool is (vector <pair <long long, long long> > vec, pair <long long, long long> par)
{
    for (long long c=0; c<vec.size(); c++)
    {
        if (vec[c]==par) return true;
    }
    return false;
}

long long tam(long long a)
{
    long long res=0;
    while (a)
    {
        a=a/10;
        res++;
    }
    return res;
}

int main()
{
    long long t;
    cin>>t;

    for (long long s=1; s<=t; s++)
    {
        cout<<"Case #"<<s<<": ";
        long long a, b;
        cin>>a>>b;
        vector <pair<long long, long long> > pares;
        pares.clear();
        long long res=0;
        for (long long c=a; c<=b; c++)
        {
            long long l=tam(c);
            if (l==1) continue;
            long long aux=c;
            for (long long x=0; x<l; x++)
            {
                aux=pow(10, l-1)*(aux%10)+(aux/10);
                for (long long c1=a; c1<=b; c1++)
                {
                    if (aux==c1 && c!=c1)
                    {
                        pair <long long, long long> ax;
                        ax=make_pair(c, c1);
                        if (!is(pares, ax))
                        {
                            pares.push_back(make_pair(c, c1));
                            pares.push_back(make_pair(c1, c));
                            res++;
                        }
                    }
                }
            }
        }
        cout<<res;
        if (s!=t) cout<<endl;


    }
    return 0;
}
