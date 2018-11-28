#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int yy[3] = {0,1,1};
int xx[3] = {1,1,0};

int main() {
    int t;
    scanf("%d",&t);
    for(int i = 1;i <= t;i++) {    
            int r,c;
            int aux = 1;
            char tab[60][60];
            scanf("%d %d",&r,&c);
            for(int j = 0;j < r;j++) 
                    scanf("%s",tab[j]);
            for(int j = 0;j < r;j++) {
                    if(!aux) break;
                    for(int k = 0;k < c;k++) {
                            if(!aux) break;
                            if(tab[j][k] == '#') {
                                         tab[j][k] = '/';
                                         for(int l = 0;l < 3;l++) {
                                                 int a = j + yy[l];
                                                 int b = k + xx[l];
                                                 if(a >= 0 && a < r && b >= 0 && b < c && tab[a][b] == '#') {
                                                      if(l == 0)
                                                           tab[a][b] = '\\';
                                                      if(l == 1)
                                                           tab[a][b] = '/';
                                                      if(l == 2)
                                                           tab[a][b] = '\\';
                                                 }
                                                 else {
                                                      aux = 0;
                                                      break;
                                                 }
                                         }
                            }
                    }
            }
            if(!aux) printf("Case #%d:\nImpossible\n",i);
            else {
                 printf("Case #%d:\n",i);
                 for(int j = 0;j < r;j++)
                         printf("%s\n",tab[j]);
            }             
                                                 
    }
    return 0;
}
