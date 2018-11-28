#include <iostream>
#include <vector>
#include <set>
#include <map>
using namespace std;

typedef long long LL;

const int MAXN = 512;

int N;
LL nums[MAXN];

set<LL> poss;
set<LL> next;
map<LL, LL> before;

void solve(int test)
{
    printf("Case #%d:\n", test); 
     
    sort(nums, nums + N); 
    
    bool found = false;
    
    before.clear();
    poss.clear();
    poss.insert(0);
    for (int i = 0; i < N; i++)
    {
        set<LL>::iterator p = poss.begin();
        
        next = poss;
        while (p != poss.end())
        {
            //cout << *p << " ";  
            LL A = *p + nums[i];
            LL B = *p - nums[i];
            
            if (before.count(A) == 0) before[A] = nums[i];
            if (before.count(B) == 0) before[B] = -nums[i];
            
            if (A == 0)
            {
                found = true;
                break;  
            }
            
            if (B == 0)
            {
                found = true;  
                break;
            }
            
            next.insert(A);
            next.insert(B);
              
            p++;  
        }
        
        if (found) break;
                
        poss = next;
    }
    
    if (!found) { cout << "Impossible" << endl; return; }
    
    vector<LL> one, two;
    
    LL cur = 0;
    for (;;)
    {
        cur -= before[cur];
        if (before[cur] < 0) one.push_back(before[cur]); else two.push_back(before[cur]);
        
        if (cur == 0) break;
    }    
    
    for (int i = 0; i < one.size(); i++)
    {
        if (i > 0) cout << " ";
        
        cout << abs(one[i]);
    }
        
    cout << endl;
    
    for (int i = 0; i < two.size(); i++)
    {
        if (i > 0) cout << " ";        
        cout << abs(two[i]);
    }
        
    cout << endl;
}

int main()
{
    int T; cin >> T;
    
    for (int t = 1; t <= T; t++)
    {
        cin >> N;
        for (int i = 0; i < N; i++) cin >> nums[i];        
        
        solve(t);
    }
    
    return 0;
}
