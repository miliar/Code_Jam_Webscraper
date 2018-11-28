#include <fstream>
#include <iostream>
using namespace std;

int n;
long long k, r;
long long num[1001], sum[1001];

int main()
{
    ifstream input;
    ofstream output;
    input.open("Csmall.in");
    output.open("Csmall.out");
    int t, i, last, left, right, mid, ca = 0;
    long long tot, val, ans;
    input >> t;
    while (t > 0)
    {
        input >> r >>  k >> n;
        for (i = 1; i <= n; i++) input >> num[i];
        sum[0] = 0;
        for (i = 1; i <= n; i++) sum[i] = sum[i - 1] + num[i];
        output << "Case #" << ++ca << ": ";
        if (k >= sum[n]) output << r * sum[n] << endl;
        else
        {
            ans = 0;
            last = 0;
            for (i = 1; i <= r; i++)
            {
                if (k >= sum[n] - sum[last])
                {
                    val = sum[n] - sum[last];
                    left = 1; right = last;
                    last = 0;
                }
                else
                {
                    val = 0;
                    left = last + 1; right = n;
                }
                if (sum[left] - sum[last] > k - val) {   ans = ans + val;  last = left - 1;   }
                else
                {
                    while (left < right)
                    {
                        mid = (left + right + 1) >> 1;
                        if (sum[mid] - sum[last] > k - val) right = mid - 1; else left = mid;
                    }
                    ans = ans + val + sum[left] - sum[last];
                    last = left;
                }
                //cout << ans << endl;
            }
            output << ans << endl;
        }
        t--;
    }
    input.close();  output.close();
    return 0;
}
