#include<iostream>
#include<cstring>
#include<cstdio>
#include<fstream>
using namespace std;
int main()
{
    int i,t,j,x,n,s,p,co=0,y;
    ofstream ot;
    ifstream in ("i.txt");
    ot.open("o.txt");
    in>>t;
    for(j=1;j<=t;j++)
    {
        in>>n>>s>>p;
        co=0;
        int v=(p-1)*3,w=((p-1)*3)-1;
        if(p==1)
        {
            for(i=0;i<n;i++)
            {
                in>>y;
                if(y>0)
                co++;
            }
        }
        else
        {
            for(i=0;i<n;i++)
            {
                in>>y;
                if(y>v)
                co++;
                else if(s>0&&y>=w)
                {
                    s--;
                    co++;
                }
            }
        }
        ot<<"Case #"<<j<<": "<<co<<endl;
    }
    return 0;
}
