#include <string.h>
#include <sstream>
#include <string>
#include <queue>
#include <vector>
#include <set>
#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;
#define ll long long
int is( int x )
{
	return x>0?x:-x;
}
int main()
{
	int T;
	scanf("%d",&T);
	for(int c=0;c<T;)
	{
		int n;
		scanf("%d",&n);
		//printf("n = %d\n",n);
		int poso=1,posb=1;
		int to=0,tb=0;
		int ans=0;
		for(int i=0;i<n;++i)
		{
			char ch;
			int id;
			cin>>ch>>id;
			//cout<<ch<<" "<<id<<endl;
			if( ch == 'O' )
			{
				int tmp = max(is( id - poso ) - tb,0)+1;
				tb = 0;
				to += tmp;
				ans += tmp;
				poso  = id;
			}
			else
			{
				int tmp = max( is( id - posb ) - to, 0 )+1;
				to = 0;
				ans += tmp;
				tb += tmp;
				posb = id;
			}
			//printf("poso(%d) posb(%d) to(%d) tb(%d)\n",poso,posb,to,tb);
		}
		printf("Case #%d: %d\n",++c,ans);
	}
}

