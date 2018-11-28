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
		int N,K; cin>>N>>K;
		
//		vector<bool> snappers(N,false);
//		for(int k=0;k<K;k++)
//		{}
		
		int mask=((1<<N)-1);
		int k=(mask&K);
		bool ans=((k^mask)==0);
		printf("Case #%d: %s\n",ds,(ans)?"ON":"OFF");
	}
	return 0;
}
