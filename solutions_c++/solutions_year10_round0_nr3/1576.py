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
#include <cstring>

using namespace std;

long long N;
long long visited[1000];
long long next[1000];
long long Q[1000];

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int nCasos;
	cin>>nCasos;
	
	for(int caso=1; caso<=nCasos; caso++)
	{
		long long R, k;
		cin>>R>>k>>N;

		vector <long long> V(2*N);
		for(int i=0; i<N; i++)
		{
			cin>>V[i];
			V[i+N] = V[i];
		}
		
		long long left = 0, right = 0;
		long long S = V[0];
		for(left = 0; left < N; left++)
		{
			while(right+1-left < N && S + V[right+1] <= k)
			{
				right++;
				S+=V[right];
			}

			next[left] = (right+1)%N;
			Q[left] = S;

			S -= V[left];
		}
		
		memset(visited, -1, sizeof(visited));
		long long p = 0, t = 0, L;
		while(1)
		{
			if(visited[p]!=-1)
			{
				L = t - visited[p];
				break;
			}
			
			visited[p] = t;
			p = next[p];

			t++;
		}

		long long x = 0;
		
		long long q = 0;
		for(int i=0; i<min(R, visited[p]); i++)
		{
			x += Q[q];
			q = next[q];
		}
		
		long long falta = max(0LL, R-visited[p]);
		
		long long nCiclos = falta/L;
		
		long long Sciclo = 0; 
		q = p;
		while(1)
		{
			Sciclo += Q[q];
			q = next[q];
			if(q==p) break;
		}

		x += nCiclos * Sciclo;

		long long r = falta%L;
		q = p;
		for(int i=0; i<r; i++)
		{
			x += Q[q];
			q = next[q];
		}

		cout<<"Case #"<<caso<<": "<<x<<endl;
	}
	
	return 0;
}
