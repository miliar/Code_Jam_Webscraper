#include<iostream>
#include<algorithm>
#include<fstream>
#include<cstring>
#include<set>
using namespace std;
string str;
long long t,i,j,k,l,a,b,n,p,x,y,z,rj,m;
set<long long> s;
int main()
{
    ofstream fout ("testout.txt");
    ifstream fin ("testin.txt");
    fin>>t;
    for (j=0; j<t; j++)
    {
        fin>>a>>b;
        rj=0;
        i=1;
        k=0;
        while (i<=a)
        {
            i*=10;
            k++;
        }
        i/=10;
        k--;
        for(n=a; n<b; n++)
            {
                m=n;
                for (x=0; x<k; x++)
                {
                    l=m%10;
                    m/=10;
                    m+=i*l;
                    if (m>n && m<=b)
                    s.insert(m);
                }
                rj+=s.size();
                s.clear();
            }
        fout<<"Case #"<<j+1<<": "<<rj<<endl;
    }
    return 0;

}
