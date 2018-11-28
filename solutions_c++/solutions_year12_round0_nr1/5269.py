#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>

using namespace std;

const char dic[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v',
                      'x', 'd', 'u', 'i', 'g', 'l', 'b',
                      'k', 'r', 'z',      't', 'n', 'w',
                      'j', 'p', 'f',      'm', 'a', 'q'};

int main()
{
    //freopen("input.in", "r", stdin);
    //freopen("output.out", "w", stdout);
    
    int t;
    char str[105];
    
    scanf("%d\n", &t);
    for(int i = 1; i <= t; i++) {
        gets(str);
        int len = strlen(str);
        printf("Case #%d: ", i);
        for(int j = 0; j < len; j++) {
            if(str[j] == ' ')
                printf(" ");
            else {
                char ch = dic[str[j] - 'a'];
                printf("%c", ch);
            }
        }
        cout << endl;
    }
    
    return 0;
}        
        
