#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

class node
{
    public:
    int a,b;
    int ind;
};

node s[1005];
bool vis[2][1005];
node s1[1005],s2[1005];

bool cmp1 (node a , node b)
{
    if( a.a != b.a ) return a.a < b.a;
    return a.b > b.b;
}

bool cmp2 (node a , node b)
{
    if( a.b != b.b ) return a.b < b.b;
    return a.a < b.a;
}

int main ()
{
    FILE *in = fopen ("B.in","r");
    FILE *out = fopen ("B.out","w");

    int t;
    int k = 1;

    fscanf (in,"%d",&t);

    while( t -- )
    {
        int n;

        memset (vis,0,sizeof(vis));

        fscanf (in,"%d",&n);

        for (int i=0; i<n; i++)
        {
            s[i].ind = i;
            fscanf (in,"%d %d",&s[i].a,&s[i].b);

            s1[i].ind = s2[i].ind = i;
            s1[i].a = s2[i].a = s[i].a;
            s1[i].b = s2[i].b = s[i].b;
        }

        sort( s1,s1+n,cmp1 );
        sort( s2,s2+n,cmp2 );

        int star = 0;
        int ret = 0;

        int cnt = 0;
        int tar = 0;

        for (int i=0; i<n; i++)
        {
            if (s2[i].b <= star)
            {
                if (vis[0][s2[i].ind] == 1) star ++;
                else star += 2;
                ret ++;
                vis[1][s2[i].ind] = 1;
            }
            else
            {
                int c;
                for (c=cnt; c<n && star<s2[i].b; c++)
                {
                    if (s1[c].a <= star)
                    {
                        if (vis[1][s1[c].ind] == 1) continue;
                        star ++;
                        ret ++;
                        vis[0][s1[c].ind] = 1;
                    }
                }
                cnt = c;

                if (star < s2[i].b)
                {
                    ret = 1<<30;
                    break;
                }

                i --;
            }
        }

        fprintf (out,"Case #%d: ",k);
        k ++;

        if (ret == 1<<30) fprintf (out,"Too Bad\n");
        else fprintf (out,"%d\n",ret);
    }
}
