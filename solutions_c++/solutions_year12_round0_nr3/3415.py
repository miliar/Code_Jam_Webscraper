#include <cstdio>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <set>
#include <queue>
#include <string>
#include <map>
#include <sstream>
#include <vector>

using namespace std; 

main()
{
    freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	
	int i,j,k,t,x,y,m,n;
	
	cin >> t;
    for (m=1;m<=t;++m)
	{
        printf("Case #%d: ",m);
        cin >> x >> y;
        int total=0;
        k=1;
        for (j=10;x/j>0;j*=10) ++k;
        n=1;
        for (i=1;i<=k;++i) n*=10;
        for (i=x;i<=y;++i)
        {
            k=0;
            for (j=10;i/j>0;j*=10)
            {
                if (i%j==0) continue;
                if ((((i%j)*(n/j)+(i/j))<=y)&&(((i%j)*(n/j)+(i/j))>i))
                {
                    ++total;
//                    cout << i << ' ' << (i%j)*(n/j)+(i/j) << '\n';
                }
            }
        }
        cout << total << '\n';
    }
}
