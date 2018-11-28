#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;
int op,bp,ot,bt;
int n,t;
char c[2];
int pos;
int mt,lt;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,cases = 1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        op = 1;
        bp = 1;
        ot = 0;
        bt = 0;
        lt = max(ot,bt);
        for(i=0;i<n;i++)
        {
            scanf("%s%d",c,&pos);
            if(c[0]=='B')
            {
                mt = abs(pos-bp);
                bp = pos;
                if(mt>(lt-bt)) mt -= lt-bt;
                else mt = 0;
                bt = lt+mt+1;
            }
            else {
                mt = abs(pos-op);
                op = pos;
                if(mt>(lt-ot)) mt -= lt-ot;
                else mt = 0;
                ot = lt+mt+1;
            }
            lt = max(ot,bt);
        }
        printf("Case #%d: %d\n",cases++,lt);
    }
	return 0;
}
