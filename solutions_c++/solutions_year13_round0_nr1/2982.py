#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<utility>
#define MP make_pair
using namespace std; 
string board[4];
bool visited[4][4];
bool is_win(int x ,int y){
    int r = 0 ;
    bool yes = false;
    if( board[x][y] == '.' || board[x][y] == 'T')
        return false;
    for(int j = 0 ; j < 4 ;j++){
            if( board[x][j] == board[x][y] || board[x][j] == 'T' )
                r++;
    }
    //cout<<" * "<<r<<endl;
    if( r == 4)
        yes = true;
    r = 0;
    for(int j = 0 ; j < 4 ;j++){
            if( board[j][y] == board[x][y] || board[j][y] == 'T' )
                r++;
    }
   // cout<<" * "<<r<<endl;
    if( r == 4 )
        yes = true;
    r = 0;
    if((x == 0 && y == 0) ||(x == 3 && y == 3)){
        for(int j = 0 ; j < 4 ; j++){
                if(board[j][j] == board[x][y] || board[j][j] == 'T') 
                    r ++ ;
        }
        if( r == 4 )
            yes = true;
    }
   // cout<<" * "<<r<<endl;
    r = 0;
    if((x == 0 && y == 3) ||(x == 3 && y == 0)){
        for(int j = 0 ; j < 4 ; j++){
                if(board[j][3-j] == board[x][y] || board[j][3-j] == 'T') 
                    r ++ ;
        }
        if( r == 4 )
            yes = true;
    }
   // cout<<" * "<<r<<endl;
    return yes;
}
void print(){
     for(int i = 0 ; i < 4 ;i++)     {
             for(int j =0 ; j < 4 ; j++)
                     cout<<board[i]<<" ";
             cout<<endl;}
     cout<<endl;
}
int main(){
    //freopen("input", "r", stdin);
    //freopen("output" ,"w",stdout);
    int t , test = 1; 
    cin>>t ;
    while(t--){
              // cout<<t<<endl;
          for(int i = 0; i < 4 ; i++)      
                  cin>>board[i];
          bool f = false;
          vector < pair < int , int > > all;
          char win='.';
          for(int i = 0 ; i < 4 ; i++){
                  for(int j = 0 ; j < 4 ; j++){
                          if( is_win(i,j)){
                              //cout<<"yes"<<endl;
                              f = true;
                              win = board[i][j];
                              break;
                          }
                          if( board[i][j] == '.')
                              all.push_back(MP(i,j));
                  }
                  if(f)
                       break;
          }            
          if( f )
              printf("Case #%d: %c won\n", test , win);
          else{
              if(all.size() == 0)
                            printf("Case #%d: Draw\n", test);
              else
                  printf("Case #%d: Game has not completed\n", test);
          }
              
          test ++ ;
    }
    return 0 ;     
}
