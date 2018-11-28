#include <iostream>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>

#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>

using namespace std;

#define FOR(i,a,b)  for(int i=(a);i<(b);++i)
#define F(i,a)      FOR(i,0,a)
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define S           size()

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int n,H,W;
    scanf("%d",&n);
    F(wer,n){
        scanf("%d%d",&H,&W);
        vector<vector<int> > map(H+2,vector<int>(W+2,-1));
        vector<vector<bool> > vis(H+2,vector<bool>(W+2,false));
        vector<vector<char> > Res(H+2,vector<char>(W+2,'a'-1));
        FOR(i,1,H+1)
            FOR(j,1,W+1)
                scanf("%d",&map[i][j]);
        char act = 'a'-1;
        int pax = 1, imax, jmax;
        while(pax > 0){
            act = 'a'-1;
            imax = H;
            jmax = W;
            pax = -19;
            FOR(i,1,H+1){
                FOR(j,1,W+1){
                    if(!vis[i][j]){
                        pax = 1;
                        if(i == imax){
                            if(j < jmax){
                                jmax = j;
                                imax = i;
                            }
                        }
                        if(i < imax){
                            imax = i;
                            jmax = j;
                        }
                        
                    }
                    if(Res[i][j] > act)
                        act = Res[i][j];
                }
            }
            if(pax != 1)
                break;
            act++;
            pair<int,int> top(imax,jmax);
            queue<pair<int,int> > q;
            q.push(top);
            char minact = act;
            while(!q.empty()){
                top = q.front();
                int x=top.first, y=top.second;
                q.pop();
                if(vis[x][y]){
                    if(minact > Res[x][y])
                        minact = Res[x][y];
                    continue;
                }
                Res[x][y] = act;
                vis[x][y] = true;
                
                int donde = map[x][y];
                if(donde > map[x+1][y]){
                    if(!(x+1 > H))
                    donde = map[x+1][y];
                }
                if(donde > map[x-1][y]){
                    if(!(x-1 < 1))
                    donde = map[x-1][y];
                }
                if(donde > map[x][y+1]){
                    if(!(y+1 > W))
                    donde = map[x][y+1];
                }
                if(donde > map[x][y-1]){
                    if(!(y-1 < 1))
                    donde = map[x][y-1];
                }
                if(donde == map[x][y])
                    continue;

                if(donde == map[x-1][y]){
                    if(!(x-1 < 1)){
                    q.push(make_pair(x-1,y)); continue;}
                }
                if(donde == map[x][y-1]){
                    if(!(y-1 < 1)){
                    q.push(make_pair(x,y-1)); continue;}
                }
                if(donde == map[x][y+1]){
                    if(!(y+1 > W)){
                    q.push(make_pair(x,y+1)); continue;}
                }
                if(donde == map[x+1][y]){
                    if(!(x+1 > H)){
                    q.push(make_pair(x+1,y)); continue;}
                }
            }
            FOR(i,1,H+1){
                FOR(j,1,W+1){
                    if(Res[i][j] == act)
                        Res[i][j] = minact;
                }
            }
        }
        
        printf("Case #%d:\n",wer+1);
        FOR(i,1,H+1){
            printf("%c",Res[i][1]);
            FOR(j,2,W+1){
                printf(" %c",Res[i][j]);
            }
            printf("\n");
        }
    }
    fclose(stdout);
    //system("pause");
    return 0;
}
