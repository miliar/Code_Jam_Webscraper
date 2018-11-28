#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int nCasos;
	cin>>nCasos;
	
	for(int caso=1; caso<=nCasos; caso++)
	{
		int N, T = 0, x = 0;
		cin>>N;
		
		vector <int> v(N);
		
		for(int i=0; i<N; i++)
		{
			cin>>v[i];
			T += v[i];
			x ^= v[i];
		}
		
		sort(v.begin(), v.end());
		
		if(x==0) cout<<"Case #"<<caso<<": "<<T -  v[0]<<endl;
		else cout<<"Case #"<<caso<<": NO"<<endl;
	}
	
	return 0;	
}
