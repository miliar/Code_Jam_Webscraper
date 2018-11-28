#include <iostream>
#include <cmath>
#include <string.h>
#include <stdio.h>
#include <utility>
#include <vector>
using namespace std;

bool is (vector <pair <int, int> > vec, pair <int, int> par)
{
    for (int c=0; c<vec.size(); c++)
    {
        if (vec[c]==par) return true;
    }
    return false;
}

int tam(int a)
{
    int res=0;
    while (a)
    {
        a=a/10;
        res++;
    }
    return res;
}

int main()
{
    int t;
    cin>>t;

    for (int s=1; s<=t; s++)
    {
        cout<<"Case #"<<s<<": ";
        int a, b;
        cin>>a>>b;
        vector <pair<int, int> > pares;
        pares.clear();
        int res=0;
        for (int c=a; c<=b; c++)
        {
            int l=tam(c);
            if (l==1) continue;
            int aux=c;
            for (int x=0; x<l; x++)
            {
                aux=pow(10, l-1)*(aux%10)+(aux/10);
                for (int c1=a; c1<=b; c1++)
                {
                    if (aux==c1 && c!=c1)
                    {
                        pair <int, int> ax;
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
