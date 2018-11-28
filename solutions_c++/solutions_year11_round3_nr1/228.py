#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <stack>
#include <queue>
#include <list>
#include <cstdlib>


using namespace std;


string word[55];
int r, c;

bool solve(int x, int y)
{
    if(y == c)
        return solve(x + 1, 0);
    if(x == r)
        return true;
    if(word[x][y] != '#')
        return solve(x, y + 1);
    if(y + 1 >= c || x + 1 >= r)
        return false;
    if(word[x][y] != '#' || word[x][y + 1] != '#' || word[x + 1][y] != '#' || word[x + 1][y + 1] != '#')
        return false;
    word[x][y] = '/';
    word[x][y + 1] = '\\';
    word[x + 1][y] = '\\';
    word[x + 1][y + 1] = '/';
    return solve(x, y + 2);
}


int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;
    for(int ti = 0; ti < t; ++ti)
    {
        cin >> r >> c;
        for(int i = 0; i < r; ++i)
            cin >> word[i];
        printf("Case #%d:\n", ti + 1);

        if(!solve(0, 0))
            printf("Impossible\n");
        else
        {
            for(int i = 0; i < r; ++i)
                cout << word[i] << endl;
        }
    }

    return 0;
}
