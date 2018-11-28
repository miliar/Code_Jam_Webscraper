#include<iostream>
#include<map>
#include<math.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
typedef long long ll;
typedef vector<int>::iterator iv;
typedef map<string,int>::iterator im;

string s[50];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int c=1, t, n, m, i, j;
    bool ck;
    cin >> t;
    while(t--)
    {
        ck = 0;
        cin >> n >> m;
        for(i=0; i<n; i++)
            cin >> s[i];
        for(i=0; i<n && !ck; i++)
        {
            for(j=0; j<m && !ck; j++)
            {
                if(s[i][j] == '#')
                {
                    s[i][j] = '/';
                    if(i + 1 >= n || j + 1 >= m || s[i+1][j] != '#' || s[i][j+1] != '#' || s[i+1][j+1] != '#')
                    {
                        ck = 1;
                        continue;
                    }
                    s[i+1][j] = '\\';
                    s[i][j+1] = '\\';
                    s[i+1][j+1] = '/';
                }
            }
        }
        printf("Case #%d:\n", c++);
        if(ck)
            puts("Impossible");
        else
            for(i=0; i<n; i++)
                cout << s[i] << endl;
    }
}
