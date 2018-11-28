#include <iostream>

using namespace std;

int main()
{
    int coden, t;
    cin >> t;
    // define vars
    long long c, d;
    long long vendornum[210];
    long long sumvendornum[210];
    long long vendorpoint[210];

    for (coden = 1; coden <= t; coden++)
    {
        cin >> c >> d;
        d *= 2;
        sumvendornum[0] = 0;
        for (long long i = 0; i < c; i++) {
            cin >> vendorpoint[i] >> vendornum[i];
            vendorpoint[i] *= 2;
            sumvendornum[i+1] = sumvendornum[i] + vendornum[i];
        }
        
        long long maxtime = 0;
        for (long long i = 0; i < c; i++)
        for (long long j = i; j < c; j++)
        {
            // find out #i ~ #j points (including #i and #j)
            long long total = (sumvendornum[j+1] - sumvendornum[i] - 1) * d;
            long long ori = vendorpoint[j] - vendorpoint[i];

            // time = 0;
            if (total - ori < 0)
                continue;

            if ((total - ori) % 2 != 0) {
                cerr << "total = " << total << endl;
                cerr << "ori = " << ori << endl;
            }
            assert ((total - ori) % 2 == 0);
            long long mvtime = (total - ori) / 2;
            if (mvtime > maxtime)
                maxtime = mvtime;
        }

        // output result
        cout << "Case #" << coden << ": ";
        if ((maxtime % 2) == 0) {
            cout << (maxtime/2) << ".0";
        } else {
            cout << ((maxtime-1)/2) << ".5";
        }
        cout << endl;
    }
    return 0;
}

