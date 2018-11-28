#include <iostream>
#include <fstream>
#include <algorithm>
#include <climits>
#include <cstdlib>
#include <cmath>
#include <cstring>




using namespace std;


int hash[1000];
int N;
char str[1000];
//char Copy[3][1000] = {"our language is impossible to understand",
// "there are twenty six factorial possibilities",
//"so it is okay if you want to just give up"};

void init()
{
    hash['a'] = 'y';
    hash['b'] = 'h';
    hash['c'] = 'e';
    hash['d'] = 's';
    hash['e'] = 'o';
    hash['f'] = 'c';
    hash['g'] = 'v';
    hash['h'] = 'x';
    hash['i'] = 'd';
    hash['j'] = 'u';
    hash['k'] = 'i';
    hash['l'] = 'g';
    hash['m'] = 'l';
    hash['n'] = 'b';
    hash['o'] = 'k';
    hash['p'] = 'r';
    hash['q'] = 'z';
    hash['r'] = 't';
    hash['s'] = 'n';
    hash['t'] = 'w';
    hash['u'] = 'j';
    hash['v'] = 'p';
    hash['w'] = 'f';
    hash['x'] = 'm';
    hash['y'] = 'a';
    hash['z'] = 'q';
    hash[' '] = ' ';

}
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    init();
    scanf("%d\n", &N);
//    memset(hash, -1, sizeof(hash));
    for(int i = 0; i < N; i++)
    {
        printf("Case #%d: ", i + 1);
        gets(str);
        int len = strlen(str);
        for(int j = 0; j < len; j++)
        {
            putchar(hash[str[j]]);
        }
        puts("");
    }
















    return 0;
}
