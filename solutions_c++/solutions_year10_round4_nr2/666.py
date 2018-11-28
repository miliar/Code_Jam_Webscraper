#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int scores[10][1025], miss[1025];
int power2[20];
long long rec[11][1025][11];
int p;
const long long MAXINT = 1050000000;

long long search(int lev, int order, int maxBelow) {
    if (rec[lev][order][maxBelow] != MAXINT) return rec[lev][order][maxBelow];
    if (lev == p-1) {
        int l, r, theMax;
        l = p - miss[order * 2];
        r = p - miss[order * 2 + 1];
        if (l < r) theMax = r;
        else theMax = l;
//        cout << "l = " << l << " r = " << r << " theMax = " << theMax << "maxBelow = " << maxBelow << endl;
        
        if (theMax <= maxBelow) {
            rec[lev][order][maxBelow] = 0;
            return rec[lev][order][maxBelow];
        }
        else if (theMax-1 == maxBelow) {
            rec[lev][order][maxBelow] = scores[lev][order];
            return rec[lev][order][maxBelow];
        }
        else {
            return MAXINT;
        }
    }
    long long sa, sb, a, b;
    sa = search(lev+1, order*2, maxBelow);
    sb = search(lev+1, order*2+1, maxBelow);
    a = sa+sb;
    sa = search(lev+1, order*2, maxBelow+1);
    sb = search(lev+1, order*2+1, maxBelow+1);
    b = sa + sb + scores[lev][order];
    rec[lev][order][maxBelow] = min(a, b);

/*    if (lev == maxBelow)
    cout << "lev = " << lev <<" order=" << order <<" maxBelow=" << maxBelow
        << " a=" << a << " b=" << b << endl;
*/
    return rec[lev][order][maxBelow];
}

int main(void)
{
    power2[0] = 1;
    for (int i=1; i<=11; ++i)
        power2[i] = power2[i-1] * 2;
    int testn;
    cin >> testn;
    for (int testi=0; testi<testn; ++testi) {
        for (int i=0; i<11; ++i)
            for (int j=0; j<1024; ++j)
                for (int k=0; k<11; ++k)
                    rec[i][j][k] = MAXINT;
        cin >> p;
        //cout << "p = " << p << endl;
            
        for (int i=0; i<power2[p]; ++i) {
            cin >> miss[i];
//            cout << miss[i] << " ";
        }
//        cout << endl;

        for (int i=p-1; i>=0; --i) {
            for (int j=0; j<power2[i]; ++j) {
                cin >> scores[i][j];
//                cout << scores[i][j] << " ";
            }
//            cout << endl;
        }
        
        cout << "Case #" << testi+1 << ": " << search(0,0,0) << endl;
/*
        for (int i=0; i<p; ++i) {
            for (int j=0; j<power2[i]; ++j)
                cout << rec[i][j][0] << " ";
            cout << endl;
        }
*/

    }
    return 0;
}
