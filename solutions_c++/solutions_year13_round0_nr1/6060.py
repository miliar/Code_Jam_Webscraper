# include <iostream>
# include <string>
# include <vector>
using namespace std;

int check_row(vector<string> v, int j, int k)
{
    char ch;
    
    if(v[j][k] == '.'){
               return 0;
    } else if (v[j][k] != 'T'){
           ch = v[j][k];
    } else if (v[j][k+1] == '.'){
           return 0;
    } else {
           ch = v[j][k+1];
    }
    int cnt = 0;
    for (int p = k; p < 4; p++){
        if(v[j][p]  == ch || v[j][p]== 'T'){
                   cnt++;
        }
    }
    
    if(cnt == 4){
           if(ch == 'X'){
                 return 1;
           } else if (ch == 'O'){
                  return 2;
           }
    }
    
    return 0;
}


int check_col(vector<string> v, int j, int k)
{
    char ch;
    if(v[j][k] == '.'){
               return 0;
    } else if (v[j][k] != 'T'){
           ch = v[j][k];
    } else if ( v[j+1][k] == '.'){
           return 0;
    } else if (v[j+1][k] != 'T'){
           ch = v[j+1][k];
    }
    
    int cnt = 0;
    
    for (int p = j; p < 4; p++){
        if(v[p][k]== ch || v[p][k]== 'T'){
                   cnt++;
        }
    }
    
    if(cnt == 4){
           if(ch == 'X'){
                 return 1;
           } else if (ch == 'O'){
                  return 2;
           }
    }
    
    return 0;
}

int check_diag(vector<string> v, int j, int k)
{
    
    
    if(j == 0 && k == 0){
         
            char ch;
            if(v[j][k] == '.'){
               return 0;
            } else if(v[j][k] != 'T'){
               ch = v[j][k];
            } else if ( v[1][1] == '.'){
                   return 0;
            } else {
                   ch =  v[1][1] ;
            }
            
            int cnt = 0;
            for (int p = 0; p < 4; p++){
                if(v[p][p] == ch || v[p][p] == 'T'){
                           cnt++;
                }
            }
            
            if(cnt == 4){
                   if(ch == 'X'){
                         return 1;
                   } else if (ch == 'O'){
                          return 2;
                   }
            }
            return 0;
    } else if (j == 0 && k == 3) {
           
           char ch;
           if(v[j][k] == '.'){
                      return 0;
           } else if (v[j][k] != 'T'){
                  ch = v[j][k];
           } else if (v[1][2] == '.'){
                  return 0;
           } else if (v[1][2] != 'T'){
                  ch = v[1][2];
           }
           
           int cnt = 0;
           
           for (int p = 0; p < 4; p++){
               if(v[p][3-p] == ch || v[p][3-p] == 'T') {
                            cnt++;
               }
           }
           
           if(cnt == 4){
                  if(ch == 'X'){
                        return 1;
                  } else if (ch == 'O') {
                         return 2;
                  }
           }
           
           return 0;
    }
}
                            
                   
                       
    
    
    
    
int main()
{
    int t;
    cin >> t;
    
    for (int i = 0; i < t; i++){
        vector<string> v;
        string s;
        
        for (int j = 0; j < 4; j++){
            cin >> s;
            v.push_back(s);
        }
        bool draw = true;
        int flag = 0;
        for (int j = 0; j < 4; j++){
            for (int k = 0; k < 4; k++){
                
              //  cout << "for " << j <<" " << k <<" ";
                if(v[j][k] == '.'){
                           draw = false;
                }
                if(j == 0 && flag == 0){
                 flag = check_col(v,j,k);
                // cout << "col " << flag << endl;
                 }  
                if (k == 0 && flag == 0){
                  flag =  check_row(v,j,k);
                 // cout << "row" << flag << endl;
                }
                if(((j == 0 && k == 0) || (j == 0 && k == 3)) && flag == 0){
                    flag = check_diag(v,j,k);
                   // cout << "diag" << flag << endl;
                }
                
                
                if(flag != 0){
                        break;
                }
            }
            if(flag != 0){
                    break;
            }
        }
        
        cout << "Case #" << i+1 <<": " ;
        if(flag == 0 && draw == false) {
                cout << "Game has not completed" << endl;
        } else if (flag == 0 && draw == true){
               cout << "Draw" << endl;
        } else if (flag == 1){
               cout << "X won" << endl;
        } else if (flag == 2){
               cout << "O won" << endl;
        }
    }
    return 0;
}
