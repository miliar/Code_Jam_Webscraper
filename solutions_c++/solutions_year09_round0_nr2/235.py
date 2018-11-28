#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
#include <cctype>
using namespace std;
const int MAXN=110,INF=(1<<30);

int height[MAXN][MAXN];
char label[MAXN][MAXN];
int basinR[MAXN][MAXN];
int basinC[MAXN][MAXN];
char result[MAXN][MAXN];
int visited[MAXN][MAXN];

int dr[]={-1,0,0,1};
int dc[]={0,-1,1,0};



int H,W;

int valid(int r, int c)
{
    if(r<0||r>=H||c<0||c>=W) return 0;
    return 1;
}

int isSink(int r, int c)
{
    for(int i=-1;i<=1;i++)
    for(int j=-1;j<=1;j++) {
        if(abs(i)+abs(j)!=1) continue;
        if(valid(r+i,c+j)) {
            if(height[r+i][c+j]<height[r][c]) return 0;
        }
    }
    return 1;

}

int ifChooseThis(int r, int c, int sr, int sc)
{
    int smallest=INF;
    for(int i=0;i<4;i++) {
        int nr=r+dr[i],nc=c+dc[i];
        if(!valid(nr,nc)) continue;
        if(height[nr][nc]<height[r][c]) {
            smallest = min(smallest,height[nr][nc]);
        }
    }
    if(smallest==INF) return 0;
    for(int i=0;i<4;i++) {
        int nr=r+dr[i],nc=c+dc[i];
        if(!valid(nr,nc)) continue;
        if(height[nr][nc]==smallest) {
            if(sr==nr&&sc==nc) return 1;
            return 0;
        }
    }
    return 0;
}

void dfs(int r, int c, const int pr, const int pc)
{
    if(visited[r][c]) return ;
    visited[r][c]=1;
    basinR[r][c]=pr;
    basinC[r][c]=pc;

    for(int i=-1;i<=1;i++) for(int j=-1;j<=1;j++) {
        if(abs(i)+abs(j)!=1) continue;
        int nr=r+i,nc=c+j;
        if(!valid(nr,nc)) continue;
        if(ifChooseThis(nr,nc,r,c)) {
            dfs(nr,nc,pr,pc);
        }
    }



}

void putLabel()
{
    for(int i=0;i<H;i++) {
        for(int j=0;j<W;j++) {
            if(isSink(i,j)) {
                memset(visited,0,sizeof(visited));
                dfs(i,j,i,j);
            }
        }
    }
    for(int i=0;i<H;i++) {
        for(int j=0;j<W;j++) {
            label[i][j]=' ';
        }
    }
    char c='a';
    for(int i=0;i<H;i++) {
        for(int j=0;j<W;j++) {
            int br = basinR[i][j];
            int bc = basinC[i][j];
            if(label[br][bc]==' ') {
                label[br][bc]=c;
                c++;
            }
            result[i][j]=label[br][bc];
        }
    }
}

int main()
{

    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    cin>>T;
    for(int tc=1;tc<=T;tc++) {

        cin>>H>>W;

        for(int i=0;i<H;i++)for(int j=0;j<W;j++)
        cin>>height[i][j];


        putLabel();
        cout<<"Case #"<<tc<<": "<<endl;
        for(int i=0;i<H;i++) {
            for(int j=0;j<W;j++) {
                if(j>0)cout<<" ";
                cout<<result[i][j];
            }
            cout<<endl;
        }

    }
    return 0;
}

