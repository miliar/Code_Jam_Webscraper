#include <iostream>
#include <cmath>
using namespace std;

int max(int a,int b)
{
    if(a>b)
    {
        return a;
    }
    else
    {
        return b;
    }
}

int main()
{
    int T,N;
    int p,po,pb,cnto,cntb,i;
    char c,pc;
    cin>>T;
    for(i=1;i<=T;i++)
    {
        cin>>N;
        po=1;
        pb=1;
        pc='0';
        cnto=0;
        cntb=0;
        while(N--)
        {
            cin>>c>>p;
            if(c=='B')
            {
                if(pc=='B'||pc=='0')
                {
                    cntb+=abs(p-pb)+1;
                }
                else
                {
                    cntb=max(cnto,cntb+abs(p-pb))+1;
                }
                pb=p;
            }
            else
            {
                if(pc=='O'||pc=='0')
                {
                    cnto+=abs(p-po)+1;
                }
                else
                {
                    cnto=max(cntb,cnto+abs(p-po))+1;
                }
                po=p;
            }
            pc=c;
        }
        cout<<"Case #"<<i<<": "<<max(cnto,cntb)<<endl;
    }
    return 0;
}
