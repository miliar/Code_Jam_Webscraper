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


int main()
{
//    freopen("A-sample.in", "r", stdin);            freopen("A-sample.out", "w", stdout);
//    freopen("A-small-attempt0.in", "r", stdin);    freopen("A-small-attempt0.out", "w", stdout);
//    freopen("A-small-attempt1.in", "r", stdin);    freopen("A-small-attempt1.out", "w", stdout);
//    freopen("A-small-attempt2.in", "r", stdin);    freopen("A-small-attempt2.out", "w", stdout);
    freopen("A-large.in", "r", stdin);             freopen("A-large.out", "w", stdout);

    int casenum;
    cin >> casenum;

    for (int casei = 0; casei < casenum; ++casei)
    {
    	int x,s,r,t,n;
        cin >> x >> s >> r >> t >> n;

        vector< pair<int,int> > ww;
        int noway = x;
        for (int i=0;i<n;i++)
        {
        	int b,e,w;
        	cin >> b >> e >> w;
        	ww.push_back(make_pair(w,e-b));
        	noway -= (e-b);
        }
        ww.push_back(make_pair(0,noway));
        sort (ww.begin(), ww.end());

        double canrun = t;
        double need = 0.0;
        for (int wn = 0; wn<n+1;wn++)
        {
        	double len = ww[wn].second;
        	double speed = ww[wn].first;

        	double walktime = len / (speed+s);
        	double runtime = len / (speed+r);

        	double runnow = 0.0;

        	if (canrun>runtime)
        	{
        		runnow = runtime;
        		canrun -= runnow;
        	}
        	else
        	{
        		runnow = canrun;
        		canrun = 0.0;
        	}

        	double d1 = runnow * (speed+r);
        	double t1 = runnow;
        	double d2 = (double)len - d1;

        	double t2 =  d2 / (speed+s);

//        	cerr << " len: " << len <<" speed: " << speed << " canrun: " << canrun << " runnow: "  << runnow << " t1: "  << t1 << " d1: "  << d1 << " t2: "  << t2 << " d2: "  << d2 << " "  << endl;

        	need += t1+t2;
        }
//        cerr << endl;

        printf("Case #%d: %5.6f\n",casei+1,need);

  //      cout.precision(12);

//        cout << "Case #" << casei+1 << ": " << need << endl;


    }

    cerr << "Done" << endl;

    return 0;
}
