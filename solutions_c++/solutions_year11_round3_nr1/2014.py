#include <cstdio>
#include <cstdlib>

#define MAX_RC 55

char tiles[MAX_RC][MAX_RC];
char ans[MAX_RC][MAX_RC];
bool visited[MAX_RC][MAX_RC];

int dx[4] = {0,1,0,1};
int dy[4] = {0,0,1,1};
char ch[4] = {'/','\\','\\','/'};

int r, c;

inline bool valid(int x, int y) {
   return x >= 0 && y >= 0 && x < c && y < r;
}

int main() {
   FILE* in = fopen("A-small-attempt0.in","r");
   FILE* out = fopen("tileout.txt","w");
   
   int t;
   fscanf(in, "%d", &t);
   for(int i = 1; i <= t; i++) {
      fprintf(out, "Case #%d:\n", i);

      fscanf(in, "%d %d", &r, &c);
      for(int y = 0; y < r; y++) {
         for(int x = 0; x < c; x++) {
            char c = 0;
            while(c != '#' && c != '.') fscanf(in, "%c", &c);
            tiles[x][y] = c;
            ans[x][y] = '.';
            visited[x][y] = false;
         }
      }

      for(int y = 0; y < r; y++) {
         for(int x = 0; x < c; x++) {
            if(!visited[x][y] && tiles[x][y] == '#') {
               printf("from %d,%d\n", x, y);
               for(int k = 0; k < 4; k++) {
                  int newx = dx[k] + x, newy = dy[k] + y;
                  printf("checking %d,%d\n", newx, newy);
                  if(valid(newx, newy)) {
                     visited[newx][newy] = true;
                     ans[newx][newy] = ch[k];
                     printf("%d,%d is visited\n", newx, newy);
                  } else {
                     fprintf(out, "Impossible\n");
                     goto loopend;
                  }
               }
            }
         }
      }
      
      for(int y = 0; y < r; y++) {
         for(int x = 0; x < c; x++) {
            fprintf(out, "%c", ans[x][y]);
         }
         fprintf(out, "\n");
      }

      loopend:
      printf("done %d\n", i);
   }
}
