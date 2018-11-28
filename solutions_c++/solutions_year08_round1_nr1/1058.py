#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int va[1000];
int vb[1000];

int main(){

	int ans=0;
	int testcase , ts;
	int n;

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	scanf("%d",&testcase);

	for(int ts=1;ts<=testcase;ts++){
	
		ans=0;
		scanf("%d",&n);

		for(int i=0;i<n;i++)
			scanf("%d",&va[i]);
		for(int i=0;i<n;i++)
			scanf("%d",&vb[i]);

		sort(va,va+n);
		sort(vb,vb+n,greater<int>());

		for(int i=0;i<n;i++)
			ans += va[i]*vb[i];

		
		printf("Case #%d: %d\n",ts,ans);
	}


	return 0;
}