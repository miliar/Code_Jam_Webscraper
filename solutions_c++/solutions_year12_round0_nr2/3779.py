#include <iostream>
#include <algorithm>

using namespace std;

int mark[105];

int main()
{
    //p mark need to acheive
    //s suprising case
    //n number of googlers
    int t, s, p, n , temp, ans;
    cin >> t;
    for (int i = 0 ;i < t ; i++)
    {
        ans = 0;
        cin >> n >> s >> p;
        for (int j = 0 ; j < n; j++)
            cin >> mark[j];
        
        sort(mark, mark+n);
        
        for(int j= n - 1 ; j>=0 ; j--)
        {
            if (mark[j] - p >= 0)
            {
                if ((mark[j]-p) >= ((p-1) * 2))
                {
                    ans ++;
                    continue;
                }
                else if (mark[j]- p >= ((p-2) * 2) && s > 0)
                {
                    ans ++;
                    s --;
                    continue;
                }
            }
        }
        cout << "Case #" << i + 1 << ": " << ans << endl;
    }
}