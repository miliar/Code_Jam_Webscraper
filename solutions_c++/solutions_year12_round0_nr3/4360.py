#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

const double eps=1e-8;

#define MEM(a) memset(a,0,sizeof(a));
#define FOR(n) for(int i=0;i<n;i++)

char x[100],y[100];
bool used[10001];

int main()
{
    //freopen("C-small-attempt0.in","r",stdin);
    //freopen("b.out","w",stdout);
    int i,j,t,cnt=0,a,b,tem,len,n,m,sum;
    scanf("%d",&t);
    while(t--)
    {
        sum=0;
        cnt++;
        scanf("%d%d",&a,&b);

        for(n=a; n<=b; n++)
        {
            if(n<10)
                continue;
            MEM(used);
            len=0;
            tem=n;
            while(tem)
            {
                x[len++]='0'+tem%10;
                tem/=10;
            }
            x[len]='\0';
            strrev(x);

            for(i=1;i<len;i++)
            {
                for(j=0;j<len-i;j++)
                {
                    y[j+i]=x[j];
                }
                for(j=len-i;j<len;j++)
                {
                    y[j-len+i]=x[j];
                }

                m=0;
                for(j=0;j<len;j++)
                {
                    m*=10;
                    m+=y[j]-'0';
                }

                if(n<m&&m<=b&&!used[m])
                {
                    used[m]=true;
                    //printf("n=%d,m=%d\n",n,m);
                    //printf("YES\n");
                    sum++;
                }
            }
            //printf("\n");
        }
        printf("Case #%d: %d\n",cnt,sum);
    }
    return 0;
}
