#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;
int main()
{
  int T;
  cin >> T;
  for(int ca = 1; ca <= T; ca++){
    vector<string> table(4);
    for(int i=0; i<4; i++){
      cin >> table[i];
    }
    vector<vector<int> > map(4,vector<int>(4));
    bool bempty = false;
    for(int i=0; i<4; i++){
      for(int j=0; j<4; j++){
	switch (table[i][j]){
	case 'X': map[i][j] = 1; break;
	case 'O': map[i][j] = -1; break;
	case 'T': map[i][j] = 0; break;
	case '.': map[i][j] = 100; bempty = true; break;
	}
      }
    }
    int ans = 0;
    int count1 = 0, count2 = 0;
    for(int i=0; i<4; i++){
      count1 += map[i][i];
      count2 += map[i][3-i];
    }
    if(count1 == 4 || count1 == 3
       || count2 == 4 || count2 == 3) ans = 1;
    else if(count1 == -4 || count1 == -3
	    || count2 == -4 || count2 == -3) ans = 2;
    for(int i=0; i<4; i++){
      int count1 = 0, count2 = 0;
      for(int j=0; j<4; j++){
	count1 += map[i][j];
	count2 += map[j][i];
      }
      if(count1 == 4 || count1 == 3
	 || count2 == 4 || count2 == 3) ans = 1;
      else if(count1 == -4 || count1 == -3
	      || count2 == -4 || count2 == -3) ans = 2;
    }
    if(ans == 0 && bempty) ans = 3;
    char* message[] = {
      "Draw", "X won", "O won", "Game has not completed",
    };
    printf("Case #%d: %s\n", ca, message[ans]); 
  }
  return 0;
}
