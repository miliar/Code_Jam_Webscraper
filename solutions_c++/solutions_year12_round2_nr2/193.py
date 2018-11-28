#include <stdio.h>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <stdlib.h>
#include <time.h>
#include <string>
#include <iostream>
#include <queue>
#define EPS 1e-10
#define oo 1e20
using namespace std;
int H,N,M;
int F[102][102];
int C[102][102];

double getmovetime(double water_level, int posx,int posy, int nx, int ny)
{
    if(!(F[posx][posy]<=C[nx][ny]-50 && F[nx][ny]<=C[nx][ny]-50))
        return oo;
    if(!(F[nx][ny]<=C[posx][posy]-50))
        return oo;
    double reqd_waterlevel_to_move = C[nx][ny]-50;
    //printf("%lf %lf\n",water_level, reqd_waterlevel_to_move);
    double min_time_for_movement = max(0.0,(-reqd_waterlevel_to_move + water_level)/10.0);
    double water_level_at_movement = water_level - 10 * min_time_for_movement;
    if(water_level_at_movement >= 20 + F[posx][posy]-EPS)
        return min_time_for_movement + 1.0;
    else
        return min_time_for_movement + 10.0;
}


int dx[]={-1,1,0,0};
int dy[]={0,0,-1,1};
struct pqitem
{
    int posx;
    int posy;
    double curr_time;
    bool operator<(const pqitem &b) const{
        return curr_time>b.curr_time;
    }
};
double min_time[102][102];

void dfs(int posx,int posy)
{
    min_time[posx][posy]=0;
    for(int d=0;d<4;d++)
    {
        int nx = posx+dx[d];
        int ny = posy+dy[d];
        if(nx <=0 || nx >=N+1 || ny<=0 || ny>=M+1)
            continue;
        if(!(F[posx][posy]<=C[nx][ny]-50 && F[nx][ny]<=C[nx][ny]-50))
            continue;
        if(!(F[nx][ny]<=C[posx][posy]-50))
            continue;
        if(!(H<=C[nx][ny]-50))
            continue;
        if(min_time[nx][ny]>oo/2)
            dfs(nx,ny);
    }
}

double solve()
{
    for(int i=1;i<=N;i++)
        for(int j=1;j<=M;j++)
            min_time[i][j]=oo;
    
    dfs(1,1);
    
    
    priority_queue<pqitem> q;
    for(int i=1;i<=N;i++)
        for(int j=1;j<=M;j++)
            if(min_time[i][j]==0)
                q.push((pqitem){i,j,0});
    while(!q.empty())
    {
        pqitem cur = q.top();
        q.pop();
        int posx=cur.posx;
        int posy=cur.posy;
        double curr_time = cur.curr_time;
        //printf("%d %d %lf\n",posx,posy,curr_time);
        double water_level = max(0.0,(double)H-curr_time*10.0);
        
        for(int d=0;d<4;d++)
        {
            int nx = posx+dx[d];
            int ny = posy+dy[d];
            if(nx <=0 || nx >=N+1 || ny<=0 || ny>=M+1)
                continue;
            double move_time = getmovetime(water_level, posx, posy, nx, ny);
            if(min_time[nx][ny] > curr_time+move_time && move_time <= oo/2)
            {
                q.push((pqitem){nx,ny,curr_time+move_time});
                min_time[nx][ny] = curr_time + move_time;
            }
        }
    }
    return min_time[N][M];
    
}


int main()
{
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        scanf("%d%d%d",&H,&N,&M);
        for(int i=1;i<=N;i++)
            for(int j=1;j<=M;j++)
                scanf("%d",&C[i][j]);
        for(int i=1;i<=N;i++)
            for(int j=1;j<=M;j++)
                scanf("%d",&F[i][j]);
        
        printf("Case #%d: %1.10f\n",t,solve());
        
    }
}