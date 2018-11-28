#include <stdlib.h>
#include <stdio.h>
#include <vector>

using namespace std;

vector< vector<int> > alt;
vector< vector<int> > dir;
int alp[27];


int h,w,nob;
int dy[] = {-1,0,0,1};
int dx[] = {0,-1,1,0};

bool ok(int x,int y) {
     if (x>=0 && x<w && y>=0 && y<h) return true;
     return false;
}

int chkdir(int m,int n) {
    int i,x,y,mark = 0,temp = alt[m][n],arah;
    for (i=0;i<4;i++) {
        x = n+dx[i];
        y = m+dy[i];
        if (ok(x,y) && temp > alt[y][x]) {
           arah = i;
           temp = alt[y][x];
           mark = 1;   
        }
    }      
    if (mark==1) return arah;
    nob++;
    return -nob;
}

void pro(int m,int n) {
     int i,x,y;
     for (i=0;i<4;i++) {
         x = n+dx[i];
         y = m+dy[i]; 
         if (ok(x,y) && dir[y][x]==3-i) {
            dir[y][x] = dir[m][n];
            pro(y,x);
         }
     }
}


int main () {
    int tc,i,j,k,temp;
    freopen ("in.txt","r",stdin);
    freopen ("out.txt","w",stdout);
    scanf ("%d",&tc);
    for (i=0;i<tc;i++) {
        scanf ("%d%d",&h,&w);
        alt.clear(); dir.clear(); 
        alt.resize(h); dir.resize(h);
        for (j=0;j<h;j++) {
            alt[j].resize(w);
            dir[j].resize(w);
            for (k=0;k<w;k++) {
                scanf ("%d",&temp);
                alt[j][k] = temp;
            }    
        }
        nob = 0;
        
        //nentuin arah aliran
        for (j=0;j<h;j++) {
            for (k=0;k<w;k++)     
                dir[j][k] = chkdir(j,k);
        }
        
        //cari basin masing-masing
        for (j=0;j<h;j++)
            for (k=0;k<w;k++) 
                if (dir[j][k]<0) pro(j,k);
                
        //urutin basin N-S W-E
        for (j=1;j<=26;j++) alp[j] = 0;
        temp = 97;
        for (j=0;j<h;j++) {
            for (k=0;k<w;k++) {
                if (alp[-dir[j][k]]!=0) continue;
                else {
                     alp[-dir[j][k]] = temp;
                     temp++;     
                }
            }    
        }
        
        printf ("Case #%d:\n",i+1); 
        for (j=0;j<h;j++) {
            for (k=0;k<w;k++) {
                printf ("%c",(char) alp[-dir[j][k]]);
                if (k<w-1) printf (" ");     
            }   
            printf("\n");
        }
    }
    return 0;
}
