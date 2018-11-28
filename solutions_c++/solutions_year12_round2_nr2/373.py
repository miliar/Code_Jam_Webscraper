#include<cstdio>
const double inf=1e10;
const int dx[4]={0,-1,0,1};
const int dy[4]={-1,0,1,0};
struct node
{
    int x,y;
    double d;
};

node h[20000];
int hn,flo[105][105],cei[105][105];
double dist[105][105];
bool v[105][105],bef[105][105];
            

void shift(int no)
{
    int p,ch;
    node t;
    if (no!=0)
    {
        p=(no-1)/2;
        if (h[p].d>h[no].d)
        {
            t=h[p];h[p]=h[no];h[no]=t;
            shift(p);
            return;
        }
    }
    if (no*2+1<=hn) ch=no*2+1; else return;
    if (no*2+2<=hn)
    {
        if (h[no*2+2].d<h[ch].d) ch=no*2+2;
    }
    if (h[no].d>h[ch].d)
    {
        t=h[ch];h[ch]=h[no];h[no]=t;
        shift(ch);
        return;
    }
    return;
}


int main()
{
    int tst,lp,i,j,n,m,hgt,x,y,nx,ny,th;
    double time,w;
    bool fl,upd;
    
    scanf("%d",&tst);
    for (lp=0;lp<tst;lp++)
    {
        scanf("%d%d%d",&hgt,&n,&m);
        for (i=0;i<n;i++)
        {
            for (j=0;j<m;j++)
            {
                scanf("%d",&cei[i][j]);
            }
        }
        for (i=0;i<n;i++)
        {
            for (j=0;j<m;j++)
            {
                scanf("%d",&flo[i][j]);
            }
        }
        for (i=0;i<n;i++)
        {
            for (j=0;j<m;j++)
            {
                dist[i][j]=inf;
                bef[i][j]=false;
                v[i][j]=false;
            }
        }
        dist[0][0]=0;
        h[0].x=0;h[0].y=0;h[0].d=0;hn=0;
        bef[0][0]=true;
        while (hn>=0)
        {
            x=h[0].x;y=h[0].y;
            h[0]=h[hn];
            hn--;
            shift(0);
            if (v[x][y]==true) continue;
            v[x][y]=true;            
            for (i=0;i<4;i++)
            {
                nx=x+dx[i];ny=y+dy[i];
                if (nx<0||nx>=n||ny<0||ny>=m) continue;
                th=cei[nx][ny]-50;
                if (flo[x][y]>th||flo[nx][ny]>th||flo[nx][ny]>cei[x][y]-50) continue;
                fl=false;
                if (hgt<th)
                {
                    time=0;
                    fl=true;
                } else time=(double)(hgt-th)/10;
                if (time<dist[x][y]) time=dist[x][y];
                fl=fl&bef[x][y];
                upd=false;
                if (fl==true)
                {
                    bef[nx][ny]=true;
                    dist[nx][ny]=0;
                    upd=true;
                } else {
                    bef[nx][ny]=false;
                    if (hgt-time*10>=flo[x][y]+20-1e-6) w=1; else w=10;
                    if (time+w<dist[nx][ny])
                    {
                        dist[nx][ny]=time+w;
                        upd=true;
                    }
                }
                if (upd==true)
                {
                    hn++;
                    h[hn].x=nx;h[hn].y=ny;h[hn].d=dist[nx][ny];
                    shift(hn);
                }
            }
        }
        printf("Case #%d: %.1f\n",lp+1,dist[n-1][m-1]);
    }
    return 0;
}
            
