#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

const int maxn = 110;

char a[100][100];
int n, m;

bool check(int i,int j)
{
    if(i >= n || j >= m)
        return false;
    if(a[i][j] != '#')
        return false;

    return true;
}

bool Solve()
{
    for(int i = 0; i < n; i ++)
    {
        for(int j = 0; j < m;j++)
        {
            if(a[i][j] == '#')
            {
                a[i][j] = '/';
                if(!check(i + 1,j))
                    return false;
                else
                    a[i + 1][j] = '\\';

                if(!check(i,j + 1))
                    return false;
                else
                    a[i][j + 1] = '\\';

                if(!check(i + 1,j + 1))
                    return false;
                else
                    a[i + 1][j + 1] = '/';
            }
        }
    }
    return true;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    cin >> T;
    for(int t = 1; t <= T; t ++)
    {
        cin>> n >> m;
        for(int i = 0;i < n; i ++)
        {
            scanf("%s", a[i]);
        }
        cout << "Case #" << t <<":" << endl;
        if(!Solve())
        {
            cout<<"Impossible"<<endl;
        }
        else{
            for(int i = 0; i < n; i ++)
                printf("%s\n", a[i]);
        }
    }
    return 0;
}
