#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<ctime>
#include<algorithm>
#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<set>
using namespace std;
struct nima
{
    int d,l;
    bool operator < (const nima &b) const
    {
        return d<b.d;
    }
}cao[10010];
struct node
{
    int id,l;
    node(int _id=0,int _l=0): id(_id),l(_l) {}
};
int main()
{
    freopen("C:\\Users\\James\\Desktop\\in.txt","r",stdin);freopen("C:\\Users\\James\\Desktop\\out.txt","w",stdout);
    int T,cas=0;
    scanf("%d",&T);
    while(T--)
    {
        int n;
        scanf("%d",&n);
        for(int i=1;i<=n;i++)
        scanf("%d %d",&cao[i].d,&cao[i].l);
        sort(cao+1,cao+1+n);
        int D;
        scanf("%d",&D);
        queue <node> Q;
        while(!Q.empty())Q.pop();
        Q.push(node(1,cao[1].d));
        bool ok=0;
        while(!Q.empty())
        {
            node temp=Q.front();
            Q.pop();
            if(cao[temp.id].d+temp.l>=D)
            {
                ok=1;
                break;
            }
            for(int i=temp.id+1;i<=n;i++)
            {
                if(cao[temp.id].d+temp.l<cao[i].d)continue;
                int x=cao[i].d-cao[temp.id].d;
                x=min(x,cao[i].l);
                Q.push(node(i,x));
            }
        }
        printf("Case #%d: ",++cas);
        if(ok)
        puts("YES");
        else
        puts("NO");
    }
}
