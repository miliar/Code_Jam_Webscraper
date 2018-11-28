#include <iostream>

using namespace std;

int a[128][128];

int main()
{
    int t;
    cin >> t;
    for (int tt=1; tt<=t; tt++)
    {
        int k;
        cin >> k;

        for (int i=0, j=0; ; )
        {
            cin >> a[i][j];

            j--, i++;
            if (i >= k)
            {
                i = i+j - (k-1) + 1;
                j = k-1;
            }
            if (j < 0)
            {
                j = i;
                i = 0;
            }
            if (i+j >= k+k-1)
                break;
        }

        int ans;
        bool f = false;
        for (ans = k; !f; ans++)
            for (int x=0; x<=ans-k && !f; x++)
                for (int y=0; y<=ans-k && !f; y++)
                {
                    f = true;
                    for (int i=0; i<k && f; i++)
                        for (int j=0; j<k && f; j++)
                        {
                            int u = j+y-x;
                            int v = i+x-y;
                            if (u >= 0 && u < k && v >= 0 && v < k && a[i][j] != a[u][v])
                                f = false;

                            u = ans-1-(j+y)-x;
                            v = ans-1-(i+x)-y;
                            if (u >= 0 && u < k && v >= 0 && v < k && a[i][j] != a[u][v])
                                f = false;
                        }
                }

        ans--;
        cout << "Case #" << tt << ": " << ans*ans - k*k << endl;
    }
    return 0;
}
