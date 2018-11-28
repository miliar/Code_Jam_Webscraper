# include <iostream>
# include <cstdio>
# include <algorithm>
# include <vector>
# include <cmath>
# include <fstream>

using namespace std;

ifstream in("A-large.in");
ofstream out("output.txt");

void fill(vector<string> &vs, int x, int y){
                         if(x < 0 || y < 0 || x > vs.size() || y > vs[0].size()){
                                return;
                              }
                              
                         if(vs[x][y] == '#'){
                                     if(x+1 < vs.size() && y+1 < vs[0].size()){                                                                     
                                            
                                            if(vs[x+1][y] == '#' && vs[x][y+1] == '#' && vs[x+1][y+1] == '#' ){
                                            vs[x][y]='/';
                                            vs[x+1][y]='\\';                                                                                                                                    
                                            vs[x][y+1]='\\';                                                                                        
                                            vs[x+1][y+1]='/';
                                            }
                                          }
                              }
                              return;
     }

void solve(vector<string> &matrix){
                          
                          for(int i = 0; i<matrix.size(); ++i){
                                  for(int j = 0; j<matrix[i].size(); ++j){
                                            if(matrix[i][j] == '#'){
                                                            fill(matrix, i, j);
                                                 }
                                          }
                                  }
                                  
                          for(int i = 0; i<matrix.size(); ++i){
                                  for(int j = 0; j<matrix[i].size(); ++j){
                                            if(matrix[i][j]=='#'){
                                                                  out<<"Impossible";
                                                                  return;
                                                 }
                                          }
                                  }
                                  
                          for(int i = 0; i<matrix.size(); ++i){
                                    out<<matrix[i];
                                    
                                    if(i != matrix.size()-1){
                                         out<<endl;
                                         }                                    
                                  }
     }
     
int main(){
    int T, cas = 0;
    
    in>>T;
    
    while(T--){
               int R, C;
               in>>R>>C;
               
               string row;
               vector<string> tiles;
               
               for(int i = 0;i<R; ++i){
                       in>>row;
                       tiles.push_back(row);
                       }
               
               out<<"Case #"<<++cas<<": \n";
               solve(tiles);
               out<<endl;
               
               }
 
 return 0;   
}
