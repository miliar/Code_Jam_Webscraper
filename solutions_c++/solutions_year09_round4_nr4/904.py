#include <algorithm>
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main(int argc, char** argv)
{
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i)
    {
        int N;
        cin >> N;
        vector <vector <int> > circles;
        for (int j = 0; j < N; ++j)
        {
            vector <int> t(3);
            cin >> t[0] >> t[1] >> t[2];
            circles.push_back(t);
        }
        if (circles.size() == 1)
            cout << "Case #" << (i + 1) << ": " << circles[0][2] << endl;
        else if (circles.size() == 2)
            cout << "Case #" << (i + 1) << ": "
                 << max(circles[0][2], circles[1][2]) << endl;
        else
        {
            vector <double> r(3);
            r[0] = max((double)circles[0][2],
                   (pow(pow(circles[1][0] - circles[2][0], 2.0)
                 + pow(circles[1][1] - circles[2][1], 2.0), 0.5)
                 + circles[1][2] + circles[2][2]) / 2);
            r[1] = max((double)circles[1][2],
                   (pow(pow(circles[0][0] - circles[2][0], 2.0)
                 + pow(circles[0][1] - circles[2][1], 2.0), 0.5)
                 + circles[0][2] + circles[2][2]) / 2);
            r[2] = max((double)circles[2][2],
                   (pow(pow(circles[1][0] - circles[0][0], 2.0)
                 + pow(circles[1][1] - circles[0][1], 2.0), 0.5)
                 + circles[1][2] + circles[0][2]) / 2);
            cout << "Case #" << (i + 1) << ": "
                 << *min_element(r.begin(), r.end()) << endl;
        }
    }
    return 0;
}