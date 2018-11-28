#include <algorithm>
#include <iostream>
#include <string.h>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <list>
#include <iostream>
#include <iomanip>
#include "math.h"
using namespace std;

long long int sumw[600][600];
long long int sumwx[600][600];
long long int sumwy[600][600];

long long int w[600][600];

int main()
{
//	freopen("B-sample.in", "r", stdin);            freopen("B-sample.out", "w", stdout);
//    freopen("B-small-attempt0.in", "r", stdin);    freopen("B-small-attempt0.out", "w", stdout);
//    freopen("B-small-attempt1.in", "r", stdin);    freopen("B-small-attempt1.out", "w", stdout);
//    freopen("B-small-attempt2.in", "r", stdin);    freopen("B-small-attempt2.out", "w", stdout);
    freopen("B-large.in", "r", stdin);             freopen("B-large.out", "w", stdout);

    char buf[1000];

    gets(buf);
    int casenum = atoi(buf);

    cerr << casenum << endl;

    for (int casei = 0; casei < casenum; ++casei)
    {
    	int r,c,d;
        gets(buf);

        stringstream ss;
    	ss << buf;
    	ss >> r;
    	ss >> c;
    	ss >> d;

        cerr << r << " " << c << " " << d << endl;

        for (int i=0;i<r;i++)
        {
        	gets(buf);
        	for (int j=0;j<c;j++)
        		w[i][j] = d+(buf[j]-'0');
        }

        sumw[0][0] = w[0][0];
        sumwx[0][0] = 0;
        sumwy[0][0] = 0;

        for (int j=1;j<c;j++)
        {
        	sumw[0][j] = 0;
        	sumwx[0][j] = 0;
        	sumwy[0][j] = 0;

        }
        for (int i=1;i<r;i++)
        {
        	sumw[i][0] = 0;
        	sumwx[i][0] = 0;
        	sumwy[i][0] = 0;
        }

        for (int i=1;i<=r;i++)
        	for (int j=1;j<=c;j++)
        	{
        		sumw[i][j] = sumw[i-1][j] + sumw[i][j-1] - sumw[i-1][j-1] + w[i-1][j-1];
        		sumwx[i][j] = sumwx[i-1][j] + sumwx[i][j-1] - sumwx[i-1][j-1]  + w[i-1][j-1]*(j-1);
        		sumwy[i][j] = sumwy[i-1][j] + sumwy[i][j-1] - sumwy[i-1][j-1]  + w[i-1][j-1]*(i-1);
        	}

        int foundmax = 0;

        int maxsize = min(r,c);

        for (int size=3;size<=maxsize;size++)
        {
        	for (int rb=0;rb<=r-size;rb++)
        		for (int cb=0;cb<=c-size;cb++)
        		{
        			long long int sw = sumw[rb+size][cb+size] - sumw[rb+size][cb] - sumw[rb][cb+size] + sumw[rb][cb];
        			long long int swx = sumwx[rb+size][cb+size] - sumwx[rb+size][cb] - sumwx[rb][cb+size] + sumwx[rb][cb];
        			long long int swy = sumwy[rb+size][cb+size] - sumwy[rb+size][cb] - sumwy[rb][cb+size] + sumwy[rb][cb];
        			sw = sw - w[rb][cb] - w[rb+size-1][cb] - w[rb][cb+size-1] - w[rb+size-1][cb+size-1];
        			swx = swx - w[rb][cb]*cb - w[rb+size-1][cb]*cb - w[rb][cb+size-1]*(cb+size-1) - w[rb+size-1][cb+size-1]*(cb+size-1);
        			swy = swy - w[rb][cb]*rb - w[rb+size-1][cb]*(rb+size-1) - w[rb][cb+size-1]*(rb) - w[rb+size-1][cb+size-1]*(rb+size-1);

        			swx *= 2;
        			swy *= 2;

        			long long int yo = (rb*2)+(size-1);
        			long long int xo = (cb*2)+(size-1);

        			bool ok = true;
        			if (yo*sw != swy) ok = false;
        			if (xo*sw != swx) ok = false;
        			if (ok)
        				if (size>foundmax)
        					foundmax = size;
        		}
        }

       if (foundmax>0)
        	cout << "Case #" << casei+1 << ": " << foundmax << endl;
        else
        	cout << "Case #" << casei+1 << ": IMPOSSIBLE" << endl;
    }
    cerr << "Done";
    return 0;
}
