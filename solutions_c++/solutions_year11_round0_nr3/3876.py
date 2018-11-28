#include <iostream>
using namespace std;
 
int main()
{
        int T;
        cin >> T;
        for (int tc=1; tc<=T; tc++)
        {
                int n;
                cin >> n;
                int *a = new int[n];
                for (int i=0; i<n; i++)
                        cin >> a[i];
                int res = 0;
                int vmin = 10e7;
                int sum = 0;
                for (int i=0; i<n; i++)
                {
                        if (a[i] < vmin)
                                vmin = a[i];
                        res ^= a[i];
                        sum += a[i];
                }
                if (res != 0)
                        cout << "Case #" << tc << ": NO" << endl;
                else
                        cout << "Csse #" << tc << ": " << (sum - vmin) << endl;
        }
        return 0;
}