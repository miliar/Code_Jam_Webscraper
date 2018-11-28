#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

int tn;
int n,s,p;
int pos,exi,tmp;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&tn);
    for (int w=1;w<=tn;w++)
    {
        scanf("%d%d%d",&n,&s,&p);
        pos=exi=0;
        for (int i=1;i<=n;i++)
        {
            scanf("%d",&tmp);
            if (tmp % 3==1)
                if (tmp/3+1>=p) exi++;
            if (tmp % 3==0)
            {
                if (tmp/3>=p) exi++;
                else if (tmp/3+1>=p && tmp>=3) pos++;
            }
            if (tmp % 3==2)
            {
                if (tmp/3+1>=p) exi++;
                else if (tmp/3+2>=p) pos++;
            }
        }
        printf("Case #%d: %d\n",w,exi+min(pos,s));
    }
    return 0;
}
