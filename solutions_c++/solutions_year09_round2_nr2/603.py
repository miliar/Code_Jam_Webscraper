#include <cstdio>
#include <iostream>
#include <sstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>

using namespace std;

int main(){
	int tc, tcN;
	
	scanf("%d ", &tcN);
	for(tc=1; tc<=tcN; ++tc){
		vector<int> v;
		char c;
		for(c = getchar(); isdigit(c); c = getchar()){
			v.push_back(c-'0');
		}
		int add = 0;
		add = !next_permutation(v.begin(), v.end());
		printf("Case #%d: ", tc);
		int i=0;
		for(i=0; i<(int)v.size(); ++i){
			if(!v[i])
				++add;
			else
				break;
		}
		for(; i<(int)v.size(); ++i){
			printf("%d", v[i]);
			for(int j=0; j<add; ++j)
				printf("0");
			add = 0;
		}
		puts("");
	}
}
