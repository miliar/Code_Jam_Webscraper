#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>

using namespace std;

int l,m,n;
bool mark[16][34];
char dict[5004][24];
char mode[1004];

void getRE()
{
    memset(mark, false, sizeof(mark));
    int len=strlen(mode);
    int i,j,p=0;
    for(i=0; i<len; ++i)
    {
        if(mode[i]=='(')
        {
            for(j=i+1; mode[j]!=')'; ++j)
                mark[p][mode[j]-'a']=true;
            i=j;
        }
        else mark[p][mode[i]-'a']=true;
        ++p;
    }
    return ;
}

int main()
{
    /*
    freopen("G:\\Download\\A-large.in", "r", stdin);
    freopen("G:\\Download\\A-large.in.out", "w", stdout);
    */

    int caseid,i,j,a=0;
    scanf("%d %d %d", &l, &m, &n);
    for(i=0; i<m; ++i)
        scanf("%s", dict[i]);
    for(caseid=1; a=0,caseid<=n; ++caseid)
    {
        scanf("%s", mode);
        getRE();
        for(i=0; i<m; ++i)
        {
            for(j=0; j<l; ++j)
                if(!mark[j][dict[i][j]-'a']) break;
            if(j>=l) ++a;
        }
        printf("Case #%d: %d\n", caseid,a);
    }

    return 0;
}

