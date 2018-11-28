#include <iostream>
#include <vector>
#include <string>

using namespace std;

#define MAX 110
#define INF 100000

int m , n;
int a[MAX][MAX];

int sink[MAX][MAX][2];

char labelMap[MAX][MAX];

//N,W,E,S
const int di[4]={-1,0,0,1};
const int dj[4]={0,-1,1,0};

void determineSink(int i, int j) {
    if (sink[i][j][0]!=-1) return; 
    int minA=INF, im, jm;
    for (int d=0; d<4; ++d) {
        int i2=i+di[d], j2=j+dj[d];
        if (0<=i2 && i2<m && 0<=j2 && j2<n && a[i2][j2]<minA) {
            minA=a[i2][j2];
            im=i2;
            jm=j2;
        }
    }
    
    //cout << "Neighbor " << i << " " << j << " " << im << " " << jm << endl;
    
    if (minA>=a[i][j]) {
        sink[i][j][0]=i;
        sink[i][j][1]=j;
    } else {        
        determineSink(im,jm);
        sink[i][j][0]=sink[im][jm][0];
        sink[i][j][1]=sink[im][jm][1];        
    }
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int nTest;
    scanf("%d", &nTest);
    for (int test=1; test<=nTest; ++test) {
        scanf("%d%d", &m, &n);
        for (int i=0; i<m; ++i)
            for (int j=0; j<n; ++j) {
                scanf("%d", &a[i][j]);
            }
            
        memset(sink,0xff,sizeof(sink));
        for (int i=0; i<m; ++i)
            for (int j=0; j<n; ++j) if (sink[i][j][0]==-1) {
                determineSink(i,j);
      //          printf("%d %d %d %d\n", i, j, sink[i][j][0], sink[i][j][1]);
            }
            
        memset(labelMap,0,sizeof(labelMap));
        
        char cur='a';        
       
        printf("Case #%d:\n", test);
        
        for (int i=0; i<m; ++i) {
            for (int j=0; j<n; ++j) {
                int si=sink[i][j][0], sj=sink[i][j][1];
                if (labelMap[si][sj]==0) {
                    labelMap[si][sj]=cur;
                    ++cur;
                }
                printf("%c ", labelMap[si][sj]);
            }
            printf("\n");
        }
    }
    
    return 0;
}
