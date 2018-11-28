#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <ctime>
 
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
using namespace std; 



int main()
{
    int t, n, k, cases = 1;
    
    cin >> t;
    
    while(cases <= t){
                
                cin >> n >> k;
                char orig[n][n];
                int lr[2][n][n], rl[2][n][n], vert[2][n][n], horiz[2][n][n];
                for(int i = 0; i < 2; i++)
                        for(int j = 0; j < n; j++)
                                for(int k = 0; k < n; k++){
                                        lr[i][j][k] = 0;
                                        rl[i][j][k] = 0;
                                        vert[i][j][k] = 0;        
                                        horiz[i][j][k] = 0;
                                }
              
                for(int i = 0; i < n; i++)
                        for(int j = 0; j < n; j++)
                                cin >> orig[i][j];
                        
                
          
                for(int i = 0; i < n; i++){
                        int right = n - 1, left = n - 1;                        
                        while(left >= 0 && right >= 0){
                                if(orig[i][right] == '.'){
                                         if(orig[i][left] == '.')
                                                 left--;
                                         else{
                                              orig[i][right] = orig[i][left];
                                              orig[i][left] = '.';
                                              right--;
                                              left--;     
                                         }                 
                                }
                                else{
                                     right--;
                                     if(left > right)
                                             left--;     
                                }
                                        
                        }                              
                }
            
                
                bool B = false, R = false;
                for(int i = 0; i < n; i++){
                        for(int j = 0; j < n; j++){
                                if(orig[i][j] != '.'){
                                        if(i-1 >= 0 && j-1 >= 0){
                                               if(orig[i-1][j-1] == orig[i][j]){
                                                       if(orig[i][j] == 'B')
                                                               rl[0][i][j] = rl[0][i-1][j-1] + 1;
                                                       else
                                                               rl[1][i][j] = rl[1][i-1][j-1] + 1;
                                               }
                                               else{
                                                    if(orig[i][j] == 'B')
                                                               rl[0][i][j] = 1;
                                                       else
                                                               rl[1][i][j] = 1;
                                               }
                                                       
                                                      
                                        }  
                                        else{
                                                    if(orig[i][j] == 'B')
                                                               rl[0][i][j] = 1;
                                                       else
                                                               rl[1][i][j] = 1;
                                        }
                                        if(i-1 >= 0 && j+1 < n){
                                               if(orig[i-1][j+1] == orig[i][j]){
                                                       if(orig[i][j] == 'B')
                                                               lr[0][i][j] = lr[0][i-1][j+1] + 1;
                                                       else       
                                                               lr[1][i][j] = lr[1][i-1][j+1] + 1;
                                               }
                                               else{
                                                    if(orig[i][j] == 'B')
                                                               lr[0][i][j] = 1;
                                                       else       
                                                               lr[1][i][j] = 1;
                                               }
                                        }
                                        else{
                                                    if(orig[i][j] == 'B')
                                                               lr[0][i][j] = 1;
                                                       else       
                                                               lr[1][i][j] = 1;
                                        }
                                        if(i-1 >= 0){
                                               if(orig[i-1][j] == orig[i][j]){
                                                       if(orig[i][j] == 'B')
                                                               vert[0][i][j] = vert[0][i-1][j] + 1;       
                                                       else
                                                               vert[1][i][j] = vert[1][i-1][j] + 1;
                                               }
                                               else{
                                                    if(orig[i][j] == 'B')
                                                               vert[0][i][j] = 1;       
                                                       else
                                                               vert[1][i][j] = 1;
                                               }
                                        }
                                        else{
                                                    if(orig[i][j] == 'B')
                                                               vert[0][i][j] = 1;       
                                                       else
                                                               vert[1][i][j] = 1;
                                        }
                                        if(j-1 >= 0){
                                               if(orig[i][j-1] == orig[i][j]){
                                                       if(orig[i][j] == 'B')
                                                               horiz[0][i][j] = horiz[0][i][j-1] + 1;
                                                       else                
                                                              horiz[1][i][j] = horiz[1][i][j-1] + 1;
                                               }
                                               else{
                                                    if(orig[i][j] == 'B')
                                                               horiz[0][i][j] = 1;
                                                       else                
                                                              horiz[1][i][j] = 1;
                                               }
                                        }
                                        else{
                                                    if(orig[i][j] == 'B')
                                                               horiz[0][i][j] = 1;
                                                       else                
                                                              horiz[1][i][j] = 1;
                                               }
                                               
                                }
                                
                                if(rl[0][i][j] == k || lr[0][i][j] == k || vert[0][i][j] == k || horiz[0][i][j] == k)
                                               B = true;
                                if(rl[1][i][j] == k || lr[1][i][j] == k || vert[1][i][j] == k || horiz[1][i][j] == k)
                                               R = true;
                                               
                        }        
                        
                }
                
              
                cout<<"Case #"<<cases<<": ";
                
                if(B && R) cout<<"Both";
                else if(B) cout<<"Blue";
                else if(R) cout<<"Red";
                else       cout<<"Neither";               
                cout<<endl;
                cases++;            
    }
    
    return 0;   
}
