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
map< string, int > mm;

int solve(string str)
{   
    //cout<<endl<<"Finding : "<<str;
    if(str == "") return 0;
    if(present(mm, str)) return 0;
    
    int len = str.length();
    int i;
    for(i = len - 1; i >= 0; i--)
        if(str[i] == '/')
            break;
            
    string str2 = "";    
    for(int j = 0; j < i; j++)
        str2 += str[j];
        
    return mm[str] = solve(str2) + 1;
}
int main()
{
    int t, cases = 1, n, m, ans;
   
    cin >> t;
    string str;
   
    while(cases <= t){
        cin >> n >> m;
        mm.clear();
              
        for(int i = 0; i < n; i++){
            cin >> str;
            mm[str] = 1;
        }
        
        ans = 0;
        for(int i = 0; i < m; i++){
            cin >> str;           
            ans += solve(str);   
        }
        cout<<"Case #"<<cases<<": "<<ans;                      
        cout<<endl;
        cases++;            
    }
    
    return 0;   
}
