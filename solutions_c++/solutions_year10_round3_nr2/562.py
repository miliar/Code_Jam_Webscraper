#include <iostream>
#include <vector>

using namespace std;



int main()
{
    int T, L, P, C;
    cin >> T;

    for (int i=1;i<=T;i++)
    {
        int power = 0;
        int compare = 2;
        vector<int> test_cases;
        cin >> L;
        cin >> P;
        cin >> C;
        int curr_test = L*C;

        while (curr_test < P)
        {
            test_cases.push_back(curr_test);
            curr_test = curr_test * C;
        }

        while (compare <= ((int) test_cases.size()))
        {
            power++;
            compare *= 2;
        }

        if (test_cases.size() == 0)
        {
            cout << "Case #" << i << ": " << (int) 0 << endl;
        }
        else
        {
            cout << "Case #" << i << ": " << (power + 1) << endl;
        }
    }
    return 1;
}
