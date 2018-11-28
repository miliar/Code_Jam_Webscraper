#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> x,y;
int n,m;

int main(){
	int i,j,p;

	scanf("%d",&n);
	for (i=0;i<n;i++){
		scanf("%d",&m);
		x.clear();
		y.clear();
		for (j=0;j<m;j++){
			scanf("%d",&p);
			x.push_back(p);
		}
		for (j=0;j<m;j++){
			scanf("%d",&p);
			y.push_back(p);
		}
		sort(x.begin(),x.end());
		sort(y.rbegin(),y.rend());
		long long sum=0;
		for (j=0;j<m;j++){
			sum+=x[j]*y[j];
		}
		printf("Case #%d: %d\n",i+1,sum);
	}
	return 0;
}
