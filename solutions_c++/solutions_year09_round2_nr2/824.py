#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int main()
{
    int casenumber;
    int x;
    string str;
    string str2;
    cin >> casenumber;
    for(x = 0; x < casenumber; ++x)
    {
        cout << "Case #" << x + 1 << ": ";
        cin >> str;
        if(next_permutation(str.begin(), str.end()))
            cout << str << endl;
        else
        {
            
            int len = str.length();
            int i;
            for(i = 0; i < len; ++i)
            {
                if(str[i] != '0') break;
            }
            cout << str[i] << "0";
            for(int k = 0; k < i; ++k)
                cout << str[k];
            for(int k = i+1; k < len; ++k)
                cout << str[k];
            cout << endl;
            
        }
        
    }
    return 0;
}
