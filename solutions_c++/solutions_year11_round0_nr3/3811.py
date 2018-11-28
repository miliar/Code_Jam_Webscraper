# include <iostream>
# include <cstdio>
# include <algorithm>
# include <vector>
# include <map>
# include <fstream>
# include <sstream>

using namespace std;

bool visited[20];
int maks;

bool valid(vector<int> vi, int sum, int nsum){
               int s = 0;
               int c = 0;
               
               for(int i = 0; i<vi.size(); ++i){
                       if(!visited[i]){
                                       s^=vi[i];
                                       c++;
                            }
                       }
                       
               if(s == sum && c != 0){
                    return true;
                    }
                    return false;
     }

void solve(vector<int> vi, int lvl, int xsum, int nsum){
           
    if(valid(vi, xsum, nsum)){
                   if(nsum > maks){
                        maks = nsum;
                        }
         }
        
    for(int i = lvl; i < vi.size(); ++i){
              if(!visited[i]){
                   visited[i]=true;
                   solve(vi, i+1, xsum^vi[i], nsum+vi[i]);
                   visited[i]=false;
                   }
            }    
}

int main()
{
    ifstream in("C-small-attempt0.in");
    ofstream out("C-small-output");
 
 int T, cas = 0;
 in>>T;
 
 while(T--){
            
            int N;
            vector<int> vi; 
            int inp;
            memset(visited, 0, sizeof(visited));
            maks = -1;
            
            in>>N;
            for(int i = 0; i < N; ++i){
                    in>>inp;
                    vi.push_back(inp);
                    }
                    
                    out<<"Case #"<<++cas<<": ";
                    solve(vi, 0, 0, 0);
                    
                    if(maks < 0){
                                        out<<"NO";
                                        }
                    else {
                                        out<<maks;
                         }
                    out<<endl;
            }
 
 return 0;   
}
