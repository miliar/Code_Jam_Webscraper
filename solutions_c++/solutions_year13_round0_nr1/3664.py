#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i!=(b);++i) 
#define REP(i,n) FOR(i,0,n) 
#define dbg(x)   (cout << #x << ":" << (x) << "\t") 
#define dbge(x) (cout << #x << ":" << (x) << "\n") 
#define all(c) c.begin(), c.end() 
#define cpresent(container, element) (find(all(container),element) != container.end())


bool check_complete(vector <string> grid,char sym){
  for(int i=0; i<4; i++)
  {
    int row_solved = true;
    for(int j=0;j<4; j++)
    {
      if(grid[i][j] != sym && grid[i][j] != 'T'){
          row_solved = false;
          break;
        }
    }
    if(row_solved)
      return true;

    int col_solved = true;
    for(int j=0;j<4;j++)
    {
      if(grid[j][i] != sym && grid[j][i] != 'T'){
        col_solved = false;
        break;
      }
    }
    if(col_solved)
      return true;
  }

  bool diag_solved = true;
  for(int i=0; i<4; i++)
  {
    if(grid[i][i] != sym && grid[i][i] != 'T'){
      diag_solved = false;
      break;
    }
  }


  if(diag_solved)
    return true;

  diag_solved = true;
  for(int i=0; i<4; i++)
  {
    if(grid[i][3-i] != sym && grid[i][3-i] != 'T'){
      diag_solved = false;
      break;
    }
  }


  if(diag_solved)
    return true;


  return false;
}

bool gamecompleted(vector <string> grid){

  bool completed = true;

  for(int i=0; i<4; i++)
  {
    for(int j=0; j<4; j++){
      if(grid[i][j] == '.'){
        completed = false;
        break;
      }
    }
    if(completed == false){
      break;
    }
  }

  return completed;
}

int main() {
  int i=0, count;
  char state;
  cin >>  count;
  
  while(i < count)
  {
    vector <string> grid(4);
    for(int j=0;j<4;j++)
    grid[j] = "";
    
    for(int j=0;j<4;j++)
    {
      for(int l=0;l<4;l++)
      {
        cin >> state;
        grid[j].push_back(state);
      }
    }

    if(check_complete(grid,'X')) {
      cout << "Case #"<< ( i + 1) << ": X won\n";
    } else if(check_complete(grid,'O')) {
      cout << "Case #"<< ( i + 1) << ": O won\n";
    } else if(gamecompleted(grid)) {
      cout << "Case #"<< ( i + 1) << ": Draw\n";
    } else {
      cout << "Case #"<< ( i + 1) << ": Game has not completed\n";
    }

  	i++;
  }
  return 0;
}
