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
	
	int i,j,k,t,m,n;
	char a[2501];
	
	cin >> t;
	for (int l=1;l<=t;++l)
	{
        printf("Case #%d:\n",l);
        int b[2501]={0};
        int num=0;
        bool su=true;
        cin >> n >> m;
        for (i=1;i<=n;++i) 
            for (j=1;j<=m;++j)
            {
                cin >> a[m*(i-1)+j];
                if (a[m*(i-1)+j]=='#') 
                {
                    ++num;
                    b[num]=m*(i-1)+j;
                }
            }
        for (i=1;i<=num;++i)
        {
            if (b[i]==0) continue;
            if (a[b[i]]=='#'&&a[b[i]+1]=='#'&&a[b[i]+m]=='#'&&a[b[i]+m+1]=='#') 
            {
                a[b[i]]='/';
                a[b[i]+1]='\\';
                a[b[i]+m]='\\';
                a[b[i]+m+1]='/';
                for (j=i;j<=num;++j)
                  if (b[j]==b[i]+m) 
                  {
                        b[j]=0;
                        b[j+1]=0;
                        break;
                  }
                b[i]=0;
                b[i+1]=0;
            }
            else {cout << "Impossible" << '\n'; su=false; break;}
        }
        if (su) for (i=1;i<=n*m;++i)
        {
            cout << a[i];
            if (i%m==0) cout << '\n';
        }
    }                    
}
