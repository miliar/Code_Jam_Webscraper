#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

#define pb push_back
#define mp make_pair
#define pii pair <int, int>


using namespace std;


const char anss[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
string s;
int main()
{
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    int c = 0;
    while (getline(cin, s))
    {
        c++;
        for (int i = 0; i < s.length(); i++)
        {
            if (s[i] != ' ') s[i] = anss[s[i] - 'a'];
        }
        cout << "Case #" << c << ": " << s << endl;
    }
    return 0;
}
