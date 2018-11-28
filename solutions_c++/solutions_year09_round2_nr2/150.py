#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int tt=1; tt<=t; tt++)
    {
        string s;
        cin >> s;

        if (!next_permutation(s.begin(), s.end()))
        {
            sort(s.begin(), s.end());

            int i;
            for (i=0; s[i] == '0'; i++);
            swap(s[i], s[0]);
            s = s[0] + ('0' + s.substr(1));
        }

        cout << "Case #" << tt << ": " << s << endl;
    }


    return 0;
}
