#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int cs = 1; cs <= T; ++cs)
    {
        string a;
        cin >> a;
        if (!next_permutation(a.begin(), a.end()))
        {
            char f;
            sort(a.begin(), a.end());
            for (int i = 0; i < a.size(); ++i)
                if (a[i] != '0')
                {
                    f = a[i];
                    a[i] = '0';
                    break;
                }
            a = string(1, f) + a;
        }
        cout << "Case #" << cs << ": " << a << endl;
    }
    return 0;
}