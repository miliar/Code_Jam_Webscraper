#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;
const int N=1010;
vector <pair <int,int> > r;
double ans[N][2];
int a[N];
void work(double dx,double dy,double R,double C,bool first)
{
    if (r.empty())
        return;
    vector <int> here;
    int len=r[0].first;
    here.push_back(r[0].second);
    double last=C-r[0].first;
    for (int i=1;i<r.size();i++)
        if (r[i].first<=last)
        {
            last-=r[i].first*2;
            here.push_back(r[i].second);
        }
    for (int i=0;i<here.size();i++)
        for (int j=0;j<r.size();j++)
            if (here[i]==r[j].second)
            {
                r.erase(r.begin()+j);
                break;
            }
    int x=here[0];
    double left=a[x],delta=first?a[x]:2*a[x];
    ans[x][0]=first?dx:dx+a[x];
    ans[x][1]=0;
    for (int i=1;i<here.size();i++)
    {
        x=here[i];
        ans[x][0]=first?dx:dx+a[x];
        ans[x][1]=left+a[x];
        left+=2*a[x];
    }
    work(dx+delta,dy,R-delta,C,false);
}
int main()
{
    int T;
    scanf("%d",&T);
    while (T--)
    {
        int n,R,C;
        scanf("%d%d%d",&n,&R,&C);
        for (int i=1;i<=n;i++)
        {
            int x;
            scanf("%d",&x);
            a[i]=x;
            r.push_back(make_pair(x,i));
        }
        sort(r.begin(),r.end());
        reverse(r.begin(),r.end());
        work(0,0,R,C,true);
        static int id=0;
        printf("Case #%d:",++id);
        for (int i=1;i<=n;i++)
            printf(" %.2f %.2f",ans[i][0],ans[i][1]);
        printf("\n");
    }
    return(0);
}

