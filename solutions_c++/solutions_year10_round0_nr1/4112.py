#include <fstream>
#include <math.h>
using namespace std;
int p[30];
int main()
{
    ifstream in("A-large.in");
    ofstream out("A-large.out");
    p[0]=1;
    for(int i=1;i<30;i++)
    {
        p[i]=2*p[i-1]+1;
    }
    int t,l,u;
    in>>t;
    int g=0;
    while(g<t)
    {
        g++;
        in>>l>>u;
        if(u<p[l-1])
        {
            out<<"Case #"<<g<<": OFF\n";
            continue;
        }
        if(u==p[l-1])
        {
            out<<"Case #"<<g<<": ON\n";
            continue;
        }
        int j=1;
        int fl=0;
        while(u>p[l-1])
        {
            int k=(j+1)*p[l-1]+j;
            j++;
            if(u==k)
            {
                fl=1;
                out<<"Case #"<<g<<": ON\n";
                break;
            }
            if(k>u)break;
        }
        if(fl==0) out<<"Case #"<<g<<": OFF\n";
    }
    out.close();
}



