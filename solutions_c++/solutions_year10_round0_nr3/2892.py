#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <algorithm>
#include <string>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <ctime>
#include <cmath>
#include <numeric>

using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int,int> pii;

#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)

int main(int argc, char* argv[])
{
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int T;
	scanf("%d", &T);

	For(test, 1, T){
		unsigned long long R,k,N;
		scanf("%llu %llu %llu",&R,&k,&N);
		queue<unsigned long long> groups;
		unsigned long long groupsize;
		unsigned long long total=0;
		unsigned long long totalOne=0;//one ride
		unsigned long long igroup,iRide;
		for(igroup=1;igroup<=N;++igroup){
			scanf("%llu",&groupsize);
			groups.push(groupsize);
			totalOne=totalOne+groupsize;
		}
		if(totalOne<=k){
			total=totalOne*R;
		}
		else{
			for(iRide=1;iRide<=R;++iRide){
				groupsize=groups.front();
				groups.pop();
				totalOne=groupsize;
				groups.push(groupsize);
				while(k>=(totalOne+groups.front())){
					groupsize=groups.front();
					groups.pop();
					totalOne=totalOne+groupsize;
					groups.push(groupsize);
				}
				total=total+totalOne;
			}
		}
		printf("Case #%d: %llu\n", test,total);
	}
}