#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (unsigned i=0; i<T; i++) {
        string nstr;
        cin >> nstr;
        string s1;
        s1.append(1, '0');
        s1.append(nstr);
        char *numstr = strdup(s1.c_str());
        next_permutation(numstr, numstr+s1.size());
        printf("Case #%d: ", i+1);
        bool leading_zero = true;
        for (int j=0; j<strlen(numstr); j++) {
            if (numstr[j] == '0') {
                if (leading_zero) continue;
            }
            else {
                leading_zero = false;
            }
            printf("%c", numstr[j]);
        }
        printf("\n");
    }
}
