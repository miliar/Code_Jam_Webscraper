#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

int main()
{
    int T;
    cin >> T;

    cout.setf(ios::fixed);

    for(int i = 0; i < T; i ++)
    {
        int N;
        cin >> N;

        vector<int> elements(N);
        for(int j = 0; j < N; j ++)
            cin >> elements[j];

        vector<int> sortElement(elements);

        sort(sortElement.begin(), sortElement.end());
        int count = 0;

        for(int j = 0; j < N; j ++)
            if(elements[j] != sortElement[j])
                count ++;

        cout << "Case #" << i + 1 << ": ";
        
        if(N == 1)
            cout << "0.000000" << endl;
        else
            cout << setprecision(6) << float(count) << endl;

    }
    return 0;
}

