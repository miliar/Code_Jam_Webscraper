#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

const char decode[] = {'y', 'h', 'e', 's' , 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l',
                        'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

string s;

int main()
{
    int t;
    cin >> t;
    cin.get();
    for(int ca = 1; ca <= t; ca ++) {
        getline(cin, s);
        printf("Case #%d: ", ca);
        for(int i = 0; i < s.size(); i ++)
            if(s[i] == ' ') printf(" ");
            else printf("%c", decode[ s[i] - 'a' ]);
        printf("\n");
    }

    return 0;
}
