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
	
	int i,j,k,t,s,p,n,m;
	int a[120];
	
	cin >> t;
	
    for (m=1;m<=t;++m)
	{
        printf("Case #%d: ",m);
        int total=0;
        cin >> n >> s >> p;
        for (i=1;i<=n;++i) cin >> a[i];
        for (i=1;i<=n;++i)
        {
            j=a[i]/3;
            k=a[i]%3;
            if (j>=p) 
            {
                ++total;
                continue;
            }
            if (a[i]==0) continue;
            if ((j>=p-1)&&(k==0)&&(s>0))
            {
                ++total;
                --s;
                continue;
            }
            if ((j>=p-1)&&(k!=0))
            {
                ++total;
                continue;
            }
            if ((j>=p-2)&&(k==2)&&(s>0))
            {
                ++total;
                --s;
                continue;
            }
        }
        cout << total << '\n';
    }
}
