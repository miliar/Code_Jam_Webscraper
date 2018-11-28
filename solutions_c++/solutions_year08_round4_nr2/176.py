#include <iostream>
#include <fstream>
#include <set>
#include <string>
#include <cstdio>

using namespace std;

void main()
{
	int i,j,k;
	int c;
	cin>>c;

	int n,m,a;

	for(i=0; i<c; i++)
	{
		cin>>n>>m>>a;
		if(a>n*m)
		{
			cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;	
			continue;
		}
		for(j=1; j<=m; j++)
		{
			if(a%j==0 && a/j<=n)
			{
				printf("Case #%d: %d %d %d %d %d %d\n",i+1,0,0,a/j,0,0,j);	
				break;
			}
		}
		if(j<=m)
			continue;
	
		bool find=false;
		int x2,x3,y2=m,y3;
		for(x2=1; x2<=n; x2++)
		{
			for(x3=1; x3<=n; x3++)
			{
				for(y3=1; y3<=m; y3++)
				{
					if(x2==x3 && y2==y3)
						continue;
					if(abs(x2*y3-x3*y2)==a)
					{
						printf("Case #%d: %d %d %d %d %d %d\n",i+1,0,0,x2,y2,x3,y3);	
						find=true;
						break;
					}
				}
				if(find)
					break;
			}
			if(find)
				break; 
		}
		if(!find)
			cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;	
	}
}
