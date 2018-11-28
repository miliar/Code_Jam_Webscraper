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
	long long n,d,g,l,h;
	cin>>T;
    for(int t=1;t<=T;t++)
    {
        printf("Case #%d: ",t);
        int a[10005];
        cin>>n>>l>>h;
        for(int i=0;i<n;i++)
            cin>>a[i];

        bool rr=false;
        for(int j=l;j<=h;j++)
        {
            bool f=false;
            for(int i=0;i<n;i++)
            {
                if(!(j%a[i]==0||a[i]%j==0))
                    {
                        f=true;
                        break;
                    }
            }
            if(!f)
            {
                cout<<j<<endl;
                rr=true;
                break;
            }
        }
        if(rr)
            continue;
        else
            cout<<"NO\n";


    }

	return 0;
}
