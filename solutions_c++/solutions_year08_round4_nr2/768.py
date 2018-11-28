#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <functional>
#include <map>
#include <set>
#include <cassert>
#include <list>
#include <deque>
#include <iomanip>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cctype>
#include <queue>
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b)) 
using namespace std;

int main()
{
	int C;
	int count=1;
	cin>>C;
	while(C--)
	{
		int N,M,A;
		cin>>N>>M>>A;
		int x1,x2,y1,y2,flag=0;
		for(x1=0;x1<=N;x1++)
		{
			for(x2=0;x2<=N;x2++)
			{
				for(y1=0;y1<=M;y1++)
				{
					for(y2=0;y2<=M;y2++)
					{
						if(x1==x2 && y1==y2)
							continue;
						if(abs((x2*y1)-(y2*x1))==A)
							flag=1;
						if(flag)
							break;
					}
					if(flag)
						break;
				}
				if(flag)
					break;
			}
			if(flag)
				break;
		}
		if(flag)
			cout<<"Case #"<<count<<": "<<"0 0 "<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<endl;
		else
			cout<<"Case #"<<count<<": IMPOSSIBLE"<<endl;
		count++;
	}
	return 0;
}

			
				

		

