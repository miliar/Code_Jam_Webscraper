#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <math.h>
#include <set>
using namespace std;
char voltmar[2000001];

inline int jobbra_tol(const int& a,int mennyivel)
{
    int ret=a;
    for (int i=0;i<mennyivel;i++)
    {
        int bal=(ret%10)*pow10((int)log10(a));
        ret=ret/10+bal;
    }
    return ret;
}

int solve()
{
    int a,b;
    scanf("%d",&a);
    scanf("%d",&b);
    memset(voltmar,0,2000001);
    int ret=0;
    for (int i=a;i<b;i++)
//        if (voltmar[i]==0)
        {
            voltmar[i]=1;
            int log_i=log10(i);
            set<int> eltolasok;
            for (int i2=1;i2<=log_i;i2++)
            {
                int akt_eltol=jobbra_tol(i,i2);
                if (akt_eltol<=b && akt_eltol!=i && (int)log10(akt_eltol)==log_i && i<akt_eltol && eltolasok.find(akt_eltol)==eltolasok.end())
                {
                    eltolasok.insert(akt_eltol);
                  //  printf("par:%d %d\n",i,akt_eltol);
                    ret++;
  //                  voltmar[akt_eltol]=1;
                }
            }
    }
    return ret;
}

int main()
{
int casenum;
scanf("%d",&casenum);
for (int i=0;i<casenum;i++)
{
    printf("Case #%d: %d\n",i+1,solve());
}
}
