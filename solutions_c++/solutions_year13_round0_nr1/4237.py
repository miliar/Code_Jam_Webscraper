#include <iostream>
#include <vector>
using namespace std;
bool didWon(char player, const vector<vector<char> >& field) {
   bool diagonal1 = true;
   bool diagonal2 = true;
   for (int i=0; i<field.size(); i++) {
      if (field[i][i] != player && field[i][i] != 'T') {
         diagonal1 = false;
      }
      if (field[i][3-i] != player && field[i][3-i] != 'T') {
         diagonal2 = false;
      }
      bool row = true;
      bool column = true;
      for (int j=0; j<field.size(); j++) {
         if (field[i][j] != player && field[i][j] != 'T') {
            row = false;
         }
         if (field[j][i] != player && field[j][i] != 'T') {
            column = false;
         }
      }
      if (row || column) {
         return true;
      }
   }
   return (diagonal1 == true || diagonal2 == true);
}

bool hasDot(const vector<vector<char> >& field) {
   for(int i=0; i<field.size(); i++) {
      for(int j=0; j<field[i].size(); j++) {
         if(field[i][j] == '.')
            return true;
      }
   }
   return false;
}


int main() {
   ios_base::sync_with_stdio(0);
   int T;
   cin >> T;
   for(int testCase = 1; testCase <= T; testCase++) {
      vector<vector<char> > field;
      field.resize(4);
      for (int i=0; i<4; i++) {
         field[i].resize(4);
         for(int j=0; j<4; j++) {
            cin >> field[i][j];
         }
      }
      cout << "Case #" << testCase << ": ";
      if ( didWon('X', field) ) {
         cout << "X won" << endl;
      } else if (didWon('O', field)) {
         cout << "O won" << endl;
      } else if (hasDot(field)) {
         cout << "Game has not completed" << endl; 
      } else {
         cout << "Draw" << endl;
      }
   }
   return 0;
}
