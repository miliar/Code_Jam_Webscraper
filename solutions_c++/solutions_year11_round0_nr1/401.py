#include<iostream>
#include<cstdlib>
#include<fstream>

using namespace std;

int abs(int x)
{
    if (x>=0)
        return x;
    else
        return -x;
}

void renew(int& x, int& y)
{
    if (y>x)
        x=y;
}

int main()
{
    //ifstream cin("A-large.in");
    //ofstream cout("A-large.out");
    int ss,n;
    cin>>ss;
    for (int cs=0; cs<ss; cs++)
    {
        cin>>n;
        int o=1, b=1, ot=0, bt=0;        
        for (int i=0; i<n; i++)
        {
            char ch;
            int x;
            cin>>ch>>x;
            if (ch=='O')
            {
                ot=ot+abs(x-o);
                renew(ot,bt);
                ot+=1;
                o=x;
            }
            if (ch=='B')
            {
                bt=bt+abs(x-b);
                renew(bt,ot);
                bt+=1;
                b=x;
            }
        }
        renew(ot,bt);
        cout<<"Case #"<<cs+1<<": "<<ot<<endl;
    }
    return 0;
}
        
