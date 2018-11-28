#include <iostream>
#include <string>
#include <algorithm>
#include <cstdio>

using namespace std;

const char supers[27] = "yhesocvxduiglbkrztnwjpfmaq";

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    string s;
    int n;
    scanf("%d\n", &n);
    for (int i = 0; i < n; i++)
    {
        getline(cin, s);
        for (int j = 0; j < s.length(); j++)
            if (s[j] >= 'a' && s[j] <= 'z')
                s[j] = supers[s[j] - 'a'];
       //cout << s << endl;
        cout << "Case #" << i + 1 << ": " << s << endl;
    }
    return 0;
}
