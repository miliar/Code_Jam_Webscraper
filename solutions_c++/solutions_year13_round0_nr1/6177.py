#include <iostream>
#include <vector>
#include <deque>

#include <algorithm>
#include <string>
#include <iomanip>

using namespace std;

typedef long long ll;

typedef std::pair<ll,ll> mypair;


int main()
{
  int T;
  
  cin>>T;
  
  vector<vector<char> > board(4);
  
  for(int j=0; j<4; ++j)
    board[j].resize(4);
  
  int X_count = 0, O_count = 0, T_count = 0;

  for(int i=0; i<T; ++i)
  {
    bool filled = true;
    bool X_won = false;
    bool O_won = false;
    
    for(int j=0; j<4; ++j)
      for(int k=0; k<4; ++k)
      {
        cin>>board[j][k];
        
        if (board[j][k] == '.') filled = false;
      }
    
    for(int j=0; j<4; ++j)
    {
      int X_count = 0, O_count = 0, T_count = 0;
      
      for(int k=0; k<4; ++k)
      {
        if (board[j][k] == 'X') X_count++;
        else if (board[j][k] == 'O') O_count++;
        else if (board[j][k] == 'T') T_count++;
      }
      
      if (X_count + T_count >= 4) {
        X_won =true; goto done;
      }
      else if (O_count + T_count >= 4) {
        O_won =true; goto done;
      }
    }
    
    for(int k=0; k<4; ++k)
    {
      int X_count = 0, O_count = 0, T_count = 0;
      
      for(int j=0; j<4; ++j)
      {
        if (board[j][k] == 'X') X_count++;
        else if (board[j][k] == 'O') O_count++;
        else if (board[j][k] == 'T') T_count++;
      }
      
      if (X_count + T_count >= 4) {
        X_won =true; goto done;
      }
      else if (O_count + T_count >= 4) {
        O_won =true; goto done;
      }
    }

    X_count = 0, O_count = 0, T_count = 0;
    
    for(int l=0; l<4; ++l)
    {
      if (board[l][l] == 'X') X_count++;
      else if (board[l][l] == 'O') O_count++;
      else if (board[l][l] == 'T') T_count++;
    }
    
    if (X_count + T_count >= 4) {
      X_won =true; goto done;
    }
    else if (O_count + T_count >= 4) {
      O_won =true; goto done;
    }

    X_count = 0, O_count = 0, T_count = 0;
    
    for(int l=0; l<4; ++l)
    {
      if (board[l][3-l] == 'X') X_count++;
      else if (board[l][3-l] == 'O') O_count++;
      else if (board[l][3-l] == 'T') T_count++;
    }
    
    if (X_count + T_count >= 4) {
      X_won =true; goto done;
    }
    else if (O_count + T_count >= 4) {
      O_won =true; goto done;
    }
    
    done:
    
    if(X_won) cout<<"Case #"<<i+1<<": " <<"X won"<<endl;
    else if(O_won) cout<<"Case #"<<i+1<<": " <<"O won"<<endl;
    else if(filled)  cout<<"Case #"<<i+1<<": " <<"Draw"<<endl;
    else cout<<"Case #"<<i+1<<": " <<"Game has not completed"<<endl;
    
  }
  
	return 0;
}
