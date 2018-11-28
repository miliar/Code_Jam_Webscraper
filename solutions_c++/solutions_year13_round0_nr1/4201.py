#include <iostream>
#include <string>
using namespace std;

char table[4][4];

void captureInput(){
  // initialize table
  for(int i=0;i<4;i++)
    for(int j=0;j<4;j++)
      table[i][j]='E';

  string s;
  for(int i=0;i<4;i++){
    cin>>s;
    for(int j=0;j<4;j++)
      table[i][j]=s[j];
  }

}

void printTable(){
    for(int i=0;i<4;i++){
      for(int j=0;j<4;j++)
	cout<<table[i][j];
      cout<<endl;
    }
}

bool testLine(char team, char e[]){
  for(int i=0;i<4;i++)
    if(e[i]!=team && e[i]!='T')
      return false;
  return true;
}

bool hasWon(char team){
  char line[4];
    
  //test rows
  for(int i=0;i<4;i++){
    for(int j=0;j<4;j++)
      line[j]=table[i][j];
    if(testLine(team,line))
      return true;
  }

  //test columns
  for(int j=0; j<4; j++){
    for(int i=0;i<4;i++)
      line[i]=table[i][j];
    if(testLine(team,line))
      return true;
  }
  
  //test diagonals
  for(int i=0;i<4;i++)
    line[i]=table[i][i];
  if(testLine(team,line))
    return true;

  for(int i=0;i<4;i++)
    line[i]=table[3-i][i];
  if(testLine(team,line))
    return true;

  return false;
}

bool hasEmptySquares(){
  for(int i=0; i<4;i++)
    for(int j=0;j<4;j++)
      if(table[i][j]=='.')
	return true;
  return false;
}

int main(){
  int T;
  cin>>T;
  for (int test=0; test<T; test++){
    captureInput();
    cout<<"Case #"<<test+1<<": ";
    if(hasWon('X')){
      cout<<"X won"<<endl;
      continue;
    }
    if(hasWon('O')){
      cout<<"O won"<<endl;
      continue;
    }
    if(hasEmptySquares())
      cout<<"Game has not completed"<<endl;
    else
      cout<<"Draw"<<endl;
  }
  return 0;
}
