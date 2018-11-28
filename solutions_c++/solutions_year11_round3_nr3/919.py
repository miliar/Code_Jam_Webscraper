/*
 * A.cpp
 *
 *  Created on: May 22, 2011
 *      Author: SICO
 */
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
using namespace std;
int num[101];
int n,l,h;
int main()
{
	freopen("a.in","rt",stdin);
	freopen("a.out","wt",stdout);
	int t;
	scanf("%d",&t);
	for(int x=1;x<=t;++x)
	{
		scanf("%d%d%d",&n,&l,&h);
		for(int i=0;i<n;++i)
			scanf("%d",&num[i]);
		int r;
		bool f=1;
		for(int i=l;i<=h;++i)
		{
			f=true;
			for(int j=0;j<n;++j)
			{
				//cout<<i<<endl;
				if(i>=num[j] && i%num[j])
				{
					f=false;
					break;
				}
				if(i<num[j] && num[j]%i)
				{
					f=false;
					break;
				}
			}
			if(f) {r=i;break;}
		}
		if(f) printf("Case #%d: %d\n",x,r);
		else 	printf("Case #%d: NO\n",x);
	}

}
