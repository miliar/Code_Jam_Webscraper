#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <functional>
#include <sstream>
#include <iostream>
#include <ctime>
#include <algorithm>

using namespace std;

#define DEBUG(x...) printf(x)
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()

#define _foreach(it, b, e) for(__typeof__(b) it = (b); it != (e); ++it)
#define foreach(x...) _foreach(x)
typedef long long int huge;
const int inf = 0x3f3f3f3f;
const huge hugeinf = 0x3f3f3f3f3f3f3f3fll; // sao dois L’s!!!
const double eps = 1e-9;
const int P = 10009;
// em caso de emergencia
#define _inline(f...) inline f() __attribute__((always_inline)); f

char dict[555][555];
char buf[5555];
int np;
int tem[33]={0};
int go (int a,int qte)
{
    int ret=0;
    if(a==qte)
    {
            int val=0;
            int at=1;
            int tam=strlen(buf);
            for(int j=0;j<tam;j++)
            {
                if(buf[j]=='+')
                {
                    val=val+at;
                    val%=P;
                    at=1;
                }
                else
                {
                    at*=tem[buf[j]-'a'];
                    at%=P;
                }

            }

            val+=at;

        return val;
    }
    for(int j=0;j<np;j++)
    {
         int tam=strlen(dict[j]);
        for(int k=0;k<tam;k++)
                    tem[dict[j][k]-'a']++;

        ret+=go(a+1,qte);
        ret%=P;

          for(int k=0;k<tam;k++)
                    tem[dict[j][k]-'a']--;
    }
    return ret;
}
int main ()
{
    int tt;
    int pp=1;
    scanf("%d",&tt);
    int num;
    while(tt--)
    {

        printf("Case #%d:",pp++);
        scanf(" %s %d",buf,&num);
        scanf("%d",&np);
        for(int i=0;i<np;i++)
            scanf(" %s",dict[i]);

        int ret[333]={0};


        for(int i=1;i<=num;i++)
            printf(" %d",go(0,i));
        printf("\n");
    }
    return 0;
}
