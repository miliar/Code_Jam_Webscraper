#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdio>

using namespace std;

int bj,ti,tn,len,ln,i,j,x,cn,dn,op[102][102],cb[102][102],a[102];
char ch1,ch2,ch3;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&tn);
    for (ti = 1; ti <= tn; ti++)
    {
        memset(cb,255,sizeof(cb));
        memset(op,0,sizeof(op));
        memset(a,0,sizeof(a));
        len = 0;
        scanf("%d",&cn);
        for (i = 1; i <= cn; i++)
        {
            scanf(" %c%c%c",&ch1,&ch2,&ch3);
            cb[ch1-64][ch2-64] = ch3-64;
            cb[ch2-64][ch1-64] = ch3-64;
        }
        scanf("%d",&dn);
        for (i = 1; i <= dn; i++)
        {
            scanf(" %c%c",&ch1,&ch2);
            op[ch1-64][ch2-64] = 1;
            op[ch2-64][ch1-64] = 1;
        }
        scanf("%d",&ln);
        scanf(" %c",&ch1);
        a[++len] = ch1-64;
        for (i = 2; i <= ln; i++)
        {
            scanf("%c",&ch1);
            a[++len] = ch1-64;
            bj = 0;
            if (len >= 2 && cb[a[len]][a[len-1]] != -1)
            {
                x = cb[a[len]][a[len-1]];
                len--;
                a[len] = x;
                bj = 1;
            }
            if (bj == 0)
            {   for (j = 1; j <= len-1; j++)
                    if (op[a[j]][a[len]] == 1)
                    {
                        len = 0;
                        break;
                    }
            }
        }
        scanf("\n");

        printf("Case #%d: [",ti);
        for (i = 1; i <= len; i++)
        {
            if (i == 1) printf("%c",(char)a[i]+64);
            else printf(", %c",(char)a[i]+64);
        }
        printf("]\n");
    }

}
