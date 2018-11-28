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
#define sz 50

int main ()
{
    int nTest; gi(nTest);
    forn(test, nTest)
    {
		int n; gi(n);
		int cnt = 0;
		forn(i, n) {
			int t; gi(t);
			if (t != i+1) cnt++; 
		}
        cout << "Case #" << test+1 << ": " << cnt << ".000000" << endl;
    }
    return 0;
}