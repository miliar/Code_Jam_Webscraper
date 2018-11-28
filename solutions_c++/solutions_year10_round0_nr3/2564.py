#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>

#define N 100000
 using namespace std;

int g[N];
int main()
{
	 int t,r,k,n,i,j,pt,tsum,sum,flg,cas=1;
	//freopen("factor.in","r",sin);
	freopen("c.out","w",stdout);
	 
	 cin>>t;
	 while(t--)
	 {
		cin>>r>>k>>n;
		for(i=0;i<n;i++)
			cin>>g[i];

		pt=0;
		tsum=0;
		for(i=0;i<r;i++)
		{
			sum=0;flg=0;
			for(j=pt;;j++)
			{
				
				if(j==n)
					j=0;
				if(j==pt&&flg==1)
					break;
				if(g[j]+sum>k)
				{
					pt=j;
					break;
				}
				sum+=g[j];
				flg=1;
			}
		
			tsum+=sum;
		}

		cout<<"Case #"<<cas++<<": "<<tsum<<endl;

	 }
	return 0;
 }
