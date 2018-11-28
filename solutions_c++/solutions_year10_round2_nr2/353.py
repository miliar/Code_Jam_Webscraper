#include <vector>
#include <list>
#include <map>
#include <set>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <climits>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;
 
#define Long long long

int main()
{
	freopen("data.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int C, N, K, B, T;
	cin >> C;
	
	int p[64];
	int v[64];
	bool saved[64];
	
	for (int x=1; x<=C; x++)
	{
		cin >> N >> K >> B >> T;
		fill(saved, saved+64, 0);
		
		for (int i=0; i<N; i++)
			cin >> p[i];
		
		for (int i=0; i<N; i++)
			cin >> v[i];
		
		int gandalf; // YOU SHALL NOT PASS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! :D
		for (gandalf = N-1; gandalf>=0; gandalf--)
			if (B - p[gandalf] <= v[gandalf]*T) continue;
			else break;
		
		int c = 0, extra = 0;
		
		//cout << "gand = " << gandalf << endl;
		//cout << "good so far = " << N-1-gandalf+extra << endl;
		while (N-1-gandalf+extra < K)
		{
			//cout << "good so far = " << N-1-gandalf+extra << endl;
			//cout << "here0\n";
			int inx = gandalf - 1;
			for(; inx>=0; inx--)
				if (!saved[inx] && B - p[inx] <= v[inx]*T) break;
			
			//cout << "inx = " << inx << endl;
			if (inx == -1) goto ohnoes;
			
			saved[inx] = 1;
			extra++;
			
			for (int i=inx+1; i<=gandalf; i++)
				if (!saved[i]) 
				{
					//cout << "had to skip " << i << endl;
					c++;
				}
		}
		
		printf("Case #%d: %d\n", x, c);	
		continue;
		
		ohnoes:
		printf("Case #%d: IMPOSSIBLE\n", x);
	}
		
}