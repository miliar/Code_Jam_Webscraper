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
#include <ctime>
#include <cfloat>
#include <cstring>

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int nCasos;
	cin>>nCasos;
	
	for(int caso=1; caso<=nCasos; caso++)
	{
		cout<<"Case #"<<caso<<": ";
		
		int R, C, k;
		cin>>R>>C>>k;
		
		vector <string> M(R);
		
		for(int i=0; i<R; i++)
			cin>>M[i];
		
		int SX[R][C];
		
		for(int i=0; i<R; i++)
		{
			int S = 0;
			for(int j=0; j<C; j++)
			{
				S += M[i][j]-'0';
				SX[i][j] = S;
			}
		}
		
		int SY[R][C];
		
		for(int j=0; j<C; j++)
		{
			int S = 0;
			for(int i=0; i<R; i++)
			{
				S += M[i][j]-'0';
				SY[i][j] = S;
			}
		}
		
		int maxK = 0;
		
		for(int i=0; i+2<R; i++)
		{
			for(int j=0; j+2<C; j++)
			{
				for(int k=min(R-i,C-j); k>=3; k--)
				{
					if(k < maxK) break;
					
					//
					
					int D1 = 0;
					
					for(int w=0; w<k; w++)
					{
						int d1 = k - 1 - 2*w;

						int p1 = SX[i+w][j+k-1] - (j > 0 ? SX[i+w][j-1] : 0);
						if(w==0 || w == k-1) p1 -= M[i+w][j] - '0' + M[i+w][j+k-1] - '0';
						
						D1 += d1 * p1;
					}
					
					if(D1 != 0) continue;
					
					//
					
					int D2 = 0;
					
					for(int w=0; w<k; w++)
					{
						int d1 = k - 1 - 2*w;

						int p1 = SY[i+k-1][j+w] - (i > 0 ? SY[i-1][j+w] : 0);
						if(w==0 || w == k-1) p1 -= M[i][j+w] - '0' + M[i+k-1][j+w] - '0';
						
						D2 += d1 * p1;
					}
					
					if(D2 != 0) continue;
					
					maxK = max(maxK, k);
				}
			}
		}
		
		if(maxK == 0) cout<<"IMPOSSIBLE"<<endl;
		else cout<<maxK<<endl;
	}
	
	return 0;
}

