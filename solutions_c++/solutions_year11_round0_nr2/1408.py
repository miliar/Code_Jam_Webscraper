//
//  main.cpp
//  Magicka
//
//  Created by Trung Dinh on 5/7/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include<fstream>
#define INPUTFILE "B-large.in"
#define OUTPUTFILE "text.out"
using namespace std;

int main (int argc, const char * argv[])
{
    int nTest;
    ifstream fi(INPUTFILE);
    ofstream fo(OUTPUTFILE);
    int f[300][300], ff[300][300];
    int c, d, n;
    fi >> nTest;
    for (int test = 0; test < nTest; test ++) {
        //initialzie
        string ans("\0");
        for (int i = 0; i < 300; i ++)
            for (int j = 0; j < 300; j ++) {
                ff[i][j] = f[i][j] = 0;
            }
        //
        fi >> c;
        for (int i  = 0; i < c; i ++) {
            char x, y, z;
            fi >> x >> y >> z;
            //cout << x << y << z << " " << (int)z << endl;
            ff[(int)x][(int) y] = (int)z;
            ff[(int)y][(int) x] = (int)z;
        }
        fi >> d;
        for (int i = 0; i < d; i ++) {
            char x, y;
            fi >> x >> y;
            //cout << x << y << endl;
            f[(int)x][(int)y] = -1;
            f[(int)y][(int)x] = -1;
        }        
        fi >> n;
        bool ok;
        for (int i = 0; i < n; i ++) {
            char x;
            fi >> x;
            //cout << i << "$"<<x<<"$";
            ok = true;
            if (i > 0) {
                if (ff[(int)x][(int)ans[ans.length() - 1]] != 0) {
                    ans[ans.length() - 1] = (char)ff[(int)x][(int)ans[ans.length() - 1]];
                    cout <<(char)ff[(int)x][(int)ans[ans.length() - 1]] << endl;
                    ok = false;
                }
                if (ok)
                    for (int j = 0; j < ans.length(); j ++)
                        if (f[(int)x][(int)ans[j]] == -1) {
                            ans = "\0";
                            //cout << ans.length() << endl;
                            ok = false;
                            break;
                        }
            }
            if (ok) ans = ans + x;
        }
        fo << "Case #" << test  + 1 << ": [";
        if (ans.length() > 0) fo << ans[0];
        for (int i = 1; i < ans.length(); i ++) fo << ", " << ans[i];
        fo << "]" << endl;
        //cout << ans << endl;
    }
    return 0;
}

