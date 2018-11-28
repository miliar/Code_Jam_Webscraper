#include <string.h>
#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <vector>
using namespace std;

int main()
{
    freopen("c:\\codejam\\input.txt","r",stdin);
    freopen("c:\\codejam\\output.txt","w",stdout);
    int n=0,ln=0,val =0,ln1=0;
    long long count=0;
    cin>>n;
    long long min,max,a;
    for(int j=0;j<n;j++)
    {
        if(j==0)
        cout<<"Case #"<<j+1<<": ";
        else
        cout<<"\nCase #"<<j+1<<": ";
        count = 0;
        cin>>min;
        cin>>max;
//        bool fl[max-min+1];
//        for(int i=0;i<=(max-min);i++)
//            fl[i] = false;
        for(long long l=min;l<=max;l++)
        {   a = l;
            ln = ceil(log10(l));
            if(ln==0)
                continue;
            val =0;
            vector<long long> checker;
            for(int i=0;i<ln-1;i++)
            {
                val = a%10;
                a /= 10;
                a += (val*pow(10,ln-1));
                ln1 = ceil(log10(a));
                int sz = checker.size();
                bool bch = true;
                for(int mn=0;mn<sz;mn++)
                    if(checker[mn]==a)
                    {
                        bch = false;
                        break;
                    }

                if((a > l) && (a <= max) && (a >= min) && (ln == ln1) && bch)
                {
                    count++;
                    checker.push_back(a);
                }
            }
        }
         cout<<count;
    }
    getchar();
    return 0;
}
