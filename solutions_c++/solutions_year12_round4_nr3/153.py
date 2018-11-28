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

int main()
{
	int nCasos;
	scanf("%d", &nCasos);
	
	for(int caso=1; caso<=nCasos; caso++)
	{
		int N;
		scanf("%d", &N);
		
		int x[N-1];
		for(int i=0; i<N-1; i++)
			scanf("%d", &x[i]);
		
		bool ok = 0;
		
		for(int it=0; it<5000000; it++)
		{
			int v[N];
			for(int i=0; i<N; i++)
				v[i] = rand() % 1000000;
			
			int y[N-1], vale = 1;
			for(int i=0; i<N-1; i++)
			{
				int ind = i+1;
				for(int j=i+2; j<N; j++)
					if((v[j] - v[i]) * (ind - i) > (v[ind] - v[i]) * (j - i))
						ind = j;
				y[i] = ind + 1;
				
				if(y[i] != x[i])
				{
					vale = 0;
					break;
				}
			}
			
			if(vale)
			{
				cout<<"Case #"<<caso<<":";
				for(int i=0; i<N; i++)
					cout<<" "<<v[i];
				cout<<endl;
				ok = 1;
				break;
			}
		}
		
		if(!ok) cout<<"Case #"<<caso<<": Impossible"<<endl;
	}	
	
	return 0;
}
