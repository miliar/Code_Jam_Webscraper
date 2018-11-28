#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <ctime>

using namespace std;

int D[10005], L[10005], x[10005];

int main()
{
	int nCasos;
	scanf("%d", &nCasos);
	
	for(int caso=1; caso<=nCasos; caso++)
	{
		int N;
		scanf("%d", &N);
		
		for(int i=0; i<N; i++)
			scanf("%d %d", &D[i], &L[i]);
		
		int last;
		scanf("%d", &last);
		
		memset(x, -1, sizeof(x));
		
		x[0] = D[0];
		
		for(int i=0; i<N; i++)
		{
			for(int j=i+1; j<N; j++)
			{
				if(x[i] != -1 && D[j] - D[i] <= x[i])
				{
					x[j] = max(x[j], min(D[j] - D[i], L[j]));
				}
				else break;
			}
		}
		
		bool ok = 0;
		for(int i=0; i<N; i++)
			if(x[i] != -1 && x[i] >= last - D[i])
				ok = 1;
		
		cout<<"Case #"<<caso<<": "<<(ok ? "YES" : "NO")<<endl;
	}
	
	return 0;
}
