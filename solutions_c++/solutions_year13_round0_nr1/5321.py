#include <iostream>

using namespace std;

bool isX(char c)
{
    if (c == 'X' || c == 'T')
        return true;
    return false;
}

bool isO(char c)
{
    if (c == 'O' || c == 'T')
        return true;
    return false;
}

int main()
{
    int T;
    cin >> T;

    
    for (int caseno=0; caseno<T; ++caseno) {
        
        char a1,a2,a3,a4,b1,b2,b3,b4,c1,c2,c3,c4,d1,d2,d3,d4;
        cin >> a1 >> a2 >> a3 >> a4;
        cin >> b1 >> b2 >> b3 >> b4;
        cin >> c1 >> c2 >> c3 >> c4;
        cin >> d1 >> d2 >> d3 >> d4;

        if ((isX(a1) && isX(a2) && isX(a3) && isX(a4)) ||
            (isX(b1) && isX(b2) && isX(b3) && isX(b4)) ||
            (isX(c1) && isX(c2) && isX(c3) && isX(c4)) ||
            (isX(d1) && isX(d2) && isX(d3) && isX(d4)) ||
            (isX(a1) && isX(b1) && isX(c1) && isX(d1)) ||
            (isX(a2) && isX(b2) && isX(c2) && isX(d2)) ||
            (isX(a3) && isX(b3) && isX(c3) && isX(d3)) ||
            (isX(a4) && isX(b4) && isX(c4) && isX(d4)) ||
            (isX(a1) && isX(b2) && isX(c3) && isX(d4)) ||
            (isX(a4) && isX(b3) && isX(c2) && isX(d1))) {
            cout << "Case #" << caseno+1 << ": X won" << endl;
        }
        else if ((isO(a1) && isO(a2) && isO(a3) && isO(a4)) ||
                 (isO(b1) && isO(b2) && isO(b3) && isO(b4)) ||
                 (isO(c1) && isO(c2) && isO(c3) && isO(c4)) ||
                 (isO(d1) && isO(d2) && isO(d3) && isO(d4)) ||
                 (isO(a1) && isO(b1) && isO(c1) && isO(d1)) ||
                 (isO(a2) && isO(b2) && isO(c2) && isO(d2)) ||
                 (isO(a3) && isO(b3) && isO(c3) && isO(d3)) ||
                 (isO(a4) && isO(b4) && isO(c4) && isO(d4)) ||
                 (isO(a1) && isO(b2) && isO(c3) && isO(d4)) ||
                 (isO(a4) && isO(b3) && isO(c2) && isO(d1))) {
            cout << "Case #" << caseno+1 << ": O won" << endl;
        } else if ((a1 == '.') || (a2 == '.') || (a3 == '.') || (a4 == '.') || (b1 == '.') || (b2 == '.') || (b3 == '.') || (b4 == '.') || (c1 == '.') || (c2 == '.') || (c3 == '.') || (c4 == '.') || (d1 == '.') || (d2 == '.') || (d3 == '.') || (d4 == '.')) {
            cout << "Case #" << caseno+1 << ": Game has not completed" << endl;
        }
        else {
            cout << "Case #" << caseno+1 << ": Draw" << endl;
        }
    }

    return 0;
}
