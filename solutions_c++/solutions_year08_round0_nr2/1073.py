#include <stdio.h>
#include <algorithm>
using namespace std;


struct stamp
{
    int time, type, pos;
} times[500];
int tn;

int cmp(const stamp& a, const stamp& b)
{
    if (a.time!=b.time) return a.time<b.time;
    if (a.type!=b.type) return a.type>b.type;
    return a.pos<b.pos;
}
int main()
{
    int ca, cas=0, t, na, nb, a, b, c, d, i;
    int trains[2], inits[2];
    freopen("B-large.in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d", &ca);
    while (ca--)
    {
        scanf("%d", &t);
        scanf("%d%d", &na, &nb);
        for (tn=i=0;i<na;++i)
        {
            scanf("%d:%d %d:%d",&a, &b, &c, &d);
            times[tn].time=a*60+b;
            times[tn].type=0;
            times[tn].pos=0;
            ++tn;
            times[tn].time=c*60+d+t;
            times[tn].type=1;
            times[tn].pos=1;
            ++tn;            
        }
        for (i=0;i<nb;++i)
        {
            scanf("%d:%d %d:%d",&a, &b, &c, &d);
            times[tn].time=a*60+b;
            times[tn].type=0;
            times[tn].pos=1;
            ++tn;
            times[tn].time=c*60+d+t;
            times[tn].type=1;
            times[tn].pos=0;
            ++tn;   
        }
        sort(times, times+tn, cmp);
        trains[0]=trains[1]=inits[0]=inits[1]=0;
        for (i=0;i<tn;++i)
        if (times[i].type==0)
        {
            if (trains[times[i].pos]==0) inits[times[i].pos]++; else
            trains[times[i].pos]--;
        } else
        {
            trains[times[i].pos]++;
        }
        printf("Case #%d: %d %d\n",++cas, inits[0], inits[1]);        
    }
    return 0;
}
