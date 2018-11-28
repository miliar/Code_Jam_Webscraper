#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    long long int i,l,j,t,n,sum,min,total;
    char c;
    ifstream fi("input.txt");
    ofstream fo("output.txt");
    fi>>t;
    for(j=1;j<=t;j++)
    {
        fi>>n;total=0;sum=0;
        for(i=1;i<=n;i++)
        {
            fi>>l;
            total=total^l;
            sum+=l;
            if(i==1)min=l;
            else if(min>l) min=l;
        }
        fo<<"Case #"<<j<<": ";
        if(total!=0) fo<<"NO";
        else fo<<(sum-min);
        fo<<"\n";
    }
    fo.close();
}            
