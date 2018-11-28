#include <iostream>
#include <set>
using namespace std;
multiset <int> s[2];
multiset <int>::iterator tmps; 
struct route
{
    int dep,arr;
    int x,y;
}train[200];
int cmp(const void *a,const void *b)
{
    route *p,*q;
    p=(route *)a;
    q=(route *)b;
    if (p->dep==q->dep) return p->arr-q->arr;
    else return p->dep-q->dep;
}
int an,bn,cn,n,t;
int ans[2];
int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);

    int nt,i,j,k,h1,h2,m1,m2;
    scanf("%d",&n);
    for (nt=1;nt<=n;nt++)
    {
        scanf("%d%d%d",&t,&an,&bn);
        cn=an+bn;
        for (i=0;i<an;i++)
        {
            scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
            train[i].dep=h1*60+m1;
            train[i].arr=h2*60+m2+t;
            train[i].x=0; train[i].y=1;
        }
        for (i=an;i<cn;i++)
        {
            scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
            train[i].dep=h1*60+m1;
            train[i].arr=h2*60+m2+t;
            train[i].x=1; train[i].y=0;
        }
        ans[0]=0; ans[1]=0;
        s[0].clear(); s[1].clear();
        qsort(train,cn,sizeof(route),cmp);
        /*cout<<endl;
        for (i=0;i<cn;i++)
            cout<<train[i].dep/60<<':'<<train[i].dep%60
            <<' '<<train[i].arr/60<<':'<<train[i].arr%60<<endl;*/
        for (i=0;i<cn;i++)
        {
            tmps=s[train[i].x].upper_bound(train[i].dep);
            if (tmps!=s[train[i].x].begin())
            {
                tmps--;
                s[train[i].x].erase(tmps);
                s[train[i].y].insert(train[i].arr);
            }
            else
            {
                s[train[i].y].insert(train[i].arr);
                ans[train[i].x]++;
            }
        }
        cout<<"Case #"<<nt<<": "<<ans[0]<<' '<<ans[1]<<endl;
    }
    //system("pause");
    return 0;
}
