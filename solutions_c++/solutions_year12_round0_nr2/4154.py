#include <iostream>
#include <fstream>
#include <stdio.h>
using namespace std;
int main()
{
    ifstream in("B-large.in");
    cin.rdbuf(in.rdbuf());
    
    int N;
    cin >> N;
    for (int T=0; T<N; ++T)
    {
        int n, a, b;
        cin >> n >> a >> b;
        int ans= 0;
        
        for (int i=0; i<n; ++i)
        {
            int t;
            cin >> t;
            if (t>= 3*b-2)
                ans ++;
            else if (b>1 && t>=3*b-4 && a>0)
            {
                a--;
                ans++;
            }
        }

        printf("Case #%d: %d\n", T+1, ans);
    }
}
