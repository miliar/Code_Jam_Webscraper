#include <iostream>
#include <queue>
#include <vector>
using namespace std;

typedef pair<int,int>pii;
#define x first
#define y second
int tes,n,m,mat[101][101],mini,minx,miny,color[101][101],col;
bool cant[27],used[101][101];

int movex[]={-1, 0, 0, 1};
int movey[]={ 0,-1, 1, 0};

int main(){
    //freopen("hasil.txt","w",stdout);
    scanf("%d",&tes);
    for (int i=0;i<tes;i++){
        scanf("%d %d",&n,&m);
        for (int j=0;j<n;j++){
            for (int k=0;k<m;k++){
                scanf("%d",&mat[j][k]);
            }
        }
        vector<int> tox[101][101],toy[101][101];
        for (int j=0;j<n;j++){
            for (int k=0;k<m;k++){
                mini=1000000000;
                minx=miny=-1;
                for (int l=0;l<4;l++){
                    int tmpx=j+movex[l];
                    int tmpy=k+movey[l];
                    if (tmpx>=0 && tmpy>=0 && tmpx<n && tmpy<m){
                        if (mat[tmpx][tmpy]<mat[j][k]){
                            if (mini>mat[tmpx][tmpy]){
                                mini=mat[tmpx][tmpy];
                                minx=tmpx;
                                miny=tmpy;
                            }
                        }
                    }
                }
                if (minx!=-1){
                    tox[j][k].push_back(minx);
                    toy[j][k].push_back(miny);
                    tox[minx][miny].push_back(j);
                    toy[minx][miny].push_back(k);
                }
            }
        }
        memset(color,-1,sizeof(color));
        col=0;
        for (int j=0;j<n;j++){
            for (int k=0;k<m;k++){
                if (color[j][k]!=-1) continue;
                memset(used,0,sizeof(used));
                queue<pii>q;
                q.push(pii(j,k));
                color[j][k]=col;
                while (!q.empty()){
                    pii top=q.front();
                    int tx=top.x;
                    int ty=top.y;
                    //cout<<tx<<' '<<ty<<endl;
                    used[tx][ty]=1;
                    q.pop();
                    for (int l=0;l<tox[tx][ty].size();l++){
                        int newx=tox[tx][ty][l];
                        int newy=toy[tx][ty][l];
                        color[newx][newy]=col;
                        if (!used[newx][newy]){
                            q.push(pii(newx,newy));
                        }
                    }
                }
                col++;
                //system("pause");
            }
        }
        printf("Case #%d:\n",i+1);
        for (int j=0;j<n;j++){
            for (int k=0;k<m;k++){
                printf("%c",color[j][k]+'a');
                if (k!=m-1) printf(" ");
            }
            printf("\n");
        }
    }
    //system("pause");
    return 0;
}
