#include <iostream>
#include <cstdio>
#include <cstring>
#include <string.h>

using namespace std;

char lang[26] = { 'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q' };
FILE* out = fopen("output.txt", "w");

void solve(int x)
{
    char buf[102];
    gets(buf);

    fprintf(out, "Case #%d: ", x);

    for(int i = 0; i < strlen(buf); ++i)
    {
        if(buf[i] == ' ')
            fprintf(out, "%c", buf[i]);
        else
            fprintf(out, "%c", lang[ buf[i]-'a' ]);
    }
    fprintf(out, "\n");
}

int main()
{
    int t;

    cin >> t;
    char buf[100];
    gets(buf);

    for(int i = 1; i <= t; ++i)
        solve(i);

    return 0;
}
