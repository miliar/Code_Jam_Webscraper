#include <iostream>
#include <cstdio>
using namespace std;
const int maxn = 100;

char a[maxn][maxn], b[maxn][maxn];

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int t1,t2,r,c;
    cin>>t1;
    for (int t2 = 1; t2 <= t1; ++t2){
        cin>>r >>c;
        bool flag = true;
        for (int i = 1; i <= r; ++i)
            for (int j = 1; j <= c; ++j)
                b[i][j] = '0';
        for (int i = 1; i <= r; ++i)
            for (int j = 1; j <= c; ++j) {
                cin>>a[i][j];
                if (b[i][j] == '0'){
                    if (a[i][j] == '.') b[i][j] = '.';
                    else {
                        b[i][j] = b[i+1][j+1] = '/';
                        b[i+1][j] = b[i][j+1] = '\\';
                        if ((i == r) || (j == c)) flag = false;
                    }
                } else if (a[i][j] == '.') flag =false;
            }
        cout<<"Case #" <<t2 <<":" <<endl;
        if (flag)
            for (int i = 1; i <= r; ++i){
                for (int j = 1; j <= c; ++j)
                    cout<<b[i][j];
                cout<<endl;
            }
        else cout<<"Impossible" <<endl;
    }
}
