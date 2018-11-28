#include <iostream>
using namespace std;
static char field[4][4];
bool horizontal(char player){
  for(int j=0;j<4;j++){
    int count = 0;
    for(int k=0;k<4;k++){
      if(field[j][k] == player || field[j][k] == 'T'){
        count++;
      }
    }
    if(count == 4){
      return true;
    }
  }
  return false;
}
bool vertical(char player){
  for(int j=0;j<4;j++){
    int count = 0;
    for(int k=0;k<4;k++){
      if(field[k][j] == player || field[k][j] == 'T'){
        count++;
      }
    }
    if(count == 4){
      return true;
    }
  }  
  return false;
}
bool diagonal(char player){
  int count=0;
  for(int j=0;j<4;j++){
    if(field[j][j] == player || field[j][j] == 'T'){
      count++;
    }
  }
  if(count == 4){
    return true;
  }
  count=0;
  for(int j=0;j<4;j++){
    if(field[3-j][j] == player || field[3-j][j] == 'T'){
      count++;
    }
  }
  if(count == 4){
    return true;
  }
  return false;
}
int main(){
  int testcases;
  cin >> testcases;
  //cin.ignore()
  for(int i=1;i<=testcases;i++){
   
    //read in field
    
    //draw = true, false wenn .
    bool draw = true;
    for(int j=0;j<4;j++){
      char in;
      for(int k=0;k<4;k++){
        cin >> in;
        if(in == '.'){
          draw = false;
        }
        field[j][k] = in;
      }
    }
    cin.ignore();
    string dummy;
    getline(cin, dummy);


    //debug output
    // for(int j=0;j<4;j++){
    //   for(int k=0;k<4;k++){
    //     cout << field[j][k] << ' ';
    //   }
    //   cout << endl;
    // }

    

    //teste x
    if(horizontal('X') || vertical('X') || diagonal('X')){
      cout << "Case #" << i << ": X won" << endl;
      continue;
    }


    //teste o    
    if(horizontal('O') || vertical('O') || diagonal('O')){
      cout << "Case #" << i << ": O won" << endl;
      continue;
    }

    //wenn draw false -> game not completed, draw else
    if(draw){
      cout << "Case #" << i << ": Draw" << endl;
    }
    else{
      cout << "Case #" << i << ": Game has not completed" << endl;
    }
    


    
  }
}