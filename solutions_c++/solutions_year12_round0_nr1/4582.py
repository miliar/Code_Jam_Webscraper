#include <iostream>
#include <vector>
#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <string.h>
#include <cstdio>
#include <string>
#include <utility>
#include <string>

using namespace std;

const bool input = 0;

int main()
{
     if(input)
    {
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    }
    string Googlerese("yhesocvxduiglbkrztnwjpfmaq");
    int n;
    char c;
    cin >> n ;
    scanf( "\n");
    for(int i = 0; i < n; i++)
    {
        cout << "Case #" << i + 1 << ": ";
        while(scanf("%c", &c) && c != '\n')
        {
            //cout << c;
            if(isalpha(c) && islower(c))
                cout << Googlerese[c - 97];
            else
                cout << c;
        }
        cout << "\n";
    }
    return 0;
}
