//#define trivia
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <stack>
#include <queue>
#include <vector>
#include <list>
#include <map>
#include <string>
#include <bitset>
#define ken(i, a, b) for(int i = int(a); i < int(b); i++)
#define tehe(i, a, b) for(int i = int(a); i > int(b); i--)
using namespace std;

int r, c;
char inp[55][55];
bool possible;

void processA() {
    possible = true;
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (inp[i][j] == '#') {
                if ((inp[i+1][j] == '#') && (inp[i][j+1] == '#') && (inp[i+1][j+1] == '#')) {
                    inp[i][j] = '/';
                    inp[i+1][j] = '\\';
                    inp[i][j+1] = '\\';
                    inp[i+1][j+1] = '/';
                }
                else
                    possible = false;
            }
        }
    }
}

int main()
{
	#ifndef trivia
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	#endif

    int tc;
    cin >> tc;
    for (int i = 0; i < tc; i++) {
        cin >> r >> c;
        scanf("\n");
        for (int j = 0; j < r; j++) {
            for (int k = 0; k < c; k++) {
                scanf("%c", &inp[j][k]);
            }
            scanf("\n");
        }
        processA();
        cout << "Case #" << (i+1) << ":" << endl;
        if (!possible)
            cout << "Impossible" << endl;
        else {
            for (int k = 0; k < r; k++) {
                for (int l = 0; l < c; l++) {
                    cout << inp[k][l];
                }
                cout << endl;
            }
        }
    }

	#ifndef trivia
	fclose(stdout);
	system("output.txt");
	#endif
	return 0;
}
