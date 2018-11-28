#include <fstream>
#include <cstring>
#include <string>
#include <iostream>
using namespace std;
int main()
{
    ifstream in("1.in");
    ofstream out("1.out");
    int t;
    in>>t;
    //cout<<t;
    int koo=0;
    while(koo!=t)
    {
        koo++;
        long long a,b;
         unsigned long long count=0;
        in>>a>>b;
            char Aa[10];
            sprintf(Aa,"%lld",a);
            string AA(Aa);
            char B[10];
            sprintf(B,"%lld",b);
            string Bo(B);
        for(long long i=a;i<=b;i++)
        {
            int k=0;
            char A[10];
            sprintf(A,"%lld",i);
            string tocheck(A);
            string all=tocheck;
            while(k!=tocheck.length())
            {
                k++;
                char s=tocheck[tocheck.length()-1];

                tocheck.erase(tocheck.length()-1);
                tocheck.insert(0,1,s);
                if(s=='0')
                    continue;
                if(tocheck>all && Bo>=tocheck)
                    count++;

            }
        }
        out<<"Case #"<<koo<<": "<<count<<endl;
    }

}
