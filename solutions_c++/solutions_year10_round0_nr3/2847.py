#include <stdio.h>
#include <string.h>
#include <list>
#include <vector>
using namespace std;
list<int> lst,lst0;
int _sum;
list<int> run(list<int> a,int k)
{
    int i,j;
    list<int> b;
    list<int> c;
    list<int>::iterator it;
    int sum=0;
    for(it=a.begin();it!=a.end();)
    {
        if(sum+ *it>k  ) break;
        else
        {
            sum+=*it;
            c.push_back(*it);
            it++;
            a.erase( a.begin() );
        }
    }
    for(it=a.begin();it!=a.end();it++)
    {
        b.push_back(*it);
    }
    for(it=c.begin();it!=c.end();it++)
    {
        b.push_back(*it);
    }
    _sum+=sum;
    return b;
}
void prt(list<int> a)
{
    list<int>::iterator it;
    for(it=a.begin();it!=a.end();it++)
    {
        printf("<%d>",*it);
    }
    printf("\n");
}
int equal(list<int> a,list<int> b)
{
    if(   a.size()!=b.size()   ) return 0;
     list<int>::iterator it,it2;
    for(it=a.begin(),it2=b.begin();it!=a.end();it++,it2++)
    {
        if(  *it  !=  *it2) return 0;
    }
    return 1;
}
int mymin(int a,int b)
{
    return a<b?a:b;
}
int main()
{
    freopen("c:\\xxx.in","r",stdin);
    freopen("c:\\yyy.txt","w",stdout);
    int i,j;
    int cas;
    scanf("%d",&cas);
    for(int u=1;u<=cas;u++)
    {
        lst0.clear();
        lst.clear();
        int r,k,n;
        scanf("%d%d%d",&r,&k,&n);

        vector<list<int> > pres;
        vector<int> presums;
        for(i=0;i<n;i++)
        {
            int a;
            scanf("%d",&a);
            lst.push_back(a);
            lst0.push_back(a);
        }
        //prt(lst);

        pres.push_back(lst);
        presums.push_back(0);
        _sum=0;
        int begin;
        int mod;
        for(i=1;;i++)
        {
            lst=run(lst,k);
            //prt(lst);
            /*

            prt(lst0);
            printf("\n");
            getchar();*/


            for(j=0;j<pres.size();j++)
            {
                if(equal(lst,pres[j])  )
                {
                begin=j;
                 mod=i-j;
                goto line1;
                }
            }
            presums.push_back(_sum);
            pres.push_back(lst);
        }
        line1:;
        int sum0=_sum-presums[begin];
        int res=0;

        //printf("<mod:%d>n",mod);

        _sum=0;
        lst=lst0;
        for(i=0;i<mymin (begin,r  );i++)
        {
            lst=run(lst,k);
        }
        res+=_sum;
            //printf("<sum0:%d>",sum0);
            //printf("<%d,%d>",res ,begin );
        r=r-begin;
        if(r>=0)
        {
            res+=sum0*(r/mod);
            lst=pres[begin];
            //printf("[[%d]",res);
            _sum=0;
            for(i=0;i<r%mod;i++)
            {
                lst=run(lst,k);
            }
            res+=_sum;


            //printf("[%d]\n",res);
        }
        else
        {
                //printf("[%d]\n",res);
        }
        printf("Case #%d: %d\n",u,res);
    }






    return 0;
}
