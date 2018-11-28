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

vector<string> inp;

int main()
{
    int l,d,n;
    cin >> l >> d >> n;
    
    int len;
    string str;
    for(int i = 0; i < d; i++){
            cin >> str;
            inp.pb(str);
    }    
    sort(all(inp));
    
    
    for(int i = 1; i <= n; i++)
    {
            vector<int> ans(d, 0);
            
            cin >> str;   
            len = sz(str);
            
            int curcnt = 0;
            for(int a = 0; a < len; a++){
                    vector<char> cand;
                    if(str[a] == '('){
                              a++;
                              while(str[a] != ')'){
                                           cand.pb(str[a]);
                                           a++;
                              }
                    }
                    else
                        cand.pb(str[a]);
                        
                    
                    
                    for(int z = 0; z < d; z++){
                            if(cpresent(cand, inp[z][curcnt]))
                                              ans[z]++;        
                    }
                    curcnt++;
                    
            }     
            
            
            
            cout<<"Case #"<<i<<": "<<count(all(ans), l);
            cout<<endl;
            
    } 
    return 0;    
}
