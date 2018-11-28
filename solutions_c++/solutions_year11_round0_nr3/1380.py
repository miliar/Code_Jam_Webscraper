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
		int minn = 1000000, sum = 0, xorr = 0, ele;
		
		forn(i, n) {
			gi(ele);
			minn = min(ele, minn);
			sum += ele;
			xorr ^= ele;
		}

		if (xorr == 0) cout << "Case #" << test+1 << ": " << (sum-minn) << endl;
		else cout << "Case #" << test+1 << ": NO" << endl;
    }
    return 0;
}