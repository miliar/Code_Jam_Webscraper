// Website  :
// Contest  :
// Problem  :
// Language : C/C++

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <string.h>
#include <math.h>
#include <algorithm>

// Bangke Style (DARKSTALKER)
int temp, i, j, k, T;
    // DEFINE
#define KASE while(T--)
#define REP(I, J, K) for((I)=(J);(I)<(K);(I)++)
#define HOLD {fflush(stdin); getchar ();}
#define INPUT(A) freopen(A, "r", stdin);
#define OUTPUT(A) freopen(A, "w", stdout);
#define reset(A, I) memset(A, I, sizeof A);
#define ll long long
#define INF 1000000000
#define MIN -1000000000
#define MAX 1000000
    // GRAPH DIRECTION
int x8[] = {1,1,0,-1,-1,-1, 0, 1};
int y8[] = {0,1,1, 1, 0,-1,-1,-1};
int x4[] = {1,0,-1, 0};
int y4[] = {0,1, 0,-1};
using namespace std;
// Bangke Style (DARKSTALKER)

//MAIN CODE
int main()
{
    int kasus = 0, panjang, a[1000];
    a['a'] = 'y';
    a['b'] = 'h';
    a['c'] = 'e';
    a['d'] = 's';
    a['e'] = 'o';
    a['f'] = 'c';
    a['g'] = 'v';
    a['h'] = 'x';
    a['i'] = 'd';
    a['j'] = 'u';
    a['k'] = 'i';
    a['l'] = 'g';
    a['m'] = 'l';
    a['n'] = 'b';
    a['o'] = 'k';
    a['p'] = 'r';
    a['q'] = 'z';
    a['r'] = 't';
    a['s'] = 'n';
    a['t'] = 'w';
    a['u'] = 'j';
    a['v'] = 'p';
    a['w'] = 'f';
    a['x'] = 'm';
    a['y'] = 'a';
    a['z'] = 'q';
    char kalimat[10000];
    INPUT("A-small-attempt0.in");
    OUTPUT("out.txt");
    cin >> T;
    getchar();
    KASE {
        kasus++;
        gets(kalimat);
        panjang = strlen(kalimat);
        cout << "Case #" << kasus << ": ";
        REP(i, 0, panjang)
            if (kalimat[i] != ' ')
                printf ("%c",a[kalimat[i]]);
            else printf (" ");
        cout << endl;
    }
    return 0;
}
//END OF MAIN CODE
