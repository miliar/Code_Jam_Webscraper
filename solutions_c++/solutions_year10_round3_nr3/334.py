/*
 * Google code jam 2010 / Round 1C
 * Task C: Making Chess Boards
 *
 * Created by Krisztian Balog on 5/23/10.
 */

#include <iostream>
#include <vector>
#include <map>
using namespace std;


string HexToBin(char ch) {
  switch (ch) {
    case '0': return "0000";
    case '1': return "0001";
    case '2': return "0010";
    case '3': return "0011";
    case '4': return "0100";
    case '5': return "0101";
    case '6': return "0110";
    case '7': return "0111";
    case '8': return "1000";
    case '9': return "1001";
    case 'A': return "1010";
    case 'B': return "1011";
    case 'C': return "1100";
    case 'D': return "1101";
    case 'E': return "1110";
    case 'F': return "1111";
    default: return "";
  }
}

typedef vector< vector< int > > T_GRID;

int min (int a, int b, int c) {
  return min (a, min (b,c));
}


void getMaxSize(const T_GRID& grid, const T_GRID& used, T_GRID& maxsize, int& max) {
  max = 0;
  
  for (int i=0;i<grid.size();i++)  // row
    for (int j=0;j<grid[i].size();j++) { // col
      int mv = 0;
      if (used[i][j]) mv = 0;
      else if (i == 0) mv = 1;
      else if (j == 0) mv = 1;
      else {
        if (grid[i-1][j-1] == grid[i][j] 
            && grid[i-1][j] == 1-grid[i][j] 
            && grid[i][j-1] == 1-grid[i][j]
            && !used[i-1][j-1] && !used[i-1][j] && !used[i][j-1]
            ) {
          mv = min(maxsize[i-1][j-1], maxsize[i][j-1], maxsize[i-1][j]) + 1;
        }
        else {
          mv = 1;
        }
      }
      
      maxsize[i][j] = mv;      
      if (mv > max) max = mv;      
    }
}

int removeMax(const T_GRID& grid, T_GRID& used, const T_GRID& maxsize, const int& max) {  
  for (int i=0;i<grid.size();i++)  
    for (int j=0;j<grid[i].size();j++) 
      if (maxsize[i][j] == max) {
        for (int ii=i-max+1;ii<=i;ii++)
          for (int jj=j-max+1;jj<=j;jj++)
            used[ii][jj] = 1;
        return 1;
      }
  return 0;  
}

void displayGrid(const T_GRID& grid) {
  for (int i=0;i<grid.size();i++) {
    for (int j=0;j<grid[i].size();j++) { 
      cout << grid[i][j] << " ";
    }
    cout << endl;
  } 
  cout << endl;
}


int main(int argc, char* argv[]) {

  int T = 0;
  cin >> T;
  
  for (int c=0;c<T;c++) {
    int N;
    int M;
    
    cin >> M; // lines
    cin >> N; // columns

    T_GRID grid;
    
    for (int i=0;i<M;i++) {
      string row;
      cin >> row;
      vector< int > gridrow;
      for (int j=0;j<row.length();j++) {
        string hr = HexToBin(row[j]);
        for (int k=0;k<hr.length();k++) {
          gridrow.push_back((int)hr[k] - (int)'0');
        }
      }
      grid.push_back(gridrow);
    }

    // init
    T_GRID used;    
    T_GRID maxsize;
    used.resize( grid.size() );
    maxsize.resize( grid.size() );
    for (int i=0;i<grid.size();i++) 
      for (int j=0;j<grid[i].size();j++) {
        used[i].push_back(0);
        maxsize[i].push_back(0);        
      }
    
    map< int, int > res;
    int sumnum = 0;
    int max = 0;
    getMaxSize(grid, used, maxsize, max);
    
    while (max > 0) {
      int num = removeMax(grid, used, maxsize, max);
      //displayGrid(used);
      
      if (res.find(max) == res.end()) res[max] = num;
      else res[max]++;

      sumnum += num;
      
      getMaxSize(grid, used, maxsize, max);      
      //displayGrid(maxsize);
    }
    
        
    // output
    cout << "Case #" << (c+1) << ": " << res.size() << endl;
    for (int i=N;i>0;i--) 
      if (res[i] > 0)
        cout << i << " " << res[i] << endl;

    //exit( -1 );
  }
    
  return 0;
}
