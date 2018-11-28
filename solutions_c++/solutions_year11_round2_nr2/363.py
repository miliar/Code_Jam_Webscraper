#include <iostream>
#include <iomanip>

using namespace std;

typedef struct
{
    int position;
    int vendor;
} point;

int main()
{
    int t, c;
    long long int d;
    point *p;

    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> c >> d;
        p = new point[c];

        for (int j = 0; j < c; j++)
            cin >> p[j].position >> p[j].vendor;

        int distance, vendors;
        double maxTime = 0.0;

        for (int j = 1; j <= c; j++)
        {
            for (int k = 0; k <= c - j; k++)
            {
                vendors = 0;
                distance = p[k+j-1].position - p[k].position;
                for (int m = k; m < k+j; m++)
                    vendors += p[m].vendor;

                if ((double)((vendors - 1) * d - distance) / 2 > maxTime)
                    maxTime = (double)((vendors - 1) * d - distance) / 2;
            }
        }

        cout << "Case #" << i + 1 << ": " << fixed << setprecision(1) << maxTime << endl;

        delete [] p;
    }

    return 0;
}
