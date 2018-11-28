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
string ref = "welcome to code jam";
string str;
int ans, len;
vector< vector<int> > grid;

int dfs(int from, int refi)
{
    if(refi == 19) return 1;
    
    int cnt = 0;
    
    for(int a = from; a < len; a++)
    {
            if(str[a] == ref[refi])
                      cnt += dfs(a+1, refi+1);        
    }
    
    return cnt % 10000;
}

int main()
{
    int n;
    cin >> n;    
    getline(cin, str, '\n');
    
    for(int i = 1; i <= n; i++){
 
            getline(cin, str, '\n');
            ans = 0;
            
            
            len = sz(str);
 
            grid.clear();
            grid.resize(len, vector<int> (len, 0));
            
           
            for(int k = 0; k < len; k++)
            {
               if(str[k] == 'w')
                         ans += dfs(k+1, 1);        
            }
            
                   
            

            //cout<<"Case #"<<i<<": "<<ans;
            //cout<<endl;
            
            ostringstream sout;
            sout<<ans;
            
            string app( 4 - sz(sout.str()),'0');
            
            cout<<"Case #"<<i<<": "<<app<<sout.str();
            cout<<endl;
    }
    return 0;    
}
