#include <cstdio>
#include <map>
#include <set>
#include <vector>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <fstream>
#include <queue>
#include <list>
#include <cstring>
#define FOR(i,a,n) for(int i=a;i<=n;i++)
#define REP(i,n) for (int i=0;i<n;i++)
#define FORD(i,n,a) for(int i=n;i>=a;i--)
#define PB push_back
#define MP make_pair
#define xx first
#define yy second
#define Min(a,b) a<b ? a:b
#define Max(a,b) a>b ? a:b
#define p2(a) ((a)*(a))
#define ALL(v) v.begin(),v.end()
using namespace std;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef double dd;

int mapa[110][110][4];
int dir[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
int n,xs,ys;

void readmap(void){
    memset(mapa,0,sizeof(mapa));
    REP(i,ys+2)
        REP(j,xs+2)
            mapa[i][j][0]=100000;
    FOR(i,1,ys)
        FOR(j,1,xs)
            scanf("%d",&mapa[i][j][0]);
}
void compute(int y,int x){
    int mn=mapa[y][x][0];
    mapa[y][x][1]=y;
    mapa[y][x][2]=x;
    REP(d,4){
        int yy=y+dir[d][0],xx=x+dir[d][1];
        if(mapa[yy][xx][0]<mn){
            mapa[y][x][1]=yy;
            mapa[y][x][2]=xx;
            mn=mapa[yy][xx][0];
        }
    }
}
    
void neighbours(void){
    FOR(i,1,ys)
        FOR(j,1,xs)
            compute(i,j);
}
int cnt;
int find(int y,int x){
    if(mapa[y][x][3]!=0)
        return mapa[y][x][3];
    if(mapa[y][x][1]==y && mapa[y][x][2]==x){
        if(mapa[y][x][3]==0)
            mapa[y][x][3]=cnt++;
        return mapa[y][x][3];
    }
    mapa[y][x][3]=find(mapa[y][x][1],mapa[y][x][2]);
    return mapa[y][x][3];
}
void printmap(void){
    cnt=1;
    FOR(i,1,ys){
        FOR(j,1,xs){
            int p=find(i,j);
            printf("%c ",(char)((int)'a'+p-1));
        }
        printf("\n");
    }
}

int main(){
    scanf("%d",&n);
    REP(i,n){
        scanf("%d %d",&ys,&xs);
        readmap();
        neighbours();
        printf("Case #%d:\n",i+1);
        printmap();
    }
    return 0;
}
