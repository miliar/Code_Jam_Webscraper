#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

string tostr (int x)
{
       int i;
       string ret;
       while (x)
       {
             ret+=x%10+'0';
             x/=10;
       }
       reverse(ret.begin(),ret.end());
       return ret;
}

int toint (string x)
{
    int i,ret=0;
    for (i=0;i<x.size();i++)
    {
        ret*=10;
        ret+=x[i]-'0';
    }
    return ret;
}

FILE *in = fopen ("C.in","r");
FILE *out = fopen ("C.out","w");
bool us[3000000]={false};
vector <int> v;
int main()
{
    int t,A,B,c=1,i;

    fscanf (in,"%d",&t);

    for (c;c<=t;c++)
    {
        fscanf (in,"%d %d",&A,&B);
        int ret=0;
        for (i=A;i<=B;i++)
        {
            string x= tostr(i);
            string y=x;
            v.clear();
            for (int j=1;j<x.size();j++)
            {
                y=y.substr(1,y.size())+y[0];
                if (y[0]=='0')
                   continue;
                int iy=toint(y);
                if (iy<=i||iy>B)
                   continue;
                if (c==4)
                if (us[iy])
                   continue;
                us[iy]=1;
                v.push_back(iy);
                ret++;
            }
            for (int j=0;j<v.size();j++)
                us[v[j]]=0;
        }
        //system ("pause");
        fprintf (out,"Case #%d: %d\n",c,ret);
    }

    return 0;
}
