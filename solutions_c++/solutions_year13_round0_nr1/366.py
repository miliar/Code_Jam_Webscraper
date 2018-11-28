#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

string a[4];

int get_result()
{
    bool more = false;
    int xd1 = 0, xd2 = 0, od1 = 0, od2 = 0;
    for(int i = 0; i < 4; i++)
    {
        int xh = 0, oh = 0, xv = 0, ov = 0;
        for(int j = 0; j < 4; j++)
        {
            xh += (a[i][j] == 'X' or a[i][j] == 'T');
            oh += (a[i][j] == 'O' or a[i][j] == 'T');
            xv += (a[j][i] == 'X' or a[j][i] == 'T');
            ov += (a[j][i] == 'O' or a[j][i] == 'T');
            more |= (a[i][j] == '.');
        }
        if(xh == 4 or xv == 4) return 0;
        if(oh == 4 or ov == 4) return 1;
        xd1 += (a[i][i] == 'X' or a[i][i] == 'T');
        od1 += (a[i][i] == 'O' or a[i][i] == 'T');
        xd2 += (a[i][3 - i] == 'X' or a[i][3 - i] == 'T');
        od2 += (a[i][3 - i] == 'O' or a[i][3 - i] == 'T');
    }
    if(xd1 == 4 or xd2 == 4) return 0;
    if(od1 == 4 or od2 == 4) return 1;
    return more ? 3 : 2;
}

string solve()
{
    int res = get_result();
    if(res == 0) return "X won";
    if(res == 1) return "O won";
    if(res == 2) return "Draw";
    if(res == 3) return "Game has not completed";
}

int main()
{
    freopen("Alarge.in", "r", stdin);
    freopen("Alarge.out", "w", stdout);
    int T = 0;
    cin >> T;
    for(int i = 1; i <= T; i++)
    {
        cin >> a[0] >> a[1] >> a[2] >> a[3];
        cout << "Case #" << i << ": " << solve() << endl;
    }
}
