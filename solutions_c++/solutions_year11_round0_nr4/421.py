#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int t, n;
    int *array;
    double counter;

    cin >> t;

    for (int i = 0; i < t; i++)
    {
        cin >> n;
        array = new int[n];
        counter = 0.0;

        for (int j = 0; j < n; j++)
        {
            cin >> array[j];
            if (array[j] != j + 1)
                counter += 1.0;
        }

        cout << "Case #" << i + 1 << ": " << fixed
            << setprecision(6) << counter << endl;

        delete [] array;
    }

    return 0;
}
