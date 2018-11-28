#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;

int n;
vi first;
vi second;
int main() {
	
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	scanf("%d", &n);

	for(int test=1; test<=n; test++) {
		long long ans=0; 
		first.clear();
		second.clear();
		int t;
		scanf("%d", &t);
		for(int i=0; i<t; i++){
			int temp;
			scanf("%d", &temp);
			first.push_back(temp);
		}
		for(int i=0; i<t; i++){
			int temp;
			scanf("%d", &temp);
			second.push_back(temp);
		}
		sort(first.begin(), first.end());
		sort(second.begin(), second.end());
		
		while(!first.empty() &&
			first[0]<0 && second[second.size()-1]>0
			)
		{
			ans+= first[0]*second[second.size()-1];
			first.erase(first.begin());
			second.erase(second.end()-1);
			//cout <<first[0]<<" "<<second[second.size()-1];
		}
		while(!first.empty() &&
			second[0]<0 && first[first.size()-1]>0
			){
			ans+= second[0]*first[second.size()-1];
			second.erase(second.begin());
			first.erase(first.end()-1);
		}
		for(int i=0; i<first.size(); i++){
			ans+=second[first.size()-1-i]*first[i];
		}
		printf("Case #%d: %d\n", test, ans);
	}

	return 0;
}
