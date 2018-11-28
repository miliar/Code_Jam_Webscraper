#import <Foundation/Foundation.h>

#import <stdlib.h>
#import <string.h>
#import <ctype.h>
#import <math.h>
/* C++
#import <vector>
#import <algorithm>
#import <queue>
#import <list>
#import <map>
#import <stack>
#import <set>
 
using namespace std;
*/

#import <iostream>
#include <vector>
#include <string>
#include <map>
#include <list>

#include <limits> // for numeric_limits

#include <set>
#include <utility> // for pair
#include <algorithm>
#include <iterator>

using namespace std;


#define CLEAR(x) memset(x,0,sizeof x);
#define FILL(x,v) memset(x,v,sizeof x);
#define abs(x) ((x)>=0?(x):(-(x)))
#define sqr(a) ((a)*(a))
#define LL unsigned long long int

char m[4][4];
BOOL incomplete;

typedef enum {
    WinnerX,
    WinnerO,
    WinnerDraw
} Winner;

Winner checkDiagonal1() {
    
    char c = m[0][0];
    if (c == '.') {
        incomplete = YES;
        return WinnerDraw;
    }
    if (c == 'T' )
        c = m[1][1];
    // a questo punto in c può esserci solo X od O
    for (int i=1;i<4;i++) {
        if (m[i][i] == '.' ) {
            incomplete = YES;
            return WinnerDraw;
        }
        if (m[i][i] != c && m[i][i] != 'T') {
            return WinnerDraw;
        }
    }
    return (c == 'X')?WinnerX:WinnerO;
}

Winner checkDiagonal2() {
    
    char c = m[0][3];
    if (c == '.') {
        incomplete = YES;
        return WinnerDraw;
    }
    if (c == 'T' )
        c = m[1][2];
    // a questo punto in c può esserci solo X od O
    for (int i=1;i<4;i++) {
        if (m[i][3-i] == '.' ) {
            incomplete = YES;
            return WinnerDraw;
        }
        if (m[i][3-i] != c && m[i][3-i] != 'T' ) {
            return WinnerDraw;
        }
    }
    return (c == 'X')?WinnerX:WinnerO;
}

Winner checkRow(int row) {
    char c = m[row][0];
    if (c == '.') {
        incomplete = YES;
        return WinnerDraw;
    }
    if ( c == 'T' )
        c = m[row][1];
    // a questo punto in c può esserci solo X od O
    for (int i=1;i<4;i++) {
        if (m[row][i] == '.' ) {
            incomplete = YES;
            return WinnerDraw;
        }
        if (m[row][i] != c && m[row][i] != 'T' ) {
            return WinnerDraw;
        }
    }
    return (c == 'X')?WinnerX:WinnerO;
}

Winner checkColumn(int col) {
    char c = m[0][col];
    if (c == '.') {
        incomplete = YES;
        return WinnerDraw;
    }
    if ( c == 'T' )
        c = m[1][col];
    // a questo punto in c può esserci solo X od O
    for (int i=1;i<4;i++) {
        if (m[i][col] == '.' ) {
            incomplete = YES;
            return WinnerDraw;
        }
        if (m[i][col] != c && m[i][col] != 'T' ) {
            return WinnerDraw;
        }
    }
    return (c == 'X')?WinnerX:WinnerO;
}

Winner checkDiagonals() {
    
    Winner winner = checkDiagonal1();
    if ((winner==WinnerO) || (winner==WinnerX))
        return winner;
    
    return checkDiagonal2();
}

Winner checkRows() {
    Winner winner;
    for (int i=0;i<4;i++) {
        winner = checkRow(i);
        if ((winner==WinnerO) || (winner==WinnerX))
            return winner;
    }
    return winner;
}

Winner checkColumns() {
    Winner winner;
    for (int i=0;i<4;i++) {
        winner = checkColumn(i);
        if ((winner==WinnerO) || (winner==WinnerX))
            return winner;
    }
    return winner;
}


Winner checkWinner() {
    // check diagonals
    Winner winner = checkDiagonals();
    if ((winner==WinnerO) || (winner==WinnerX))
        return winner;
    // check rows
    winner = checkColumns();
    if ((winner==WinnerO) || (winner==WinnerX))
        return winner;
    // check columns
    return checkRows();
}

int main(int argc, const char * argv[])
{
    @autoreleasepool {
        FILE *fi, *fo;
        int i, j;
        int t;
        
        
        fi=fopen("input.txt", "r");
        fo=fopen("output.txt", "w");
        
        fscanf(fi, "%d", &t);
        
        for ( i=0 ; i<t ; i++ ) { // for each row
            // read input
            for (j=0;j<4;j++) {
                fscanf(fi, "%s", m[j]);
            }
            
            // SOLVE
            incomplete = NO;
            Winner winner = checkWinner();
            
            NSString *s;
            if ( winner == WinnerO )
                s = @"O won";
            else if ( winner == WinnerX )
                s = @"X won";
            else if ( winner == WinnerDraw && !incomplete )
                s = @"Draw";
            else
                s = @"Game has not completed";
                
            // write output
            fprintf(fo, "Case #%d: %s\n", i+1, [s cStringUsingEncoding:NSASCIIStringEncoding]);
        }
        fclose(fo);
        fclose(fi);
    }
    return 0;
}

