using namespace std;
#include <iostream>
#include <cstdio>
#include <cstring>
#include <numeric>
#include <utility>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <cassert>

#define out(x) (cout<<#x<<": "<<x<<endl)

template<class T>
inline int lth(const T &x) {return static_cast<int>(x.size()); }

const int to[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};
int n,m;
char color[120][120];
int h[120][120];
vector<pair<int,int> > G[120][120];

void dfs(int I,int J,char x) {
    color[I][J] = x;
    
    for(vector<pair<int,int> >::iterator r=G[I][J].begin(),E=G[I][J].end();r!=E;++r) {
        if(color[r->first][r->second]!=x) {
            assert(color[r->first][r->second]==0);///debug
            dfs(r->first,r->second,x);
        }
    }
}

int main(int argc,char **argv) {
    freopen(argv[1],"r",stdin);
    freopen(argv[2],"w",stdout);

    int Kse;
    scanf("%d",&Kse);
    for(int k=1;k<=Kse;++k) {
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;++i) {
            for(int j=0;j<m;++j) {
                scanf("%d",h[i]+j);
            }
        }
        for(int i=0;i<n;++i)
            for(int j=0;j<m;++j)
                G[i][j].clear();
        for(int i=0;i<n;++i) {
            for(int j=0;j<m;++j) {
                int Min=0x7f7f7f7f;
                int MinI=-1,MinJ=-1;
                for(int t=0;t<4;++t) {
                    const int I = i+to[t][0];
                    const int J = j+to[t][1];
                    if(I<n && I>=0 && J<m && J>=0) {
                        if(h[I][J] < h[i][j] && h[I][J]<Min) {
                            Min = h[I][J];
                            MinI = I;
                            MinJ = J;
                        }
                    }
                } 
                if(MinI !=-1) {
                    assert(MinJ!=-1);///debug
                    G[MinI][MinJ].push_back(make_pair(i,j));
                    G[i][j].push_back(make_pair(MinI,MinJ));
                }
            }
        }

        memset(color,0,sizeof(color));
        char ch='a';
        for(int i=0;i<n;++i) {
            for(int j=0;j<m;++j) {
                if(color[i][j]==0 ) {
                    dfs(i,j,ch);
                    ++ch;
                }
            }
        }
        printf("Case #%d:\n",k);
        for(int i=0;i<n;++i) {
            for(int j=0;j<m;++j) 
                printf("%c ",color[i][j]);
            printf("\n");
        }
    }
    return 0;
}











