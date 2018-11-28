#include<iostream>
#include<cstring>
#include<cstdio>
#include<fstream>
using namespace std;
int main()
{
    char a[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    char b[111],c[111],d[20],e[10];
    string bb;
    int i,t,j,n,x;
    ofstream ot;
    ifstream in ("input.txt");
    ot.open("output.txt");
    in>>t;
    getline(in,bb);
    for(j=1;j<=t;j++)
    {
        getline(in,bb);
        cout<<bb<<endl;
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
        for(i=0;i<bb.size();i++)
        {
            if(bb[i]==' ')
            c[i]=' ';
            else
            c[i]=a[bb[i]-'a'];
        }
        c[i]='\0';
        ot<<d<<c<<endl;
    }
    in.close();
    ot.close();
    return 0;
}

