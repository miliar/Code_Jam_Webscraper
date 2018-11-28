#include <iostream>
#include <vector>
#include <utility>
#include <map>
using namespace std;

int H[200][200];
int state[200][200];
int height, width;

void walk(int i, int j)
{
     int dir[4][2] = { {-1,0} , {0, -1}, {0, 1}, {1, 0} };
     vector<pair<int, int> > path;
     int ID;
     while (true) {
           path.push_back(make_pair(i, j));
           int nextX = -1;
           int nextY = -1;
           int minH = 99999999;
           
           for (int k = 0; k < 4; ++k) {
               int newX = i + dir[k][0];
               int newY = j + dir[k][1];
               if (newX >= 0 && newX < height && newY >= 0 && newY < width) {
                        if (H[newX][newY] < minH && H[newX][newY] < H[i][j]) {
                                          minH = H[newX][newY];
                                          nextX = newX;
                                          nextY = newY;
                        }
               }
           }
           
           if (nextX == -1) {
              ID = i * width + j;
              break;
           }
           if (state[nextX][nextY] >= 0) {
              ID = state[nextX][nextY];
              break;
           }
           i = nextX;
           j = nextY;
     }
     for (int i = 0; i < path.size(); ++i)
         state[path[i].first][path[i].second] = ID;
}      
                          
                                           
int deal()
{
    for (int i = 0; i < height; ++i)
        for (int j = 0; j < width; ++j)
            state[i][j] = -1;
    
    for (int i = 0; i < height; ++i)
        for (int j = 0; j < width; ++j)
            if (state[i][j] == -1) 
               walk(i, j);
              
    map<int, char> result;
    char answer[200][200];
    char now = 'a'; 
    for (int i = 0; i < height; ++i) 
        for (int j = 0; j < width; ++j) {
            if (result.find(state[i][j]) == result.end()) {
                result[state[i][j]] = now++;
            }
            answer[i][j] = result[state[i][j]];
        }

    static int cases = 0;
    cases++;
    printf("Case #%d:\n", cases);
    for (int i = 0; i < height; ++i) {
        for (int j = 0; j < width; ++j)
            printf("%c ", answer[i][j]);
        printf("\n");
    }    
} 


int main()
{
    int T;
    cin >> T;
    while (T--)
    {
          scanf("%d%d", &height, &width);
          for (int i = 0; i < height; ++i)
              for (int j = 0; j < width; ++j)
                  scanf("%d", &H[i][j]);
          deal();
    }
}
