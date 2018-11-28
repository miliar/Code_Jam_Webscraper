#include<stdio.h>
#include<algorithm>
using namespace std;

struct Time
{
    int hh,mm;
};

struct Train
{
    Time beg,end;
}a[110],b[110];

void add(Time& tim,int t)
{
    tim.mm+=t;
    if(tim.mm>=60)
    {
        tim.mm-=60;
        tim.hh++;
    }
}

bool operator<(Time t1,Time t2)
{
    if(t1.hh==t2.hh)
        return t1.mm<t2.mm;
    return t1.hh<t2.hh;
}
bool operator<=(Time t1,Time t2)
{
    if(t1.hh==t2.hh)
        return t1.mm<=t2.mm;
    return t1.hh<t2.hh;
}

bool pr1(Train tr1,Train tr2)
{
    return tr1.beg<tr2.beg;
}
bool pr2(Train tr1,Train tr2)
{
    return tr1.end<tr2.end;
}

int n1,i1,t,na,nb,i,pos,che1,che2;

int main()
{
    scanf("%d",&n1);
    for(i1=1;i1<=n1;i1++)
    {
        scanf("%d",&t);
        scanf("%d %d",&na,&nb);
        for(i=1;i<=na;i++)
        {
            scanf("%d:%d %d:%d",&a[i].beg.hh,&a[i].beg.mm,&a[i].end.hh,&a[i].end.mm);
            add(a[i].end,t);
        }
        for(i=1;i<=nb;i++)
        {
            scanf("%d:%d %d:%d",&b[i].beg.hh,&b[i].beg.mm,&b[i].end.hh,&b[i].end.mm);
            add(b[i].end,t);
        }
        sort(a+1,a+1+na,pr1);
        sort(b+1,b+1+nb,pr2);
        pos=1;che1=0;
        for(i=1;i<=na;i++)
        {
            if(pos>nb)
            {
                che1++;
                continue;
            }   
            if(b[pos].end<=a[i].beg)
                pos++;
            else
                che1++;
        }
        sort(a+1,a+1+na,pr2);
        sort(b+1,b+1+nb,pr1);
        pos=1;che2=0;
        for(i=1;i<=nb;i++)
        {
            if(pos>na)
            {
                che2++;
                continue;
            }   
            if(a[pos].end<=b[i].beg)
                pos++;
            else
                che2++;
        }
        printf("Case #%d: %d %d\n",i1,che1,che2);
    }
    return 0;
}
