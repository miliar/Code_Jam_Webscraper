#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;
int po,pb,to,tb;
int n,t,ca=1;
int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    int i;
    char c[2];
    int pos;
    int mt,lt;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        po = 1;
        pb = 1;
        to = 0;
        tb = 0;
        lt = max(to,tb);
        for(i=0;i<n;i++)
        {
            scanf("%s%d",c,&pos);
            if(c[0]=='B')
            {
                mt = abs(pos-pb);
                pb = pos;
                if(mt>(lt-tb)) mt -= lt-tb;
                else mt = 0;
                tb = lt+mt+1;
            }
            else {
                mt = abs(pos-po);
                po = pos;
                if(mt>(lt-to)) mt -= lt-to;
                else mt = 0;
                to = lt+mt+1;
            }
            lt = max(to,tb);
            //printf("%d\n",lt);
        }
        printf("Case #%d: %d\n",ca++,lt);
    }
	return 0;
}
