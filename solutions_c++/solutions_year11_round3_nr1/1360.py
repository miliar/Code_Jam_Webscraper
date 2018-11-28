#include <algorithm>
#include <iostream>
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
#include <stdio.h>
using namespace std;

long long nod(long long a,long long b)
{
    while(a&&b)
        if(a>b) a=a%b; else b=b%a;
    return a+b;
}

int main()
{
	int T;
	cin>>T;
    for(int t=1;t<=T;t++)
    {
        printf("Case #%d:\n",t);
        int n,m;
        cin>>n>>m;
        char a[55][55];
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
              cin>>a[i][j];

        for(int i=0;i<n-1;i++)
            for(int j=0;j<m-1;j++)
            {
                if(a[i][j]=='#'&&a[i+1][j]=='#'&&a[i][j+1]=='#'&&a[i+1][j+1]=='#')
                {
                    a[i][j]='/';
                    a[i][j+1]='\\';
                    a[i+1][j]='\\';
                    a[i+1][j+1]='/';
                }
            }
            bool f=false;
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                if(a[i][j]=='#')
                {
                    f=true;
                    break;
                }

            if(f)
            {
                printf("Impossible\n");
            }
            else{
                for(int i=0;i<n;i++)
            {
            for(int j=0;j<m;j++)
              cout<<a[i][j];
              cout<<endl;
            }
            }
    }

	return 0;
}
