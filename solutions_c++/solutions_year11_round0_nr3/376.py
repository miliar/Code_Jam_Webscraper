#include <list>
#include <deque>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <utility>
#include <string>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <sstream>

using namespace std;

int main() {
	int NC;
	cin >> NC;
	for(int cs=1;cs<=NC;cs++) {
		vector<int> nums;
		int N,sum=0,aux1=0,aux2=0,n;
		cin >> N;
		for(int i=0;i<N;i++) {
			cin >> n;
			nums.push_back(n);
			sum+=nums[i];
			aux2=aux2^nums[i];
		}
		sort(nums.begin(),nums.end());
		for(int i=1;i<=N;i++) {
			sum-=nums[i-1];
			aux1=aux1^nums[i-1];
			aux2=aux2^nums[i-1];
			if(aux1==aux2)
				break;
		}
		
		if(aux1 == aux2)
			cout << "Case #" << cs << ": " << sum  << endl;
		else
			cout << "Case #" << cs << ": NO" << endl;
	}
	
	return 0;
}
