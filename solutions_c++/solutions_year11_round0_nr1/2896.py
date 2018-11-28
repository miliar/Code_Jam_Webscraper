#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <cmath>
#include <math.h>
using namespace std;
int T,n;
struct pos
{
    char r;
    int p;
};
vector<pos> R;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    for (int ca=1;ca<=T;ca++)
    {
        R.clear();
        int i,j;
        scanf("%d",&n);
        for (i=0;i<n;i++)
        {
            char a;
            int b;
            cin>>a>>b;
            //scanf("%s %d",&a,&b);
            pos t;
            t.r=a;
            t.p=b;
            R.push_back(t);
            //printf("%c %d\n",a,b);
        }
        int pb=1,po=1,cntb=0,cnto=0;
        int timeb=0,timeo=0;
        for (i=0;i<R.size();i++)
        {
            if (R[i].r=='B')
            {
                int Dis=fabs(pb-R[i].p);
                pb=R[i].p;
                if (timeb+Dis<timeo)
                    timeb=timeo+1;
                else
                    timeb+=Dis+1;
            }
            else
            {
                int Dis=fabs(po-R[i].p);
                po=R[i].p;
                if (timeo+Dis<timeb)
                    timeo=timeb+1;
                else
                    timeo+=Dis+1;
            }
        }
        printf("Case #%d: %d\n",ca,max(timeo,timeb));
    }
    return 0;
}
