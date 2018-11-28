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

int k;
int arr[sz][sz];
bool hor[sz];
bool vert[sz];

int main ()
{
    int nTest; gi(nTest);
    forn(test, nTest)
    {
        init(arr, -1);
        gi(k); 
        forn(i,2*k-1)
            forn(j,k - abs(k - (i+1)))
                gi(arr[i][abs(k - (i+1)) + 2*j]);
/*        forn(i,2*k)
        {
            forn(j, 2*k)
                if (arr[i][j] != -1) cout << arr[i][j]; else cout << ' ';
            cout << endl; 
        }*/
        forn(i,2*k-1) hor[i] = vert[i] = true;
        forn(i,2*k-1)
            forn(j, i)
                if (i + (i-j) < 2*k-1)
                    forn(l, 2*k-1)
                        if (arr[j][l] != arr[2*i-j][l] && arr[j][l] != -1 && arr[2*i-j][l] != -1)
                            hor[i] = false;
        forn(i,2*k-1)
            forn(j, i)
                if (i + (i-j) < 2*k-1)
                    forn(l, 2*k-1)
                        if (arr[l][j] != arr[l][2*i-j] && arr[l][j] != -1 && arr[l][2*i-j] != -1)
                            vert[i] = false;
        int mindiff = 2*k;
        forn(i,2*k-1) forn(j,2*k-1) if (hor[i] && vert[j])
            mindiff = min(mindiff, abs(k - (i+1)) + abs(k - (j+1)));
        mindiff += k; 
        int cost = mindiff*mindiff - k*k; 
        cout << "Case #" << test + 1 << ": " << cost << endl;
    }
    return 0;
}