
#include <iostream>
using namespace std;

static char board[4][4];




// Read next board using cin, to board variable
void read_board(){
  
  for(int row=0; row<4; row++){
    
    string next;
    cin >> next;

    for(int col=0; col<4; col++){
      
      board[row][col] = next[col];

    }


  }

}



char process_board(){


  bool is_completed = true;


  // Go through every row
  for(int row = 0; row < 4; row++){
    
    bool has_x_won = true;
    bool has_o_won = true;

    for(int col = 0; col < 4; col++){
      
      char c = board[row][col];
      if(c == '.'){
        has_x_won = false;
        has_o_won = false;
        is_completed = false;
      }
      if(c == 'X'){
        has_o_won = false;
      }
      if(c == 'O'){
        has_x_won = false;
      }

    }

    if(has_x_won) return 'X';
    if(has_o_won) return 'O';


  }

  


  for(int col = 0; col < 4; col++){
    
    bool has_x_won = true;
    bool has_o_won = true;

    for(int row = 0; row < 4; row++){
      
      char c = board[row][col];
      if(c == '.'){
        has_x_won = false;
        has_o_won = false;
      }
      if(c == 'X'){
        has_o_won = false;
      }
      if(c == 'O'){
        has_x_won = false;
      }

    }

    if(has_x_won) return 'X';
    if(has_o_won) return 'O';


  }


  bool has_x_won = true;
  bool has_o_won = true;
  for(int d = 0; d < 4; d++){

      
    char c = board[d][d];
    if(c == '.'){
      has_x_won = false;
      has_o_won = false;
    }
    if(c == 'X'){
      has_o_won = false;
    }
    if(c == 'O'){
      has_x_won = false;
    }

  }
  if(has_x_won) return 'X';
  if(has_o_won) return 'O';


  has_x_won = true;
  has_o_won = true;
  for(int d = 0; d < 4; d++){

      
    char c = board[d][3-d];
    if(c == '.'){
      has_x_won = false;
      has_o_won = false;
    }
    if(c == 'X'){
      has_o_won = false;
    }
    if(c == 'O'){
      has_x_won = false;
    }


  }
  if(has_x_won) return 'X';
  if(has_o_won) return 'O';

  if(!is_completed)
    return 'N';

  return 'D';

  
}




int main(){
  int ncases;
  cin >> ncases;

  for(int i=0; i<ncases; i++){
    read_board();
    char result = process_board();

    if(result == 'X')
      cout << "Case #" << i+1 << ": X won" << endl;
    if(result == 'O')
      cout << "Case #" << i+1 << ": O won" << endl;
    if(result == 'N')
      cout << "Case #" << i+1 << ": Game has not completed" << endl;
    if(result == 'D')
      cout << "Case #" << i+1 << ": Draw" << endl;

  }

}

