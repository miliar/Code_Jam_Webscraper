#include <stdio.h>
#include <queue>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int main(){
	int cases;
	scanf("%d",&cases);
	
	for(int k=0;k<cases;k++){
		int nums,temp;
		scanf("%d",&nums);
		vector<int> x;
		vector<int> y;
		
		for(int i=0;i<nums;i++){
			scanf("%d",&temp);
			x.push_back(temp);
		}
		for(int i=0;i<nums;i++){
			scanf("%d",&temp);
			y.push_back(temp);
		}
		sort(x.begin(),x.end());
		sort(y.begin(),y.end());
		reverse(y.begin(),y.end());
		long long ans = 0;
		for(int i=0;i<nums;i++){
			ans+=(long long)x[i]*(long long)y[i];
		}
		printf("Case #%d: %lld\n",k+1,ans);		
	}
	
	
}