#include<math.h>
#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream in("x.in");
    ofstream out("x.out");
    long long qw,temp,t,a,b,i,j,tempa,we,nra,nrb,res;
    nrb=0;
    nra=0;
    res=0;
    in>>t;
    for(qw=1;qw<=t;qw++)
    {
        res=0;
    in>>a>>b;
    for(i=a;i<b;i++)
    {
        nra=0;
            tempa=i;
            while (tempa!=0)
            {
                tempa=tempa/10;
                nra++;
            }
            we=pow(10,nra-1);
        for(j=i+1;j<=b;j++)
        {

            temp=i;
            do{
            temp=temp%we*10+temp/we;
            if (temp==j) res++;
            } while(i!=temp);
        }
    }
    out<<"Case #"<<qw<<": "<<res<<endl;
    }
    }
