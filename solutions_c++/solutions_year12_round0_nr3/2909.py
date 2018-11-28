#include<iostream>
#include<cstring>
#include<cstdio>
#include<fstream>
using namespace std;
int main()
{
    int i,t,j,x,a,b,co=0,y,k;
    char d[100],e[100];
    ofstream ot;
    ifstream in ("input.txt");
    ot.open("output.txt");
    in>>t;
    for(j=1;j<=t;j++)
    {
        in>>a>>b;
        co=0;

        for(i=a;i<=b;i++)
        {
            int count=-1,m=10,n=1;
            x=i;
            while(x)
            {
                x/=10;
                n*=10;
                count++;
            }
            n/=10;
            for(k=0;k<count;k++)
            {
                x=i/m;
                y=i%m;
                y*=n;
                y=y+x;
                m*=10;
                n/=10;
                if(y>i&&y<=b)
                co++;
            }
        }
        strcpy(d,"Case #");
        int n=0;
        x=j;
        while(x)
        {
            int k=x%10;
            x/=10;
            e[n++]=k+'0';
        }
        e[n]='\0';
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
