#include<iostream>
using namespace std;
const int MAXN=1010;
const int INFI=2000100;
int x1[MAXN],x2[MAXN],y1[MAXN],y2[MAXN],g_c;
bool visted[MAXN];
void reader()
{
    int i,xx1,xx2,yy1,yy2;
    scanf("%d",&g_c);
    for(i=0;i<g_c;i++)
    {
        scanf("%d%d%d%d",&xx1,&yy1,&xx2,&yy2);
        x1[i]=min(xx1,xx2);
        x2[i]=max(xx1,xx2);
        y1[i]=min(yy1,yy2);
        y2[i]=max(yy1,yy2);
    }
}
inline bool near(int i,int j)
{
    if(x1[i]>x2[j]+1||x1[j]>x2[i]+1||
        y1[i]>y2[j]+1||y1[j]>y2[i]+1)
            return false;
    if((x1[i]==x2[j]+1&&y1[i]==y2[j]+1)||
        (x1[j]==x2[i]+1&&y1[j]==y2[i]+1))
            return false;
    return true;
}
void dfs(int node,int &minxy,int &maxx,int &maxy)
{
    visted[node]=true;
    minxy=min(minxy,x1[node]+y1[node]);
    maxx=max(maxx,x2[node]);
    maxy=max(maxy,y2[node]);
    for(int i=0;i<g_c;i++)
    {
        if(visted[i]==false&&near(node,i))
        {
            dfs(i,minxy,maxx,maxy);
        }
    }
}
int work()
{
    int i,res=-INFI;
    memset(visted,0,sizeof(visted));
    for(i=0;i<g_c;i++)
    {
        if(visted[i]==false)
        {
            int maxx=-INFI;
            int maxy=-INFI;
            int minxy=INFI;
            dfs(i,minxy,maxx,maxy);
            int t=maxx+maxy+1-minxy;
            res=max(res,t);
        }
    }
    return res;
}
int main()
{
    int t;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        reader();
        printf("Case #%d: %d\n",cas,work());
    }
    return 0;
}
