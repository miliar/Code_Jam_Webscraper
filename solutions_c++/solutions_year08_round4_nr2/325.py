#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <bitset>
#include <cstdio>
#include <cmath>
#include <cstdlib>

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

#define eps 1e-8
#define pi acos(-1)

using namespace std;

int area(int x1, int y1, int x2, int y2, int x3, int y3)
{
	return abs(x2*y3 + x1*y2 + y1*x3 - x2*y1 - x3*y2 - y3*x1);
}

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int C;
	cin>>C;
	
	for(int i=0; i<C; i++)
	{
		int N, M, A;
		cin>>N>>M>>A;
		
		cout<<"Case #"<<i+1<<": ";
		bool ok = false;
		
		for(int x1=0; x1<=N; x1++)
		{
			if(ok) break;
			for(int y1=0; y1<=M; y1++)
			{
				if(ok) break;
				for(int x2=0; x2<=N; x2++)
				{
					if(ok) break;
					for(int y2=0; y2<=M; y2++)
					{
						if(ok) break;
						
						if(A == area(x1, y1, x2, y2, 0, 0))
						{
							cout<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<" "<<0<<" "<<0<<endl;
							ok = true;
							break;
						}
						if(A == area(x1, y1, x2, y2, N, 0))
						{
							cout<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<" "<<N<<" "<<0<<endl;
							ok = true;
							break;
						}						
						if(A == area(x1, y1, x2, y2, 0, M))
						{
							cout<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<" "<<0<<" "<<M<<endl;
							ok = true;
							break;
						}						
						if(A == area(x1, y1, x2, y2, N, M))
						{
							cout<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<" "<<N<<" "<<M<<endl;
							ok = true;
							break;
						}
					}
				}
			}
		}
		if(!ok) cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}
