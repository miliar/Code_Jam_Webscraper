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
    int n, len, j;
    cin  >> n;
    vector<int> c;
    string str;
    for(int i = 1; i <= n; i++){
            cin >> str;
            len = sz(str);
            c.clear();
            
            for(j = len; j < 23; j++)
                    c.pb(0);
                    
            for(j = 0; j < len; j++)
                    c.pb(str[j] - '0');
                    
                      
            //tr(c, itr) cout<<*itr<<" ";
            //cout<<endl;
            next_permutation(all(c));            
            //tr(c, itr) cout<<*itr<<" ";
            //cout<<endl;
            //cout<<endl<<sz(c);
            cout<<"Case #"<<i<<": ";
            for(j = 0; j < 23; j++)
                    if(c[j] != 0)
                            break;
            while(j < 23){
                    cout<<c[j];
                    j++;
            }
            cout<<endl;
    }
    return 0;    
}
