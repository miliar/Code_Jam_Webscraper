#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	int n;
	cin >> n;
    int n0 = n;
    while(n-->0)
    {
        bool x = false, o = false;
        string m;
        int a[4][4];
        for(int j = 0; j < 4; j++)
        {
            cin >> m;
            for(int i = 0; i < 4; i++)
                switch(m[i])
                {
                    case '.':
                        a[i][j] = 1;
                        break;
                    case 'X':
                        a[i][j] = 4;
                        break;
                    case 'O':
                        a[i][j] = 16;
                        break;
                    case 'T':
                        a[i][j] = 64;
                        break;
                }
        }
        int r = 0;
        for(int i = 0; i < 4; i++)
        {
            int s = 0, t = 0;
            for(int j = 0; j < 4; j++)
            {
                r += a[i][j];
                s += a[i][j];
                t += a[j][i];
            }
        //    cerr << r << endl << s << endl << t << endl;
            if(s == 16 || t == 16 || s == 76 || t == 76)
                x = true;
            if(s == 64 || t == 64 || s == 128 || t == 128)
                o = true;
        }
        int s = 0, t = 0;
        for(int i = 0; i < 4; i++)
        {
            s += a[i][i];
            t += a[i][4 - i - 1];
        }
        if(s == 16 || t == 16 || s == 76 || t == 76)
            x = true;
        if(s == 64 || t == 64 || s == 112 || t == 112)
            o = true;
        if(x)
            cout << "Case #" << n0 - n << ": X won" << endl;
        else if(o)
            cout << "Case #" << n0 - n << ": O won" << endl;
        else if(r == 8*4+7*16+64 || r == 8*4+8*16)
            cout << "Case #" << n0 - n << ": Draw" << endl;
        else
            cout << "Case #" << n0 - n << ": Game has not completed" << endl;
    }
	return 0;
}
