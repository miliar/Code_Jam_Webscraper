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

int L[1005], P[1005], idx[1005];

bool orden(int id1, int id2)
{
	int val1 = 100*L[id1] + P[id1] * L[id2];
	int val2 = 100*L[id2] + P[id2] * L[id1];
	
	if(val1 != val2) return val1 < val2;
	else return id1 < id2;
}

int main()
{
	int nCasos;
	scanf("%d", &nCasos);
	
	for(int caso=1; caso<=nCasos; caso++)
	{
		int N;
		scanf("%d", &N);
		
		for(int i=0; i<N; i++)
			scanf("%d", &L[i]);
		
		for(int i=0; i<N; i++)
		{
			scanf("%d", &P[i]);
			P[i] = 100 - P[i];
		}
		
		for(int i=0; i<N; i++)
			idx[i] = i;
		
		sort(idx, idx + N, orden);
		
		cout<<"Case #"<<caso<<":";
		
		for(int i=0; i<N; i++)
			cout<<" "<<idx[i];
		
		cout<<endl;
	}
	
	return 0;
}
