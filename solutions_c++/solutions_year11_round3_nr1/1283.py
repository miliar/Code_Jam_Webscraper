#include <iostream>
#include <string>
using namespace std;

int t,r,c;
int possible;
string a[50];
int main()
{
    string tmp;
    int i,it,j;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> t;
    for (it = 1;it <= t;++it)
    {
        possible = 1;
        cin >> r >> c;
        for (i = 0;i < r;++i) cin >> a[i];
        for (i = 0;i < r;++i)
            for (j = 0;j < c;++j)
                if (a[i][j] == '#')
                {
                    a[i][j] = '/';
                    if (a[i + 1][j] == '#') a[i + 1][j] = '\\'; else possible = 0;
                    if (a[i][j + 1] == '#') a[i][j + 1] = '\\'; else possible = 0;
                    if (a[i + 1][j + 1] == '#') a[i + 1][j + 1] = '/'; else possible = 0;
                    if (possible == 0)
                    {
                        i = r;
                        j = c;
                    }
                }
        cout << "Case #" << it << ':' << endl;
        if (possible) for (i = 0;i < r;++i) cout << a[i] << endl;
        else cout << "Impossible" << endl;
    }
    //system("pause");
    fclose(stdin);
    fclose(stdout);
    return 0;
}
