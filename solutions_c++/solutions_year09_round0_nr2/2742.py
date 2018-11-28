#include<cstdio>
#include<vector>
#include<algorithm>
#include<queue>
using namespace std;
#define mp make_pair
#define pb push_back
#define fi first
#define sc second
#define inf 100000000
typedef pair<int,int> ii;

int tt,t,n,m,mini,maxi;
int tab[200][200],p[200][200],dx[]={-1,0,0,1},dy[]={0,-1,1,0};
bool vis[200][200];
vector<ii> nodes[2000];
char res[200][200],wsk[30];
queue<ii> q;

bool check(int x,int y,int c) {
    int temp=inf; int poz=inf;
    for(int i = 0; i < 4; ++i) {
        if(x+dx[i]>=0 && x+dx[i]<n && y+dy[i]>=0 && y+dy[i]<m) {
            if(tab[x+dx[i]][y+dy[i]]<temp) {
                temp=tab[x+dx[i]][y+dy[i]];
                poz=i;
            }
        }
    }
    if(poz==c) return true;
    return false;
}

void bfs(int x,int y) {
  //   printf("w bfs-ie mamy %d %d i %d\n",x,y,t);
     vis[x][y]=1; p[x][y]=t;
     q.push(mp(x,y));
     while(!q.empty()) {
         ii top=q.front(); q.pop();
         x=top.fi; y=top.sc; int h=tab[x][y];
         for(int i = 0; i < 4; ++i) {
             if(x+dx[i]>=0 && x+dx[i]<n && y+dy[i]>=0 && y+dy[i]<m) {
                 if(!vis[x+dx[i]][y+dy[i]] && h<tab[x+dx[i]][y+dy[i]]) {
                     int str; if(i==0) str=3; if(i==1) str=2; if(i==2) str=1; if(i==3) str=0;
                     if(check(x+dx[i],y+dy[i],str)) {
                         q.push(mp(x+dx[i],y+dy[i]));
                         vis[x+dx[i]][y+dy[i]]=1; p[x+dx[i]][y+dy[i]]=t;
                     }
                 }
             }
         }
     }
}

void czysc() {
     for(int i = 0; i < n; ++i) 
         for(int j = 0; j < m; ++j) 
             tab[i][j]=p[i][j]=res[i][j]=vis[i][j]=0;
     for(int i = mini; i <= maxi; ++i) nodes[i].clear();
     mini=maxi=0;
     for(int i = 0; i < 29; ++i) wsk[i]=0;
     
}

int main() {
    scanf("%d",&tt);
    for(int q = 1; q <= tt; ++q) {
        scanf("%d%d",&n,&m);
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < m; ++j) {
                scanf("%d",&tab[i][j]);
                nodes[tab[i][j]].pb(mp(i,j));
                mini=min(mini,tab[i][j]);
                maxi=max(maxi,tab[i][j]);
            }
        }
        t=0;
        for(int i = mini; i <= maxi; ++i) {
            for(int j = 0; j < nodes[i].size(); ++j) {
                if(!vis[nodes[i][j].fi][nodes[i][j].sc]) {
                    ++t;
 //                   printf("biore pod lupe -> %d %d o wys = %d\n",nodes[i][j].fi,nodes[i][j].sc,tab[nodes[i][j].fi][nodes[i][j].sc]);                    
                    bfs(nodes[i][j].fi,nodes[i][j].sc); 
 //                   printf("teraz wyglada tak:\n");
//                    for(int a = 0; a < n; ++a) {
 //                       for(int z = 0; z < m; ++z) {
//                            printf("%d ",p[a][z]);
//                        }
//                        printf("\n");
//                    } 
                }
            }
        }
        char pom='a';
        for(int i = 0; i < n; ++i) for(int j = 0; j < m; ++j) 
        if(wsk[p[i][j]]<'a' || wsk[p[i][j]]>'z') {
            wsk[p[i][j]]=pom; ++pom;
        }
        for(int i = 0; i < n; ++i) for(int j = 0; j < m; ++j) res[i][j]=wsk[p[i][j]];
        printf("Case #%d:\n",q);
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < m; ++j) {
                printf("%c ",res[i][j]);
            }    
            printf("\n");
        }
        czysc();

    }
   // while(1);
}
