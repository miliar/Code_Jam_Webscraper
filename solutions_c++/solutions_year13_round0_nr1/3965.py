#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <cmath>
#include <cstdio>
#include <cstring>
#include <vector>
#include <functional>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <cassert>
#include <map>
#include <deque>
#include <queue>
#include <set>
#include <stack>

using namespace std;

typedef vector<char> vi;
typedef vector<vi> vvi; 

typedef unsigned int uint;

#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define MAX_DISTANCE (300000)

void clearB(vvi &B) {
    for (int x = 0; x < 4; x++) {
        for (int y = 0; y < 4; y++) {
            B[x][y] = 0;
        }
    }
    
}

void printB(vvi &B) {
    for (int x = 0; x < 4; x++) {
        for (int y = 0; y < 4; y++) {
            cout << B[x][y];
        }
        
        cout << endl;
    }
    
}

int check(vvi &B, char c) {
    int row, col;
    
    for (int x = 0; x < 4; x++) {
        row = col = 0;
        for (int y = 0; y < 4; y++) {
            if (B[x][y] == c || B[x][y] == 'T')
                row++;
            if (B[y][x] == c || B[y][x] == 'T')
                col++;
        }
        
        if (row == 4 || col == 4)
            return 1;
    }
    
    row = col = 0;
    for (int x = 0; x < 4; x++) {
        if (B[x][x] == c || B[x][x] == 'T')
            row++;
        if (B[3-x][x] == c || B[3-x][x] == 'T')
            col++;
    }
    
    if (row == 4 || col == 4)
        return 1;
    
    return 0;
    
}

int hasDot(vvi &B) {
    for (int x = 0; x < 4; x++) {
        for (int y = 0; y < 4; y++) {
            if (B[x][y] == '.')
                return 1;
        }
    }
    
    return 0;
}

int main(void) {
	
	int x, y, z;
	int numCases;
	unsigned int i, j, k;
	
	string line;
	getline(cin, line);
	istringstream(line) >> numCases;
    
	for (int T = 1; T <= numCases; T++) {
		vvi B(4, vi(4));
        for (int x = 0; x < 4; x++) {
            getline(cin, line);
            istringstream stream(line);
            stream >> B[x][0] >> B[x][1] >> B[x][2] >> B[x][3];
        }
        getline(cin, line);
        //printB(B);
        //printf("0, 3 = %c\n", B[0][3]);
        //continue;
        
		printf("Case #%d: ", T);
        if (check(B, 'X'))
            puts("X won");
        else if (check(B, 'O'))
            puts("O won");
        else if (hasDot(B))
            puts("Game has not completed");
        else
            puts("Draw");
        
        
	}

	return 0;
}