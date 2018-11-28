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
    long long r, k, n, ans, cur;
    int cases;
    vector<int> arr; 
    vector<bool> available;   

    cin >> cases;
    
    int i = 1;
    while(i <= cases){
        cin >> r >> k >> n;

        arr.clear();
        arr.resize(n, 0);

        available.clear();
        available.resize(n, true);
        
        for(int j = 0; j < n; j++)
                cin >> arr[j];

        cout<<"Case #"<<i<<": ";
        ans = 0;
        int cntr = 0;
        while(r){
                 cur = 0;
                 while(cur <= k){
                           if(available[cntr] && k - cur >= arr[cntr]){
                                cur += arr[cntr];
                                available[cntr] = false;
                                cntr += 1;
                                cntr %= n;
                           }
                           else{
                                
                                ans += cur;
                                available.clear();
                                available.resize(n, true);
                                break;     
                           }     
                 }
                 r--;
        }
        cout<<ans;
        cout<<endl;
        i++;
    }
    return 0;   
}
