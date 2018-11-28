#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;




int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	char a[100][100];
	int r,c;
	int tnum;
	cin>>tnum;
	
	for(int q=1;q<=tnum;q++)
	{
		cin>>r>>c;
		cin.get();
		for(int i=0;i<r;i++) gets(a[i]);
		for(int i=0;i<r-1;i++)
		{
			for(int j=0;j<c-1;j++)
			{
				j = j;
				if(a[i][j]=='#' && a[i+1][j]=='#' && a[i][j+1]=='#' && a[i+1][j+1]=='#')
				{ 
					a[i][j]='/';
					a[i+1][j]='\\';
					a[i][j+1]='\\'; 
					a[i+1][j+1]='/'; 
				}
			}
		}	
		bool flag=true;
		for(int i=0;i<r;i++)
			for(int j=0;j<c;j++)
				if(a[i][j]=='#') 
				{flag=false;break;}
		printf("Case #%d:\n",q);
		if(!flag)
			puts("Impossible");
		else
		{
			for(int i=0;i<r;i++)
				puts(a[i]);
		}
	}
}