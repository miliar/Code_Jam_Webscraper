#include <iostream>
#include <string>
#include <cstdio>

using namespace std;
string s[6];
int cnt;
void answ(bool tx, bool tc, int cu)
{
    if(!tx && !tc && cu == 0) cout << "Draw";
    if(!tx && !tc && cu != 0) cout << "Game has not completed";
    if(tx && !tc) cout << "X won";
    if(!tx && tc) cout << "O won";
}
void myfind()
{
    bool tx = false, tc = false;
    int cu = 0, mx = 0, mo = 0;
    for(int k = 0; k < 4; k++)
    {
        int x = 0, o = 0, nx = 0, no = 0;
        for(int p = 0; p < 4; p++)
        {
            if(s[k][p] == 'X' || s[k][p] == 'T') x++;
            if(s[k][p] == 'O' || s[k][p] == 'T') o++;
            //---------------------------------------
            if(s[p][k] == 'X' || s[p][k] == 'T') nx++;
            if(s[p][k] == 'O' || s[p][k] == 'T') no++;
            //---------------------------------------
            if(p + k == 3 && (s[k][p] == 'X' || s[k][p] == 'T')) mx++;
            if(p + k == 3 && (s[k][p] == 'O' || s[k][p] == 'T')) mo++;
            //------------------------------------------------------
            if(s[k][p] == '.') cu++;

        }
        if(x == 4) tx = true;
        if(o == 4) tc = true;
        //-----------------------------
        if(nx == 4) tx = true;
        if(no == 4) tc = true;
        //-----------------------------
        if(mx == 4) tx = true;
        if(mo == 4) tc = true;
        //-----------------------------
        if(tx || tc) break;
    }
    if(!tx && !tc)
    {
        int x = 0, o = 0;
         for(int i = 0; i < 4; i++)
        {
            if(s[i][i] == 'X' || s[i][i] == 'T') x++;
            if(s[i][i] == 'O' || s[i][i] == 'T') o++;
        }
        if(x == 4) tx = true;
        if(o == 4) tc = true;
    }
    answ(tx, tc, cu);
}
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> cnt;
    for(int i = 0; i < cnt; i++)
    {
        for(int j = 0; j < 4; j++) cin >> s[j];
        cout << "Case #" << i + 1 <<": ";
        myfind();
        cout << endl;
    }
    return 0;
}

