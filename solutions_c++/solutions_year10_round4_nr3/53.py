#include<iostream>
#include<vector>
#include<cstring>
#include<stdio.h>
#include<string>
#include<cassert>
#include<algorithm>
using namespace std;

#define forn(i,n) for (int i=0;i<(n);i++)
#define init(a,v) memset(a,v,sizeof(a))
#define gi(t) scanf("%d",&(t))
#define sz 110

int r; 
bool arr[sz][sz];
bool arr2[sz][sz]; 
int x1, x2, y1, y2; 


int main ()
{
    int nTest; gi(nTest);
    forn(test, nTest)
    {
        init(arr, 0);
        gi(r);
        forn(i,r)
        {
            gi(x1);gi(y1);gi(x2);gi(y2);
            if (x1 > x2) swap(x1, x2);
            if (y2 < y1) swap(y1, y2);
            for (int j = x1; j <= x2; j++)
                for (int k = y1; k <= y2; k++)
                    arr[j][k] = true;
        }
                                
        int ans = 0;
        bool val;
        do
            {
                val = false;
                // Compute this stage, increment ans
                ans++;
                init(arr2, 0); 
                forn(i,sz) forn(j,sz) if (i && j)
                {
                    int cnt = 0;
                    if (arr[i-1][j]) cnt++; 
                    if (arr[i][j-1]) cnt++;
                    if (arr[i][j]) cnt++;
                    if (cnt >= 2)
                    { arr2[i][j] = true; val = true; }
                }
                memcpy(arr, arr2, sizeof(arr));
                // Label val as true is something is alive
            } while (val);
       cout << "Case #" << test + 1 << ": " << ans << endl; 
    }
    return 0;
}