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
    int t, cases = 1;
   
    cin >> t;

    int n, ans;
    int A[1001], B[1001];
    
    while(cases <= t){
        
        cin >> n;
        ans = 0;
        for(int i = 0; i < n; i++){
            cin >> A[i] >> B[i];
            
            for(int j = 0; j < i; j++){
                if( (A[j] < A[i] && B[j] > B[i]) || (A[j] > A[i] && B[j] < B[i]) )
                    ans++;
            }        
        }
        cout<<"Case #"<<cases<<": "<<ans;                      
        cout<<endl;
        cases++;            
    }
    
    return 0;   
}
