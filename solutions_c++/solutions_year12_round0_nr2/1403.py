#include <fstream>

using namespace std;
int n,x,p,t,T,a,b,S,i,scor;
int main()
{
    ifstream fi("dance.in");
    ofstream fo("dance.out");
    fi>>T;
    for(t=1;t<=T;t++)
    {
        fi>>n>>S>>p;
        a=b=0;
        for(i=1;i<=n;i++)
        {
            fi>>x;
            scor=x/3;
            if(x%3) scor++;
            if(scor>=p) { a++; continue; }
            if(x%3==1 or x==0) continue;
            if(scor+1>=p) b++;
        }
        if(S<b) b=S;
        fo<<"Case #"<<t<<": "<<a+b<<"\n";
    }
    return 0;
}
