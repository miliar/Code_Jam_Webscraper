#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <cmath>
#include <math.h>
using namespace std;
#define M 105
int ca,T;
int c,d,n;
bool ck[M];
string C,D;
char N[M];
int main()
{
    freopen("B-small-attempt2.in","r",stdin);
    freopen("B-small-attempt2.out","w",stdout);
    scanf("%d",&T);
    for (int ca=1;ca<=T;ca++)
    {
        int i,j;
        memset(N,0,sizeof(N));
        C="";D="";
        memset(ck,0,sizeof(ck));
        cin>>c;
        if (c) cin>>C;
        //for (i=0;i<c;i++)
        //    cin>>C[i];
        cin>>d;
        if (d) cin>>D;
        //for (i=0;i<d;i++)
        //    cin>>D[i];
        cin>>n;
        cin>>N;
        string t="";
        for (i=0;i<n;i++)
        {
            int x=-1;
            for (j=i-1;j>=0;j--) if (!ck[j]) {x=j;break;}
            if (i>0 && x>-1 && ((N[i]==C[0] && N[x]==C[1]) || (N[i]==C[1] && N[x]==C[0])))
            {
                //printf("%d %d!\n",x,i);
                ck[x]=1;
                N[i]=C[2];
            }
            else if (N[i]==D[0])
            {
                for (j=i-1;j>=0;j--)
                {
                    if (N[j]==D[1] && !ck[j])
                    {
                        for (int k=0;k<=i;k++)
                            ck[k]=1;
                    }
                }
            }
            else if (N[i]==D[1])
            {
                for (j=i-1;j>=0;j--)
                {
                    if (N[j]==D[0] && !ck[j])
                    {
                        for (int k=0;k<=i;k++)
                            ck[k]=1;
                    }
                }
            }
        }
        printf("Case #%d: [",ca);
        for (i=0;i<n;i++)
        {
            if (ck[i]) continue;
            t+=N[i];
        }
        if (t.length()) putchar(t[0]);
        for (i=1;i<t.length();i++)
        {
            printf(", %c",t[i]);
        }
        printf("]\n");
    }
    return 0;
}
