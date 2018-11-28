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
using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int T;
    cin >> T;
    for (int t = 0; t < T; ++t)
    {
    	int c,d,v,p;
        cin >> c >> d; // num of lines, min dist

        int points[300000];

        for (int i=0;i<300000;i++)
        	points[i] = 0;


        for (int i=0;i<c;i++)
        {
        	cin >> p >> v;
        	points[p+150000] = v;
        }

        long long int* vpos = new long long int[2000000];
//        int vpos[2000000];
        int vnum = 0;
        for (int i=0;i<300000;i++)
        	for (int j=0;j<points[i];j++)
        		vpos[vnum++] = i-150000;

        long long int mind = 999999999999ll;
        long long int maxd = -999999999999ll;

        long long int peast = 0;

        long long int pwest = 0;
        for (int i=1;i<vnum;i++)
        {
        	pwest = pwest + d - (vpos[i] - vpos[i-1]);
        	if (pwest < 0)
        		pwest = 0;
        	if (pwest > maxd)
        		maxd = pwest;
//        	printf("i:%d  pwest: %d  d:%d   vpos[i]:%d   vpos[i-1]:%d\n",i,pwest,d,vpos[i],vpos[i-1]);
        }
        if (vnum == 1)
        	maxd = 0;

/*        for (int i=0;i<vnum;i++)
        {
        	long long int cd = i*d - vpos[i];
        	if (cd<mind) mind = cd;
        	if (cd>maxd) maxd = cd;
//        	printf("%d %d %lld %lld %lld\n",t,i,cd,mind,maxd);
        }*/

/*        for (int i=0;i<vnum;i++)
        	printf(" %d ",vpos[i]);

        printf("\n%lld %lld\n",mind,maxd);
*/
//        long long int dd = maxd - mind;
        double sol = (double)maxd / 2.0;

        printf("Case #%d: %.1f\n",t+1,sol);
//        cout << "Case #" << t+1 << ": " << sol << endl;

        delete vpos;
    }

    return 0;
}
