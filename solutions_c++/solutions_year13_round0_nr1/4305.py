#include <iostream>
#include <string>
#include <string.h>
#include <vector>
#include <stdio.h>
#include <stdlib.h>

using namespace std;


int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    cin.ignore(100500, '\n');
    for (int o_O=0;o_O<t;o_O++){
        cout << "Case #" << o_O+1 << ": ";
        string s;
        char a[4][4];
        vector <bool> f(4, false);
        for (int i=0;i<4;i++){
            getline(cin, s);
            for (int j=0;j<4;j++){
                if (s[j]=='.')
                    f[2]=true;
                a[i][j]=s[j];
            }
        }
        getline(cin,s);
        vector <int> o(8,0);
        vector <int> x(8,0);
        int t1=0;
        int t2=0;
        int t3=0;
        int t4=0;
        for (int i=0;i<4;i++){
            if ((a[i][i]=='X')||(a[i][i]=='T')) t1++;
            if ((a[i][i]=='O')||(a[i][i]=='T')) t2++;
            if ((a[i][3-i]=='X')||(a[i][3-i]=='T')) t3++;
            if ((a[i][3-i]=='O')||(a[i][3-i]=='T')) t4++;
            for (int j=0;j<4;j++){
                if ((a[i][j]=='X')||(a[i][j]=='T')){
                    x[i]++;
                    x[4+j]++;
                    if ((x[i]==4)||(x[j+4]==4))
                        f[0] = true;
                }
                if ((a[i][j]=='O')||(a[i][j]=='T')){
                    o[i]++;
                    o[j+4]++;
                    if ((o[i]==4)||(o[j+4]==4))
                        f[1] = true;
                }
            }
        }
        if ((t1==4)||(t3==4))
            f[0]=true;
        if ((t2==4)||(t4==4))
            f[1]=true;
        if (f[0])
            cout << "X won" << endl;
        else
        if (f[1])
            cout << "O won" << endl;
        else
        if (f[2])
            cout << "Game has not completed" << endl;
        else
            cout << "Draw" << endl;
    }
    return 0;
}
