#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int l,n,c;
long long t;

int dist[1000000];
int map[1000000];
long long timeTaken[1000000];
long long timeSaved[1000000];

int main(){
	int tc,tn;
	int i,j,k;
	bool first;
	long long res;

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	cin >> tc;
	for (tn=0; tn<tc; tn++){
		cin >> l >> t >> n >> c;
		for (i=0; i<c; i++)
			cin >> dist[i];
		j=0;
		for (i=0; i<n; i++){
			map[i] = dist[j++];
			if (j>=c)
				j=0;
		}

		timeTaken[0] = 2*map[0];
		for (i=1; i<n; i++)
			timeTaken[i] = 2ll*(long long)map[i]+timeTaken[i-1];

		first = false;
		for (i=0; i<n; i++){
			if (timeTaken[i]<=t)
				timeSaved[i] = 0;
			else{
				if (!first){
					first = true;
					timeSaved[i] = (timeTaken[i]-t)/2;
				}
				else
					timeSaved[i] = map[i];
			}
		}
		
		sort(timeSaved,timeSaved+n);
		res = timeTaken[n-1];
		for (i=0; i<l; i++)
			res-=timeSaved[n-1-i];

		printf("Case #%d: %lld\n", tn+1, res);

	}
	return 0;
}