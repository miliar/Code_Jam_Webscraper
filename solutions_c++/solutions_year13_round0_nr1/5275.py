#include <cstdio>
#include <algorithm>
using namespace std;

FILE *in,*out;
char ar[5][15];

int read()
{
    int t,z,v;
    for(t=0;t<4;t++)
        fscanf(in,"%s",ar[t]);
    return 0;
}

int check()
{
    int t,z,v;
    for(t=0;t<4;t++)
    {
        char WHO[5]=".XO";
        for(v=1;v<3;v++)
        {
            for(z=0;z<4;z++)
                if(ar[t][z]!=WHO[v] && ar[t][z]!='T')
                    break;
            if(z==4) return v;
            for(z=0;z<4;z++)
                if(ar[z][t]!=WHO[v] && ar[z][t]!='T')
                    break;
            if(z==4) return v;
            for(z=0;z<4;z++)
                if(ar[z][z]!=WHO[v] && ar[z][z]!='T')
                    break;
            if(z==4) return v;
            for(z=0;z<4;z++)
                if(ar[3-z][z]!=WHO[v] && ar[3-z][z]!='T')
                    break;
            if(z==4) return v;
        }
    }
    for(t=0;t<4;t++)
        for(z=0;z<4;z++)
            if(ar[t][z]=='.')
                return 3;
    return 0;
}

int main()
{
    in = fopen("input","r");
    out= fopen("output","w");
    int t,z,v,test;
    fscanf(in,"%d",&test);
    for(t=0;t<test;t++)
    {
        fprintf(out,"Case #%d: ",t+1);
        read();
        z=check();
        if(z==0) fprintf(out,"Draw\n");
        if(z==1) fprintf(out,"X won\n");
        if(z==2) fprintf(out,"O won\n");
        if(z==3) fprintf(out,"Game has not completed\n");
    }
    return 0;
}
