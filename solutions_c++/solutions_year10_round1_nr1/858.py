/*
 * Google code jam 2010 / Round 1A
 * Task A: Rotate
 *
 * Created by Krisztian Balog on 5/21/10.
 */

#include <iostream>
#include <vector>
using namespace std;


int canWin(const vector<vector<int> >& b, int N, int K, int player, int dx, int dy) {
  
  vector<vector<int> > p; // board
  p.resize( N );
  for (int i=0;i<N;i++) 
    p[i].resize( N, 0 );
      
  for (int i=0;i<N;i++) {
    for (int j=0;j<N;j++) {
      if (b[i][j] == player) {

        p[i][j] = 1;
        int i2 = i+dy;
        int j2 = j+dx;
        if (i2 >= 0 && i2 < N && j2 >= 0 && j2 < N) 
          if (p[i2][j2]+1 > p[i][j]) p[i][j] = p[i2][j2]+1;
          
        if (p[i][j] == K) return 1;
      }      
    }
  }
  /*
  cout << "Player " << player << " (" << dx << ", " << dy << ")" << endl;
  for (int i=0;i<N;i++) {
    for (int j=0;j<N;j++) {
      if (p[i][j] > 0) cout << p[i][j];
      else cout << ".";
    }
    cout << endl;
  }
  cout << endl;
  */
  return 0;
}

int main(int argc, char* argv[]) {
    
  int T = 0;
  cin >> T;
  
  for (int c=0;c<T;c++) {
    int N;
    int K;
    
    cin >> N;
    cin >> K;
    
    // read in NxN table
    vector<vector<int> > b; // board
    b.resize( N );
            
    for (int i=0;i<N;i++) {
      b[i].resize( N, 0 );
      string str;
      cin >> str;
      for (int j=0;j<N;j++) {
        if (str[j] == 'R') b[i][j] = 1;
        if (str[j] == 'B') b[i][j] = 2;
      }
    }
    
    // rotate table
    vector<vector<int> > b2; // board
    b2.resize( N );
    for (int i=0;i<N;i++) 
      b2[i].resize( N, 0 );
    
    for (int i=0;i<N;i++) {
      for (int j=0;j<N;j++) {
        int i2 = j;
        int j2 = (N-1)-i;
        b2[i2][j2] = b[i][j];
      }
    }
    
    /*
    cout << "Rotated: " << endl;
    for (int i=0;i<N;i++) {
      for (int j=0;j<N;j++) {
        if (b2[i][j] == 1) cout << "R";
        else if (b2[i][j] == 2) cout << "B";
        else cout << ".";
      }
      cout << endl;
    }
    cout << endl;
    */
    
    // apply gravity
    for (int i=0;i<N;i++)
      for (int j=0;j<N;j++)
        b[i][j] = 0;
    
    for (int j=0;j<N;j++) {
      int md = 0;
      for (int i=N-1;i>=0;i--) {
        if (i+1 <= N-1 && b2[i+1][j] == 0) md++;
        b[i+md][j] = b2[i][j];
      }
    }
    
    /* 
    cout << "Gravity: " << endl;                             
    for (int i=0;i<N;i++) {
      for (int j=0;j<N;j++) {
        if (b[i][j] == 1) cout << "R";
        else if (b[i][j] == 2) cout << "B";
        else cout << ".";
      }
      cout << endl;
    }
    cout << endl;
    */
    
    // determine who wins
    int Rwin = 0; 
    int Bwin = 0; 
    vector<int> dx;
    vector<int> dy;
    dy.push_back(0);dx.push_back(-1); // "-"
    dy.push_back(-1);dx.push_back(0); // "|"
    dy.push_back(-1);dx.push_back(1); // "/"
    dy.push_back(-1);dx.push_back(-1); // "\"
    
    for (int i=0;i<dx.size();i++) {
      if (canWin(b, N, K, 1, dx[i], dy[i])) Rwin = 1;
      if (canWin(b, N, K, 2, dx[i], dy[i])) Bwin = 1;      
    }
    
    
    // output
    cout << "Case #" << (c+1) << ": ";
    if (Rwin && Bwin) cout << "Both";
    else if (Rwin && !Bwin) cout << "Red";
    else if (!Rwin && Bwin) cout << "Blue";
    else cout << "Neither";
    cout << endl;
  }
    
  return 0;
}
