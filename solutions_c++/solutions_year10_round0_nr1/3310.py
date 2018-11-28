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
    int n, k, t1, t2, t3, cases;
    
    cin >> cases;
    
    int i = 1;
    while(i <= cases){
        cin >> n >> k;
        cout<<"Case #"<<i<<": ";
        t1 = (int)pow((double)2, (double)n);
        
        t3 = k - t1 + 1;
        
        if(t3 < 0) cout<<"OFF";
        else if(t3 % t1 == 0) cout<<"ON";
        else cout<<"OFF";
        
        cout<<endl;
        i++;
    }
    return 0;   
}
