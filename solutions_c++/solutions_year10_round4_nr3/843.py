#include <cstdlib>
#include <iostream>

using namespace std;

int field1[110][110];
int field2[110][110];

int minX, minY, maxX, maxY;

int C, R;

void fillB(int X1, int Y1, int X2, int Y2){
     for(int i = X1; i <= X2; i++){
             for(int j = Y1; j <= Y2; j++){
                     field1[i][j] = 1;
             }
     }
}

bool nextB(bool o){
     bool l = false;
     for(int i = minX; i <= maxX; i++){
             for(int j = minY; j <= maxY; j++){
                     if(o){
                           if(field1[i][j] == 0 &&  field1[i-1][j] == 1 && field1[i][j-1] == 1){field2[i][j] = 1; l = true;}
                           if(field1[i][j] == 1 && (field1[i-1][j] == 1 || field1[i][j-1] == 1)) {field2[i][j] = 1; l = true;}
                           else{}
                     }else{ 
                           if(field2[i][j] == 0 &&field2[i-1][j] == 1 && field2[i][j-1] == 1){field1[i][j] = 1; l = true;}
                           if(field2[i][j] == 1 && (field2[i-1][j] == 1 || field2[i][j-1] == 1)) {field1[i][j] = 1; l = true;}
                            
                     }
             }
     }
     return l;
}

void printField(int w){
     for(int i = minX; i <= maxX; i++){
             for(int j = minY; j< maxY; j++){
                     if(w == 1) printf("%d ", field1[i][j]);
                     else printf("%d ", field2[i][j]); 
             }
             printf("\n");
     }
}

int main(int argc, char *argv[])
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("Solution.txt", "w", stdout);
    
    
    scanf("%d ", &C);
    
    for(int cas = 1; cas <= C; cas++){
    
            scanf("%d ",&R);
            int x1, x2, y1, y2;
          
            memset(field1, 0, sizeof(field1));
            memset(field2, 0, sizeof(field2));
            
            minX = 1000; minY = 1000;
            maxX = 0; maxY = 0;
            
            for(int i = 0; i < R; i++){
                    scanf("%d %d %d %d ", &x1, &y1, &x2, &y2);
                    if(x1 < minX) minX = x1;
                    if(x2 > maxX) maxX = x2;
                    if(y1 < minY) minY = y1;
                    if(y2 > maxY) maxY = y2;
                    
                    fillB(x1, y1, x2, y2);
            }
    
            int count = 1;
            bool o = true;
            
            
            while(nextB(o)){
                           count +=1;
                           o = (!o);
                           if(!o) memset(field1, 0, sizeof(field1));
                           else memset(field2, 0, sizeof(field2));
                           
            }
            
            
            printf("Case #%d: %d\n", cas, count);
    }

    return 0;
}
