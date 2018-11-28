#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

//North, West, East, South
int diri[4] = {-1, 0, 0, 1};
int dirj[4] = {0, -1, 1, 0};

int main () {
  int N;
  
  scanf ("%d", &N);
  
  for (int n = 1; n <= N; n++) {
    int W, H;
    scanf ("%d%d", &H, &W);
    vector<vector<int> > alt (H);
    vector<vector<char> > basin (H);
    for (int i = 0; i < H; i++) {
      alt[i] = vector<int> (W);
      basin[i] = vector<char> (W, '\0');
      for (int j = 0; j < W; j++)
        scanf ("%d", &(alt[i][j]));
    }
    
    /*for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++)
        printf ("%d ", alt[i][j]);
      printf ("\n");
    }*/
    
    char next = 'a';
    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++) {
        if (basin[i][j] != '\0')
          continue;
        
        int ni = i, nj = j;
        vector<int> path;
        
        while (basin[ni][nj] == '\0') {
          //printf ("%d %d\n", ni, nj);
          int mink = 4;
          for (int k = 0; k < 4; k++) {
            if (ni + diri[k] < 0 || ni + diri[k] >= H || nj + dirj[k] < 0 || nj + dirj[k] >= W)
              continue;
            if (alt[ni+diri[k]][nj+dirj[k]] < alt[ni][nj] && (mink == 4 || alt[ni+diri[k]][nj+dirj[k]] < alt[ni+diri[mink]][nj+dirj[mink]]))
              mink = k;
          }
          if (mink < 4) {
            path.push_back(mink);
            ni += diri[mink];
            nj += dirj[mink];
          }
          else {
            basin[ni][nj] = next;
            next++;
          }
        }
        
        //printf ("iusdiuhsdihiuh");
        char color = basin[ni][nj];
        for (int k = path.size()-1; k >= 0; k--) {
          ni -= diri[path[k]];
          nj -= dirj[path[k]];
          basin[ni][nj] = color;
        }
      }
    }
    
    printf ("Case #%d:\n", n);
    
    for (int i = 0; i < H; i++) {  
      for (int j = 0; j < W; j++)
        printf ("%c ", basin[i][j]);
      printf ("\n");
    }   
        
        
  }
  
  return 0;
}
