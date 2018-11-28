#include <iostream>
#include <cstring>
#include <string>

using namespace std;

string map = "yhesocvxduiglbkrztnwjpfmaq";
int T;
string str;

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small.out", "w", stdout);
    
    scanf("%d\n", &T);
    char s[10000];
    
    for (int i = 1; i <= T; ++i)
    {
        gets(s);
        str = s;
        for (int j = 0; j < str.length(); ++j)
        {
            if (s[j] != ' ')
                str[j] = map[s[j] - 'a'];
        }
        cout << "Case #" << i << ": " << str << endl;
    }
}
