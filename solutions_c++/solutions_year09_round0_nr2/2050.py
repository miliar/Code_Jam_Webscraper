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
 
#include <conio.h> 
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
using namespace std; 

vector< vector<int> > grid;
vector< vector<char> > ans;
vector< vector<bool> > visited;
char availbasin;
int t, h, w;
int n;

bool isvalid(int x, int y)
{
     if(x < 0 || x >= h) return false;
     if(y < 0 || y >= w) return false;     
     
     return true;
}

/*
bool canflow(int fromx, int fromy, int tox, int toy)
{
     if(!isvalid(fromx, fromy)) return false;
     if(!isvalid(tox, toy)) return false;
     
     
     cout<<endl<<"trying for ("<<fromx<<", "<<fromy<<") to ("<<tox<<", "<<toy<<")";
     
     int x, y;
     
     x = fromx-1;
     y = fromy;
     
     if(!(x == tox && y == toy)){
            if(isvalid(x, y) && grid[x][y] <= grid[tox][toy])
                          return false;       
     }

     x = fromx;
     y = fromy-1;
     
     if(!(x == tox && y == toy)){
            if(isvalid(x, y) && grid[x][y] <= grid[tox][toy])
                          return false;       
     }
     
     x = fromx+1;
     y = fromy;
     
     if(!(x == tox && y == toy)){
            if(isvalid(x, y) && grid[x][y] <= grid[tox][toy])
                          return false;       
     }
     
     x = fromx;
     y = fromy+1;
     
     if(!(x == tox && y == toy)){
            if(isvalid(x, y) && grid[x][y] <= grid[tox][toy])
                          return false;       
     }
     cout<<endl<<"can flow from ("<<fromx<<", "<<fromy<<") to ("<<tox<<", "<<toy<<")";
     return true;
}
*/
bool canflow(int fromx, int fromy, int tox, int toy)
{
     if(!isvalid(fromx, fromy)) return false;
     if(!isvalid(tox, toy)) return false;
     
     //cout<<endl<<"Checking for ("<<fromx<<", "<<fromy<<") to ("<<tox<<", "<<toy<<")";
     
     int x, y;
     int curx = 100000000, cury = 10000000, curmin;
     curmin = grid[fromx][fromy];
     
     x = fromx - 1;
     y = fromy;
     
     if(isvalid(x, y) && grid[x][y] < curmin){
          curmin = grid[x][y];
          curx = x;
          cury = y;             
     }
     
     x = fromx;
     y = fromy - 1;
     
     if(isvalid(x, y) && grid[x][y] < curmin){
          curmin = grid[x][y];
          curx = x;
          cury = y;             
     }
     
     x = fromx;
     y = fromy + 1;   
     
     if(isvalid(x, y) && grid[x][y] < curmin){
          curmin = grid[x][y];
          curx = x;
          cury = y;             
     }
     
     x = fromx + 1;
     y = fromy;
     
     if(isvalid(x, y) && grid[x][y] < curmin){
          curmin = grid[x][y];
          curx = x;
          cury = y;             
     }
     
     
     
     if(curx == tox && cury == toy) return true;
     //cout<<endl<<"can not flow : curx "<<curx<<" cury "<<cury;
     return false;  
}

bool doit(int x, int y)
{
     if(isvalid(x, y) && visited[x][y]) return false;
     
     visited[x][y] = true;
     //char c;
     //cout<<endl<<"doing for "<<x<<" "<<y;
     //getch();
     if(canflow(x, y, x-1, y) || canflow(x-1, y, x, y)){
                   ans[x-1][y] = availbasin;
                   doit(x-1, y);
     }
     //cout<<endl<<"still in "<<x<<" "<<y;
     if(canflow(x, y, x, y-1) || canflow(x, y-1, x, y)){
                   ans[x][y-1] = availbasin;
                   doit(x, y-1);              
     }
     
     if(canflow(x, y, x, y+1) || canflow(x, y+1, x, y)){
                   ans[x][y+1] = availbasin;
                   doit(x, y+1);              
     }
     
     if(canflow(x, y, x+1, y) || canflow(x+1, y, x, y)){
                   ans[x+1][y] = availbasin;
                   doit(x+1, y);              
     }
     
     
     
     return true;
}

int main()
{
    
    cin >> t;
    

    for(int i = 1; i <= t; i++){
            
            cin >> h >> w;
            grid.clear();
            grid.resize(h, vector<int> (w, 0));
            ans.clear();
            ans.resize(h, vector<char> (w, '1'));
            visited.clear();
            visited.resize(h, vector<bool> (w, false));
            
            vector<int> temp;
            for(int a = 0; a < h; a++)
                    for(int b = 0; b < w; b++){                           
                            cin  >> grid[a][b];               
                    }
                     
            
            
            
            cout<<"Case #"<<i<<":";
            cout<<endl;
            
               
            
            
            ans[0][0] = 'a';
            availbasin = 'a';
            doit(0, 0);
            availbasin = 'b'; 
            
            for(int a = 0; a < h; a++)
                    for(int b = 0; b < w; b++)
                            if(ans[a][b] == '1'){
                                         ans[a][b] = availbasin;                                         
                                         doit(a, b);
                                         availbasin++;
                            }            
            
            
            for(int a = 0; a < h; a++)
            {
                    for(int b = 0; b < w; b++)
                    {
                            cout << ans[a][b] << " ";                 
                    }        
                    cout<<endl;
            }         
            
    }
    return 0;    
}
