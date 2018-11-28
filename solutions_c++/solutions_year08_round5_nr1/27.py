#include <stdio.h>
#include <string.h>
#include <vector>
#include <set>
#include <string>
#include <algorithm>
#include <map>
using namespace std;

// 0..3 = ENWS

map<int,int> vmap[7000];
map<int,int> hmap[7000];

int areamap[7000][7000]; // 0 = not, 1 = inside, 2 = inpocket
int dfx[]={1,0,-1,0};
int dfy[]={0,1,0,-1};

#define CENTER 3500
#define C(x) (x+CENTER)

char buffer[100];

inline int R(int x){    
    x++;
    if (x>3) x=0;
    return x;
}
inline int L(int x){    
    x--;
    if (x<0) x=3;
    return x;
}

int main(){
    int ntc,ttc=0;
    scanf("%d", &ntc);
    while (ntc--){
        memset(areamap,0,sizeof(areamap));
        for (int i=0;i<7000;i++){
            vmap[i].clear();
            hmap[i].clear();
        }
        int n;
        scanf("%d", &n);
        int px = 0, py=0, dir=0;
        
        for (int i=0;i<n;i++){
            int times;
            scanf("%s%d", buffer, &times);
            for (int j=0;j<times;j++){
                for (int k=0;buffer[k];k++){
                    if (buffer[k]=='R'){
                        dir = R(dir);
                    } else if (buffer[k]=='L'){
                        dir = L(dir);
                    } else {
                        // move
                        int nx = px+dfx[dir], ny=py+dfy[dir];
                        int ux = min(px,nx);
                        int uy = min(py,ny);
                        
                        if (dir==0){
                            // E
                            vmap[C(ux)][C(uy)]++;
                        } else if (dir==1){
                            // N
                            hmap[C(uy)][C(ux)]++;
                        } else if (dir==2){
                            // W
                            vmap[C(ux)][C(uy)]--;
                        } else {
                            // S
                            hmap[C(uy)][C(ux)]--;
                        }
                        
                        px=nx;
                        py=ny;
                    }
                }
            }
        }        
        for (int i=0;i<7000;i++){
            vector<int> xss;
            for (map<int,int>::iterator it = vmap[i].begin();it!=vmap[i].end();it++){
                pair<int,int> cur = *it;
                if (cur.second!=0){
                    xss.push_back(cur.first);
                }
            }
            // sort not needed
            
            for (int j=1;j<xss.size();j++){
                /* if (j%2){
                    // area inside
                    for (int k=xss[j-1];k<xss[j];k++){
                        areamap[i][k]=1;
                    }
                } */
                if (!(j%2)) {
                    // pocket inside
                    for (int k=xss[j-1];k<xss[j];k++){
                        areamap[i][k]=2;
                    }
                }
            }
            
            if (xss.size()%2){
                fprintf(stderr, "Possible Error detected\n");
            }
        }
        for (int i=0;i<7000;i++){
            vector<int> xss;
            for (map<int,int>::iterator it = hmap[i].begin();it!=hmap[i].end();it++){
                pair<int,int> cur = *it;
                if (cur.second!=0){
                    xss.push_back(cur.first);
                }
            }
            // sort not needed
            
            for (int j=1;j<xss.size();j++){
                /* if (j%2){
                    // area inside
                    for (int k=xss[j-1];k<xss[j];k++){
                        areamap[i][k]=1;
                    }
                } */
                if (!(j%2)) {
                    // pocket inside
                    for (int k=xss[j-1];k<xss[j];k++){
                        areamap[k][i]=2;
                    }
                }
            }            
            
            if (xss.size()%2){
                fprintf(stderr, "Possible Error detected\n");
            }
        }   
        int res = 0; 
        for (int i=0;i<7000;i++)
        for (int j=0;j<7000;j++){
            if (areamap[i][j]==2){
               // printf("%d %d\n", i-CENTER, j-CENTER);
                res++;
            }
        }    
        
        printf("Case #%d: %d\n", ++ttc, res);
    }
    
    return 0;
}
