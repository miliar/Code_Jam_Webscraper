#include <algorithm>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <fstream>
using namespace std;
string m[4];
string judge( )
{
    for(int i = 0; i < 4; ++i)
    {
        if(m[i][0] == 'X' and m[i][1] == 'X' and m[i][2] == 'X' and m[i][3] == 'X')
            return "X won";
        if(m[i][0] == 'O' and m[i][1] == 'O' and m[i][2] == 'O' and m[i][3] == 'O')
            return "O won";
        if(m[0][i] == 'X' and m[1][i] == 'X' and m[2][i] == 'X' and m[3][i] == 'X')
            return "X won";
        if(m[0][i] == 'O' and m[1][i] == 'O' and m[2][i] == 'O' and m[3][i] == 'O')
            return "O won";
    }
    if(m[0][0] == 'X' and m[1][1] == 'X' and m[2][2] == 'X' and m[3][3] == 'X')
        return "X won";
    if(m[0][0] == 'O' and m[1][1] == 'O' and m[2][2] == 'O' and m[3][3] == 'O')
        return "O won";

    if(m[0][3] == 'X' and m[1][2] == 'X' and m[2][1] == 'X' and m[3][0] == 'X')
        return "X won";
    if(m[0][3] == 'O' and m[1][2] == 'O' and m[2][1] == 'O' and m[3][0] == 'O')
        return "O won";
    for(int i = 0; i < 4; ++i)
        for(int j = 0; j < 4; ++j)
            if(m[i][j] == '.')
                return "Game has not completed";
    return "Draw";
}
int main()
{
    fstream fin;
    ofstream fout;
    fin.open("test.in");
    fout.open("res.out");
int t;fin>>t;
for(int times = 0; times < t; ++times)
{
//FW

    string res;
    fin >> m[0] >> m[1]>>m[2]>>m[3];
    int tx = -1, ty = -1;
    for(int i = 0; i < 4; ++i)
        for(int j = 0; j < 4; ++j)
            if(m[i][j] == 'T')
            {
                tx = i;
                ty = j;
            }
    if(tx != -1)
    {
    m[tx][ty] = 'X';
    string res1 = judge();

    m[tx][ty] = 'O';
    string res2 = judge();
//cout << res1<<" "<<res2<< res1.compare(res2)<<endl;
    if(res1.compare(res2) == 0)
        res = res1;
    else if(res1.compare(string("X won")) == 0)
        res = "X won";
    else res = "O won";
    }
    else
        res = judge();

    fout <<"Case #"<<times+1<<": ";
    fout << res<<endl;

//FW
}
fout.close();
}
