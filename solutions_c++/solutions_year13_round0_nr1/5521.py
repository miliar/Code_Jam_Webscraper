
#include<stdio.h>

#include <string>
#include <iostream>
using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)

char tp[20];
int x[110000];
string  statuses[4] = {"X won", "O won", "Draw", "Game has not completed"};

#define toIndex(row,column) ((row)*4+(column) )

//return Value : -1 - Fail.. 0 - Success.. 1 - OnGoing..
int winValue = 0;
int XWin = 0, TotalXWin = 0;
int OWin = 0, TotalOWin = 0;

char    base = '.';

int    checkWin( int startRow, int startCol, int delRow, int delCol , bool foundDraw)
{
    char    target = tp[toIndex(startRow, startCol)];
    if( (startRow+delRow) >= 4 || (startCol+delCol) >= 4)
    {
        if (foundDraw)
            return 1;
        else if (base == 'F')
            return -1;
        else
            return 0;
    }
    
    //int check = toIndex(startRow+delRow, startCol+delCol);
    
    char    nextTarget = tp[toIndex(startRow+delRow, startCol+delCol)];
    
    if(  target == '.' || nextTarget == '.')
        return 1;
    else if( (target == 'T') || (nextTarget == 'T') || (target == nextTarget) )
    {
        
        if (base == target)
        {
            if (base == 'T')    base = nextTarget;
            
            if (base == 'O')                    OWin++;
            else if(base == 'X')                XWin++;
        }
    }
    else
    {
        base = 'F'; // now.. this line doesn't count except not completed!!..
    }
    //    winValue++;
    
    return checkWin(startRow+delRow, startCol+delCol, delRow, delCol, foundDraw);
    
    /* else //superpass..
        return -1;
    */
}


void solve() {
	int n=4;
    int mid = 0;
    int ret = 0;
    int onGoing = 0;
	//scanf("%d", &n);
	forn(i, n)
        scanf("%s", tp+(4*i));
    
    // Done in building 4x4 board.. now analyze it!!
    
    forn(x, 4)
    {
        base = tp[toIndex(x, 0)];
        mid = checkWin(x,0,0,1,false);    // Row #1, #2..
        if (mid == 0)
        {
            TotalOWin += OWin;
            TotalXWin += XWin;
        } else if (mid == 1)    // OnGoing..
        {
            onGoing++;
        }
        OWin =0, XWin =0;
        
        base = tp[toIndex(0, x)];
        mid = checkWin(0,x,1,0,false);    // Column #1, #2..
        if (mid == 0)
        {
            TotalOWin += OWin;
            TotalXWin += XWin;
        } else if (mid == 1)    // OnGoing..
        {
            onGoing++;
        }
        OWin =0, XWin =0;
    }
    base = tp[toIndex(0, 0)];
    mid = checkWin(0,0,1,1,false);
    if (mid == 0)
    {
        TotalOWin += OWin;
        TotalXWin += XWin;
    } else if (mid == 1)    // OnGoing..
    {
        onGoing++;
    }
    OWin =0, XWin =0;
    
    base = tp[toIndex(0, 3)];
    mid = checkWin(0,3,1,-1,false);
    if (mid == 0)
    {
        TotalOWin += OWin;
        TotalXWin += XWin;
    } else if (mid == 1)    // OnGoing..
    {
        onGoing++;
    }
    OWin =0, XWin =0;
    
    if ( (onGoing != 0) || (TotalOWin != 0 && TotalXWin != 0) )    ret = 3;          // Not Completed..
    
    if ( (onGoing == 0) && TotalOWin == 0 && TotalXWin == 0)    ret = 2;     // Draw
    
    if ( TotalOWin > TotalXWin)               ret = 1;    // O Win
    if ( TotalOWin < TotalXWin)               ret = 0;    // X Win..
    
    cout << statuses[ret] << endl;
}

int main() {

    #ifdef ALEX_PRIVATE_TEST
    freopen("/Users/admin/Documents/input.txt", "rt", stdin);
    freopen("/Users/admin/Documents/output.txt", "wt", stdout);
    #endif
	
	int tt;
	scanf("%d", &tt);
	forn(ii, tt) {
        OWin = 0, XWin = 0;
        TotalOWin = 0, TotalXWin = 0;
		printf("Case #%d: ", ii + 1);
		solve();
	}
	
	return 0;
}

