#include<stdlib.h>
#include<iostream>
#include<map>
using namespace std;

const int CELLS = 4;


char res(map<char, int> &count) {
 
    if (count['T'] == CELLS)
       return '.';
    if (count['X']+ count['T'] == CELLS)
        return 'X';
    if (count['O']+ count['T'] == CELLS)
        return 'O';
    return '.'; 
}


char solve(char v[CELLS][CELLS]) {

  bool isComplete = true;

  map<char, int> count;
  
  //Rows
  for(int r = 0; r < CELLS; ++r){
    count['X'] = count['T'] = count['.'] = count['O'] = 0;
    for(int c = 0; c < CELLS; ++c) {
        count[v[r][c]]++;
    }    
    int winner = res(count);
    if(winner != '.')
        return winner;
  }
  //COLS

  for(int c = 0; c < CELLS; ++c){
    count['X'] = count['T'] = count['.'] = count['O'] = 0;
    for(int r = 0; r < CELLS; ++r) {
        count[v[r][c]]++;
    }    
    int winner = res(count);
    if(winner != '.')
        return winner;
  }

  //Diagonal
  count['X'] = count['T'] = count['.'] = count['O'] = 0;
  for(int c = 0; c < CELLS; ++c) {
    count[v[c][c]]++;
    int winner = res(count);
    if(winner != '.')
        return winner;
  }

  count['X'] = count['T'] = count['.'] = count['O'] = 0;
  for(int c = 0; c < CELLS; ++c) {
    count[v[c][CELLS-c-1]]++;
    int winner = res(count);
    if(winner != '.')
        return winner;
  }

  return '.';
}


int main() {

    char v[CELLS][CELLS];
    int n_cases;
    cin >> n_cases;
    
    
    for (int num_case = 0; num_case < n_cases; num_case++) {
        char c;
        bool completed = true;
        for (int i = 0; i < CELLS; ++i) {
            cin.get(c);
            for (int j = 0; j < CELLS; ++j) {
                cin.get(c);
                
                if (c == '.')
                    completed = false;
                v[i][j] = c; 
            }
        }

        /*    for (int i = 0; i < CELLS; ++i) {
              for (int j = 0; j < CELLS; ++j) {
              cout << v[i][j];
              }
              cout << endl;
              }
              cout << endl;
        */
        cin.get(); 

        char sol = solve(v);
        cout << "Case #" << num_case+1 << ": ";
        switch(sol){
            case '.':
                if (completed)
                    cout << "Draw" << endl;
                else
                    cout << "Game has not completed" << endl;
                break;
            case 'X': case 'O':
                cout << sol << " won" << endl;

        }

    }
    return EXIT_SUCCESS;
}
