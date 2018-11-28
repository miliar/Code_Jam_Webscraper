#include <iostream>
#include <cmath>
#include <list>
#define sf(x) scanf("%d",&x)
using namespace std;
char grid[30][30];
int sx,sy,cx,cy;
typedef struct State {
    int a,b,c,d,e;
    int val;
};
State states[17][17][17][17][4];
int delta[4][2] = {{1,0},{0,1},{-1,0},{0,-1}};
list<State*> thelist;
void getportal(State* next, int dir, int *px, int *py, int *pz) {
    *pz=dir;
    *px=next->a;
    *py=next->b;
    for (int i=0;;i++) {
        *px+=delta[dir][0];
        *py+=delta[dir][1];
        if (grid[*px][*py]=='#') return;
    }
}
int main() {
    int T; sf(T);
    for (int t=1; t<=T; t++) {
        int R,C;sf(R);sf(C);//printf("%d %d\n",R,C);
        for (int j=0; j<=C+1; j++) grid[0][j]=grid[R+1][j]='#';
        grid[0][C+2]=grid[R+1][C+2]=0;
        //printf("%s\n",grid[0]);
        for (int i=1; i<=R; i++) {
            scanf("%s",&grid[i][1]);
            grid[i][0]=grid[i][C+1]='#';
            grid[i][C+2]=0;
            for (int j=1; j<=C; j++) {
                if (grid[i][j]=='O') {sx=i;sy=j;}
                else if (grid[i][j]=='X') {cx=i;cy=j;}
                if (grid[i][j]=='O' || grid[i][j]=='X') grid[i][j]='.';
            }
        }
//        for (int i=0; i<=R+1; i++) printf("%s\n",grid[i]);
//        printf("\n");

        for (int i=0; i<=R+1; i++)
        for (int j=0; j<=C+1; j++)
        for (int k=0; k<=R+1; k++)
        for (int l=0; l<=C+1; l++)
        for (int m=0; m<4; m++) {
            states[i][j][k][l][m].a=i;
            states[i][j][k][l][m].b=j;
            states[i][j][k][l][m].c=k;
            states[i][j][k][l][m].d=l;
            states[i][j][k][l][m].e=m;                                                
            states[i][j][k][l][m].val=-2;                                                            
        }
        thelist.clear();
        for (int i=0; i<4; i++) {
            int px,py,pz;getportal(&states[sx][sy][0][0][0],i,&px,&py,&pz);
            states[sx][sy][px][py][pz].val=0;
            thelist.push_back(&states[sx][sy][px][py][pz]);
        }

        int ans = -1;
        while (thelist.size()) {
            ans++;
          //  printf("ANS = %d\n",ans);
            int zz = thelist.size();
            for (int z=0; z<zz; z++) {
                State* next = thelist.front();
                bool debug = next->a==1 && next->b==30;
              //  if (debug)
              //  printf("%d %d %d %d %d\n",next->a,next->b,next->c,next->d,next->e,ans);
                
                if (next->a==cx && next->b==cy) {
                    printf("Case #%d: %d\n",t,ans);
                    goto end;
                }
                thelist.pop_front();
                // optionally fire a portal
                for (int i=0; i<5; i++) {
             //   if (debug)                    printf("fire in dir %d\n",i);
                    // first a portal in direction i
                    int px,py,pz;                    
                    if (i==4) {
                        px=next->c;
                        py=next->d;
                        pz=next->e;
                    } else getportal(next,i,&px,&py,&pz);
                    //printf("%d %d %d\n",px,py,pz);
                    for (int j=0; j<4; j++) {
                        int tx = next->a+delta[j][0];
                        int ty = next->b+delta[j][1];                        
                        if (grid[tx][ty]=='#') {
                            tx=next->c-delta[next->e][0];
                            ty=next->d-delta[next->e][1];
                            //printf("(%d %d)\n",tx,ty);
                            int tpx,tpy,tpz;
                            for (int k=0; k<5; k++) {
                                if(k==4) {tpx=px;tpy=py;tpz=pz;}
                                else getportal(&states[tx][ty][0][0][0],k,&tpx,&tpy,&tpz);
                                if (states[tx][ty][tpx][tpy][tpz].val!=-2) continue;
                                states[tx][ty][tpx][tpy][tpz].val=ans;
             ///   if (debug)                        printf("%d %d %d %d %d\n",tx,ty,tpx,tpy,tpz);                                
                                thelist.push_back(&states[tx][ty][tpx][tpy][tpz]);
                            }
                            continue;
                        }
                        if (grid[tx][ty]!='.') continue;
                            int tpx,tpy,tpz;
                            for (int k=0; k<5; k++) {
                                if(k==4) {tpx=px;tpy=py;tpz=pz;}
                                else getportal(&states[tx][ty][0][0][0],k,&tpx,&tpy,&tpz);
                                if (states[tx][ty][tpx][tpy][tpz].val!=-2) continue;
                                states[tx][ty][tpx][tpy][tpz].val=ans;
             //   if (debug)                        printf("%d %d %d %d %d\n",tx,ty,tpx,tpy,tpz);                                
                                thelist.push_back(&states[tx][ty][tpx][tpy][tpz]);
                            }                        
                        
                    }
                }

          //   if (debug)  system("PAUSE");
            }
        }
  printf("Case #%d: THE CAKE IS A LIE\n",t);
        end:;
        
    }
}
