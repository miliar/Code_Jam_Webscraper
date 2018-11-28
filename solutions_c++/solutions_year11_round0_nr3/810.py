#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <cstdio>
#include <climits>
#include <cmath>
using namespace std;

int main()
{
	int T; cin>>T;
	for(int ds=1;ds<=T;ds++)
	{
		int N; cin>>N;
		vector<int> pieces(N);
		for(int i=0;i<N;i++)
			cin>>pieces[i];
		
		sort(pieces.begin(),pieces.end());
		
		int patrick=pieces[0];
		int sean=0;
		int total=0;
		for(int i=1;i<N;i++)
		{
			sean^=pieces[i];
			total+=pieces[i];
		}
		
		if(sean!=patrick)
			printf("Case #%d: NO\n",ds);
		else
			printf("Case #%d: %d\n",ds,total);
	}
	return 0;
}
