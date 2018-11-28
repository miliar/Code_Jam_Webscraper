#include <cstdio>
#include <cstring>
#include <iostream>
#include <fstream>

using namespace std;

int n,s,p,sum;
int t[101];

ofstream fout("B-large.out");
ifstream fin("B-large.in");

void sub()
{
    int i,u1,u2;
    u1=p;
    if ((p-1)>0) u1=u1+(p-1)*2;
    u2=p;
    if ((p-2)>0) u2=u2+(p-2)*2;
    for (i=1;i<=n;i++)
    {
        if (t[i]>=u1) sum++;
          else if ((t[i]>=u2)&&(s>0))
          {
              s--;
              sum++;
          }
    }
    return;
}

int main()
{
    int T,i,j;
    fin>>T;
    for (i=1;i<=T;i++)
    {
        fin>>n>>s>>p;
        memset(t,0,sizeof(t));
        for (j=1;j<=n;j++)
          fin>>t[j];
        sum=0;
        sub();
        fout<<"Case #"<<i<<": "<<sum<<endl;
    }
    return 0;
}
