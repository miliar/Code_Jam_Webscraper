#include <iostream>
#include <cstdlib>
#include <limits.h>

using namespace std;

int main()
{
	int t,n,test = 0;
	cin >> t;
	while(t--){
		cin >> n;
		test++;
		int *AA = (int*)malloc(sizeof(int)*n);
		int xr = 0,sum = 0;
		int mval = INT_MAX;
		for(int i=0;i<n;i++){
			cin >> AA[i];
			xr ^= AA[i];
			mval = min(mval , AA[i]);
			sum += AA[i];
		}
		if(xr != 0)
			cout <<"Case #"<<test<<": "<<"NO\n";
		else
			cout <<"Case #"<<test<<": "<< sum-mval<<"\n";
	}
		
	return 0;
}
