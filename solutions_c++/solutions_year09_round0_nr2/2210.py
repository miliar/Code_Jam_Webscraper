#include<iostream>
using namespace std;
int cases,m,n;
struct Point
{
       int x,y,val,pre,mark;
}p[10001];
struct Sink
{
       int x,y;
       char mark;
}que[30];
int dir[101][101];
bool use[101][101];
int cmp1(const void *a,const void *b)
{
    return ((Point*)a)->val>((Point*)b)->val?-1:1;
}
int cmp2(const void *a,const void *b)
{
    Sink *p=(Sink*)a,*q=(Sink*)b;
    if(p->y!=q->y)
    return p->y>q->y?1:-1;
    else
    return p->x>q->x?1:-1;
}
int get(int n)
{
    //cout<<"    "<<n<<endl;system("pause");
    if(p[n].pre==n)
    return n;
    p[n].pre=get(p[n].pre);
    return p[n].pre;
}
int main()
{
    scanf("%d",&cases);
    int temp=0;
    while(temp<cases)
    {
        memset(use,0,sizeof(use));
        temp++;
        int v;
        int tt=0;
        scanf("%d%d",&m,&n);
        for(int i=1;i<=m;i++)
        for(int j=1;j<=n;j++)
        {
            scanf("%d",&v);
            p[tt].x=i;
            p[tt].y=j;
            p[tt].val=v;
            tt++;
        }
        qsort(p,tt,sizeof(p[0]),cmp1);
        for(int i=0;i<tt;i++)
        dir[p[i].x][p[i].y]=i,p[i].pre=i;
      /*  for(int i=1;i<=m;i++)
        {
             for(int j=1;j<=n;j++)
             {
                 if(j!=1)
                 printf(" ");
                 printf("%d",dir[i][j]);
             }
             printf("\n");
        }*/
        for(int i=0;i<tt;i++)
        {
             int temp=p[i].val;
             if(p[i].x>1&&temp>p[dir[p[i].x-1][p[i].y]].val)
             {
                 temp=p[dir[p[i].x-1][p[i].y]].val;
                 p[i].pre=dir[p[i].x-1][p[i].y];
             }
             if(p[i].y>1&&temp>p[dir[p[i].x][p[i].y-1]].val)
             {
                 temp=p[dir[p[i].x][p[i].y-1]].val;
                 p[i].pre=dir[p[i].x][p[i].y-1];
             }
             if(p[i].y<n&&temp>p[dir[p[i].x][p[i].y+1]].val)
             {
                 temp=p[dir[p[i].x][p[i].y+1]].val;
                 p[i].pre=dir[p[i].x][p[i].y+1];
             }
             if(p[i].x<m&&temp>p[dir[p[i].x+1][p[i].y]].val)
             {
                 temp=p[dir[p[i].x+1][p[i].y]].val;
                 p[i].pre=dir[p[i].x+1][p[i].y];
             }
        }
        int nn=0;
        for(int i=0;i<tt;i++)
        {
             if(p[i].pre==i)
             {
                 que[nn].x=p[i].x;
                 que[nn].y=p[i].y;
                 nn++;
             }
        }
      /*  qsort(que,nn,sizeof(que[0]),cmp2);
        for(int i=0;i<nn;i++)
        p[dir[que[i].x][que[i].y]].mark='a'+i;*/
        printf("Case #%d:\n",temp);
        int mm=0;
        for(int i=1;i<=m;i++)
        {
            for(int j=1;j<=n;j++)
            {
                if(j!=1)
                printf(" ");
                int q=get(dir[i][j]);
                if(!use[p[q].x][p[q].y])
                {
                    use[p[q].x][p[q].y]=true;
                    p[q].mark='a'+mm;
                    mm++;
                }
              //  cout<<q<<endl;
                printf("%c",p[q].mark);
            }
            printf("\n");
        }//system("pause");
    }
}
        
             
