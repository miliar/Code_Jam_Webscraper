#include<iostream>
#include<cstring>
#include<vector>
#include<string>
#include<algorithm>
#include<functional>
#include<stdio.h>
using namespace std;

#define forn(i,n) for(int i=0;i<(n);i++)
#define init(a,v) memset(a,v,sizeof(a))
#define gi(t) scanf("%d",&(t))
#define sz 55

int n, k; 
int input[sz][sz];

void rotate()
{
    forn(i,n)
    {
        int j = n-1; int k = n-1;
        while (j >= 0)
        {
            while (j >= 0 && !input[i][j]) j--;
            if (j < 0) break;
            if (j != k)
            {
                input[i][k] = input[i][j];
                input[i][j] = 0; 
            }
            j--; k--; 
        }
    }
}

void find(bool &red, bool &blue)
{
    int cr = 0; int cb = 0;
    cr = 0; cb = 0;
    // Horizontal
    forn(i,n)
    {
        cr = 0; cb = 0; 
        forn(j,n)
        {
            if (input[i][j] == 1) cr++; else cr = 0;
            if (input[i][j] == 2) cb++; else cb = 0;
            if (cr == k) red = true; 
            if (cb == k) blue = true;
        }
    }
    // Vertical
    forn(j,n)
    {
        cr = 0; cb = 0;
        forn(i,n)
        {
            if (input[i][j] == 1) cr++; else cr = 0;
            if (input[i][j] == 2) cb++; else cb = 0;
            if (cr == k) red = true;
            if (cb == k) blue = true;
        }
    }
    // Diagonal down
    forn(diag,2*n-1)
    {
        int i = ((diag >= n)? diag-(n-1): 0);
        int j = ((diag >= n)? 0: diag);
        cr = 0; cb = 0;
        for(; i < n && j < n; i++, j++)
        {
            if (input[i][j] == 1) cr++; else cr = 0;
            if (input[i][j] == 2) cb++; else cb = 0;
            if (cr == k) red = true;
            if (cb == k) blue = true;
        }
    }
    // Diagonal up
    forn(diag,2*n-1)
    {
        int i = ((diag >= n)? diag-(n-1): 0);
        int j = ((diag >= n)? n-1: diag);
        cr = 0; cb = 0;
        for(; i < n && j >= 0; i++, j--)
        {
            if (input[i][j] == 1) cr++; else cr = 0;
            if (input[i][j] == 2) cb++; else cb = 0;
            if (cr == k) red = true;
            if (cb == k) blue = true;
        }
    }
}

char str[sz];

int main ()
{
    int test; gi(test);
    forn(numb,test)
    {
        bool red = false, blue = false;
        // take the input
        gi(n); gi(k); init(input, 0); 
        forn(i,n)
        {
            scanf("%s", str);
            forn(j,n)
            {
                if (str[j]=='R') input[i][j] = 1; 
                if (str[j]=='B') input[i][j] = 2;
            }
        }
        // process
        rotate();
        find(red, blue); 
        // output
//        printf("Case #%d: ", numb+1);
        cout << "Case #" << numb+1 << ": ";
        if (red && blue) cout << "Both" << endl; 
        if (!red && blue) cout << "Blue" << endl;
        if (red && !blue) cout << "Red" << endl;
        if (!red && !blue) cout << "Neither" << endl;
    }
    return 0;
}