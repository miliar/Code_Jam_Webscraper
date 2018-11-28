#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    //freopen("C-small.in", "r", stdin);
    freopen("C-small-attempt0.in", "r", stdin);
    //freopen("C-large.in", "r", stdout);
    freopen("C-small.out", "w", stdout);
    //freopen("C-large.out", "w", stdout);
    
    int T;
    int A, B;
    int tmp[100];
    
    cin >> T;
    int n, p;
    
    for (int t = 1; t <= T; ++t)
    {
        cin >> A >> B;
        n = 0; int x = A;
        p = 1;
        if (A == 0) n = 1;
        else while (x > 0) {n++; x /= 10;}
        
        for (int i = 1; i <= n - 1; ++i) p *= 10;
        
        int ans = 0;
        
        if (n > 1)
        { 
            for (int x = A; x <= B; ++x)
            {
                int cur = x, cnt = 0;
                for (int i = 1; i <= n - 1; ++i)
                {
                    int pre = cur;
                    cur = (cur % 10) * p + cur / 10;
                    if (pre % 10 == 0 || cur > B || cur <= x) continue;
                        
                        bool found = false;
                        for (int j = 0; j < cnt; ++j)
                            if (tmp[j] == cur)
                            {
                                found = true;
                                break;
                            }
                        if (!found)
                        {
                            ans++; tmp[cnt++] = cur;
                        }
                } 
            }
        }
        
        cout << "Case #" << t << ": " << ans << endl;
    }
    
    return 0;
}
