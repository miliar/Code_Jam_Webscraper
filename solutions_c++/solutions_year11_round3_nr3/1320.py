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
	
	int t,i,j,k,n,l,h,sum;
	
	cin >> t;
	for (int ll=1;ll<=t;++ll)
	{
        int a[10001]={0};
        bool su=false;
        printf("Case #%d: ",ll);
        cin >> n >> l >> h;
        for (i=1;i<=n;++i) cin >> a[i];
        for (i=l;i<=h;++i)
        {
            su=false;
            for (j=1;j<=n;++j)
            {
                if (a[j]%i==0||i%a[j]==0) su=true;
                else { su=false; break; }
            }
            if (su) 
            {
                cout << i << '\n';
                break;
            }
        }
        if (!su) cout << "NO" << '\n';
    }
}   
