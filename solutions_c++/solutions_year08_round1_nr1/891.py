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
    int cases;
    cin >> cases;
    int n, t, m;
    int cnt = 1;
    while(cases--)
    {
        cin >> n;
        vector<int> a(n, 0);
        vector<int> b(n, 0);
        
        for(int i = 0; i < n; i++)
                cin >> a[i];
        for(int i = 0; i < n; i++)
                cin >> b[i];
                
        sort(all(a));
        sort(all(b));
        
        /*m = 8000010;
        do{
            do{
                     t = 0;
                     for(int i = 0; i < n; i++)
                         t += a[i] * b[i];
                     if(t < m) m = t;    
            }while(next_permutation(all(b)));
        }while(next_permutation(all(a)));
         */
        m = 0; 
        for(int i = 0; i < n; i++)
                m += a[i] * b[n-1-i];         
        cout<<"Case #"<<cnt<<": "<<m<<endl;
        cnt++;
    }
    return 0;
}

