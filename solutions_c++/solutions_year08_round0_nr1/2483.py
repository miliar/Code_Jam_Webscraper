#include <cstdio>
#include <iostream>
#include <string>
#include <set>
#define MAXL 100
using namespace std;

set<string> S1,S2;
char line[MAXL+1];
int n,s,q,cnt;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j,k;
    gets(line);
    sscanf(line,"%d",&n);
    for(k=0;k<n;k++)
    {
        gets(line);
        sscanf(line,"%d",&s);
        S1.clear();
        for(i=0;i<s;i++)
        {
            gets(line);
            S1.insert(line);
        }
        gets(line);
        sscanf(line,"%d",&q);
        S2.clear();
        cnt=0;
        for(j=0;j<q;j++)
        {
            gets(line);
            S2.insert(line);
            if(S2.size()==s)
            {
                S2.clear();
                S2.insert(line);
                cnt++;
            }
        }
        printf("Case #%d: %d\n",k+1,cnt);
    }
    return 0;
}
