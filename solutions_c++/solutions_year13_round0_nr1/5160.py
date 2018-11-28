#include <iostream>
#include <vector>

using namespace std;

void display(unsigned long map) {
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            int b = i * 4 + j;
            cout << ((map & (1 << b)) ? 'X' : '.');
        }
        cout << endl;
    }
}

int main()
{
    int coden, t;
    cin >> t;
    // define vars
    string map;
    unsigned long xmap, omap;
    unsigned long one = 1;
    vector<unsigned long> pattern;
    unsigned long p1 = 0;
    unsigned long p2 = 0;
    unsigned long full = (one << 16) - 1;
    int result;

    for (int i = 0; i < 4; i++) {
        p1 |= one << (i * 4 + i);
        p2 |= one << (i * 4 + 3 - i);
    }
    pattern.push_back(p1);
    pattern.push_back(p2);

    for (int i = 0; i < 4; i++) {
        p1 = 0;
        p2 = 0;
        for (int j = 0; j < 4; j++) {
            p1 |= one << (i * 4 + j);
            p2 |= one << (j * 4 + i);
        }
        pattern.push_back(p1);
        pattern.push_back(p2);
    }

    //display(full);
    //cout << pattern.size() << endl;
    //for (int i = 0; i < pattern.size(); i++) {
        //display(pattern[i]);
        //cout << endl;
    //}

    for (coden = 1; coden <= t; coden++) {
        xmap = 0;
        omap = 0;
        for (int i = 0; i < 4; i++) {
            cin >> map;
            //cout << "map="<< map << endl;
            for (int j = 0; j < 4; j++) {
                int b = i * 4 + j;
                switch (map[j]) {
                case 'X':
                    xmap |= one << b; // set bit
                    omap &= ~(one << b);  // clear bit
                    break;
                case 'O':
                    xmap &= ~(one << b);  // clear bit
                    omap |= one << b; // set bit
                    break;
                case 'T':
                    xmap |= one << b; // set bit
                    omap |= one << b; // set bit
                    break;
                case '.':
                    xmap &= ~(one << b);  // clear bit
                    omap &= ~(one << b);  // clear bit
                    break;
                }
            }
        }
        //display(xmap);
        //display(omap);
        //display(xmap | omap);
        //cout << endl;

        // output result
        cout << "Case #" << coden << ": ";

        int result = 0;
        for (int i = 0; i < pattern.size(); i++) {
            if (((xmap & pattern[i]) ^ pattern[i]) == (unsigned long) (0)) {
                result = 1;
                /*
                cout << endl << "result:----------------" << endl;
                display(xmap);
                cout << endl;
                display(pattern[i]);
                cout << endl;
                display(xmap & pattern[i]);
                cout << endl;
                display((xmap & pattern[i]) ^ pattern[i]);
                */
                break;
            }
            if (((omap & pattern[i]) ^ pattern[i]) == 0) {
                result = 2;
                /*
                cout << "result:" << endl;
                display(pattern[i]);
                */
                break;
            }
        }

        if (result == 1) {
            cout << "X won" << endl;
        } else if (result == 2) {
            cout << "O won" << endl;
        } else if ((xmap | omap) == full) {
            cout << "Draw" << endl;
        } else {
            //cout << "xmap | omap = " << (xmap | omap) << endl;
            //cout << "full = " << (full) << endl;
            cout << "Game has not completed" << endl;
        }
    }
    return 0;
}

