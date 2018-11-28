#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>

using namespace std;

int pos[128],col[128],n,T;
char buf[256];

int max(int a,int b) {return a>b?a:b;}
int abs(int x) {return x>0?x:-x;}

int main()
{
    int nowCase = 0;
    scanf("%d",&T);
    while (T--)
    {
        scanf("%d",&n);
        for (int i = 0;i < n;++i)
        {
            scanf("%s%d",buf,&pos[i]);
            col[i] = buf[0] == 'O';
        }
        int t[2] = {0,0},p[2] = {1,1};
        for (int i = 0;i < n;++i)
        {
            int next = -1;
            for (int j = i+1;j < n;++j)
                if (col[j] != col[i])
                {
                    next = j;
                    break;
                }
            t[col[i]] += abs(p[col[i]] - pos[i]) + 1;
            p[col[i]] = pos[i];
            if (-1 != next)
            {
                t[col[next]] += abs(p[col[next]] - pos[next]);
                p[col[next]] = pos[next];
            }
            if (t[col[next]] < t[col[i]]) t[col[next]] = t[col[i]];
        }
        cout << "Case #" << ++nowCase << ": ";
        cout << max(t[0],t[1]) << endl;
    }
    return 0;
}
