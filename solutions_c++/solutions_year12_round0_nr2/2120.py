#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

const int maxn=1005;

int a[maxn];

int n,s,p,t;
int ans,cc=0;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int num;
    scanf("%d",&t);
    while (t--)
    {
        scanf("%d%d%d",&n,&s,&p);
        ans=0;
        for (int i=1;i<=n;i++)
        {
            scanf("%d",&num);
            if (num%3==1)
            {
                int k=num/3;
                if (k+1 >= p) ans++;
            }
            else if (num%3==2)
            {
                int k=num/3;
                if (k + 1 >= p) ans++;
                else if (k + 2 >= p && s > 0)
                {
                    s--;
                    ans++;
                }
            }
            else if (num%3==0)
            {
                int k=num/3;
                if (k >= p) ans++;
                else
                {
                    if (k-1 >= 0 && k+1 >= p && s > 0)
                    {
                        s--;
                        ans++;
                    }
                }
            }
        }
        printf("Case #%d: %d\n",++cc,ans);
    }
    return 0;
}

/*
10
5 2 8
29 20 8 18 18 21

*/


/*
#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int c[30];

void init()
{
    c[0]=24;
    c[1]=7;
    c[2]=4;
    c[3]=18;
    c[4]=14;
    c[5]=2;
    c[6]=21;
    c[7]=23;
    c[8]=3;
    c[9]=20;
    c[10]=8;
    c[11]=6;
    c[12]=11;
    c[13]=1;
    c[14]=10;
    c[15]=17;
    c[16]=25;
    c[17]=19;
    c[18]=13;
    c[19]=22;
    c[20]=9;
    c[21]=15;
    c[22]=5;
    c[23]=12;
    c[24]=0;
    c[25]=16;
}

char s[1000];
int cc=0;

int main()
{
    init();
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int t;
    scanf("%d",&t);
    gets(s);
    while (t--)
    {
        gets(s);
        printf("Case #%d: ",++cc);
        int l=strlen(s);
        for (int i=0;i<l;i++)
            if (s[i]==' ') printf(" ");
            else printf("%c",c[s[i]-'a']+'a');
        puts("");
    }
    return 0;
}
*/
