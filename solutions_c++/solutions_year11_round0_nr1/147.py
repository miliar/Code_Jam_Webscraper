#include<iostream>
using namespace std;
int l[2],d[2];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int cases,tt,n,t,q,x;
    char ch;
    for (scanf("%d",&cases),tt=0;tt<cases;tt++)
    {
        l[0]=0;
        l[1]=0;
        d[0]=1;
        d[1]=1;
        t=0;
        for (scanf("%d",&n);n;n--)
        {
            scanf("%c",&ch);
            scanf("%c",&ch);
            if (ch=='O') q=0;
            else q=1;
            scanf("%d",&x);
            t=max(t,l[q]+abs(x-d[q]));
            t++;
            l[q]=t;
            d[q]=x;
        }
        printf("Case #%d: %d\n",tt+1,t);
    }
    return 0;
}
