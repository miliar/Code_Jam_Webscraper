#include <vector>
#include <cstdio>
#include <iostream>
using namespace std;

#define mp make_pair
int abs(int a){
    return (a>0)?a:-a;
}

int main(){
	freopen("output.txt","w",stdout);
	vector<int> a;
	int n, t, k, sum, mn, x;
	scanf("%d",&t);
	for(int test = 1; test<= t;test++ ){
		scanf("%d",&n);
		sum = 0; 
		for(int i=0;i<n;i++){
			scanf("%d",&k);
			//a.push_back(k);
			sum +=k;
			mn = (i == 0)?k:min(mn,k);
			x = (i == 0)?k:x^k;
		}
		if(x != 0)
			printf("Case #%d: NO\n",test);
		else
			printf("Case #%d: %d\n",test,sum - mn);
	}
	return 0;
}
