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
vector<long long> arr;

long long solve(long long start, long long end)
{
    long long mid = start + (end - start) / 2;   
    if(mid == start) return 0;
    
    if(end - mid > mid - start)
        return solve(mid, end) + 1;
    return solve(start, mid) + 1;
}


int main()
{
    int t, cases = 1;
   
    cin >> t;

    long long L, P, temp;
    int C;
    
    while(cases <= t){
                
        cin >> L >> P >> C;
        arr.clear();
        
        arr.pb(L);
        temp = L;
        while(temp*C < P){
            temp *= C;
            arr.pb(temp);   
        }
        arr.pb(P);
        //cout<<endl;
        //tr(arr, itr) cout<<*itr<<" ";
        //cout<<endl;
        cout<<"Case #"<<cases<<": "<<solve(0, sz(arr)-1);                      
        cout<<endl;
        cases++;            
    }
    
    return 0;   
}
