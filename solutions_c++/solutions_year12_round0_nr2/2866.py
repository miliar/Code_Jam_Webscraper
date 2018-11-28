#include<iostream>
#include<cstring>
#include<cstdio>
#include<fstream>
using namespace std;
int main()
{
    int i,t,j,x,n,s,p,co=0,y;
    char d[100],e[100];
    ofstream ot;
    ifstream in ("input.txt");
    ot.open("output.txt");
    in>>t;
    for(j=1;j<=t;j++)
    {
        in>>n>>s>>p;
        co=0;
        int a=(p-1)*3,b=((p-1)*3)-1;
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
                if(y>a)
                co++;
                else if(s>0&&y>=b)
                {
                    s--;
                    co++;
                }
            }
        }
        strcpy(d,"Case #");
        n=0;
        x=j;
        while(x)
        {
            int k=x%10;
            x/=10;
            e[n++]=k+'0';
        }
        e[n]='\0';
        cout<<e<<endl;
        strrev(e);
        strcat(d,e);
        n=strlen(d);
        d[n++]=':';
        d[n++]=' ';
        d[n]='\0';
        ot<<d<<co<<endl;
    }
    return 0;
}
