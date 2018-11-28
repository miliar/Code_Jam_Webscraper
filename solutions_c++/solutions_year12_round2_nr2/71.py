#include <cstdio>
#include <cstring>
#include <cmath>

#include <algorithm>
#include <iostream>

using namespace std;

typedef long long LL;
typedef double db;

const db oo = 1e100;
const int Max = 128;
const int MaxD = 10010;

int mv[4][2] = {{-1,0},{0,1},{1,0},{0,-1}};
int H,N,M,C[Max][Max],F[Max][Max];
int Q[MaxD],Heap[MaxD],id[MaxD],hn;
db dis[MaxD];

bool valid(int nx,int ny){
    return  0 <= nx && nx < N &&
            0 <= ny && ny < M;
}
bool passable(int x,int y,int nx,int ny){
    int d = max(F[x][y],F[nx][ny]);
    if (d + 50 > C[nx][ny]) return false;
    if (F[nx][ny] + 50 > C[x][y]) return false;
    return true;
}
bool near(int x,int y){
    return dis[x] < dis[y];
}
void sink(int p){
    int q = p << 1,r = Heap[p];
    while (q <= hn){
        if (q < hn)
            q += near(Heap[q+1],Heap[q]);
        if (near(r,Heap[q]))
            break;
        id[Heap[p] = Heap[q]] = p;
        p = q,q <<= 1;
    }
    id[Heap[p] = r] = p;
}
void swim(int q){
    int p = q >> 1,r = Heap[q];
    while (p && near(r,Heap[p])){
        id[Heap[q] = Heap[p]] = q;
        q = p,p >>= 1;
    }
    id[Heap[q] = r] = q;
}
int delMin(){
    if (hn == 0) return -1;
    int x = Heap[1];
    id[Heap[1] = Heap[hn--]] = 1;
    sink(1);
    return x;
}
void dealElmt(int x,int f){
//    printf("deal %d %d\n",x,f);
    if (f == 0)//insert
        swim(id[Heap[++hn] = x] = hn);
    else if (f == 1){//remove
        if (id[x] < hn){
            int d = Heap[hn--];
            id[Heap[id[x]] = d] = id[x];
            sink(id[x]);
            swim(id[x]);
        }else
            --hn;
    }else if (f == 2){//update
        sink(id[x]);
        swim(id[x]);
    }else{//error
        while (1);
    }
}

int main(){
    freopen("W:\\B-small-attempt0.in","r",stdin);
    freopen("W:\\B-small-attempt0.out","w",stdout);
    int tCase;
    scanf("%d",&tCase);
    for (int ct = 1;ct <= tCase;ct++){
        scanf("%d%d%d",&H,&N,&M);
        for (int i = 0;i < N;i++)
            for (int j = 0;j < M;j++)
                scanf("%d",&C[i][j]);
        for (int i = 0;i < N;i++)
            for (int j = 0;j < M;j++)
                scanf("%d",&F[i][j]);
        int td = N * M;
        for (int i = 0;i < td;i++)
            dis[i] = oo;
        int qn = 0;
        dis[Q[qn++] = 0] = 0;
        hn = 0;
        for (int q = 0;q < qn;q++){
            int s = Q[q];
            int x = s / M,y = s % M;
            dealElmt(s,0);
            for (int k = 0;k < 4;k++){
                int nx = x + mv[k][0];
                int ny = y + mv[k][1];
                if (valid(nx,ny) &&
                    passable(x,y,nx,ny) &&
                    H + 50 <= C[nx][ny]){
                    int ns = nx * M + ny;
                    if (dis[ns] > oo / 2)
                        dis[Q[qn++] = ns] = 0;
                }
            }
        }
//        printf("time goes...\n");
        while (hn > 0){
            int s = delMin();
            int x = s / M,y = s % M;
            db t = dis[s];
            db h = max(H - t * 10.0,0.0);
            for (int k = 0;k < 4;k++){
                int nx = x + mv[k][0];
                int ny = y + mv[k][1];
                if (valid(nx,ny) &&
                    passable(x,y,nx,ny)){
                    db mh = C[nx][ny] - 50.0;
                    db nt = t + (mh < h ? (h - mh) / 10.0 : 0.0) + 1.0;
                    mh = min(mh,h);
                    if (mh < F[x][y] + 20.0) nt += 9.0;
                    int ns = nx * M + ny;
                    if (dis[ns] > oo / 2){
                        dis[ns] = nt;
                        dealElmt(ns,0);
                    }else if (nt < dis[ns]){
                        dis[ns] = nt;
                        dealElmt(ns,2);
                    }
                }
            }
        }
        printf("Case #%d: %.10f\n",ct,dis[td - 1]);
    }
    return 0;
}
