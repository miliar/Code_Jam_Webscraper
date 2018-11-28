#include <cstdio>
#include <vector>
#include <sstream>
using namespace std;

int ishappy(int n, int base){
	static char dp[10][20000000];
	char &ret=dp[base-1][n];
		if(ret) return ret;
	if(n==1)
		return 1;
	ret=-1;
	int sum=0;
	while(n){
		sum+=(n%base)*(n%base);
		n/=base;
	}
	ret=ishappy(sum, base);
	return ret;
}

int main(){
	int cases;
	scanf("%d ", &cases);
	for(int casenum=1; casenum<=cases; casenum++){
		char buffer[50];
		gets(buffer);
		istringstream b(buffer);
		int ins;
		vector<int> bases;
		while(b>>ins)
			bases.push_back(ins);
		int i=2;
		while(1){
			int j;
			for(j=0; j<bases.size(); j++)
				if(ishappy(i, bases[j])==-1)
					break;
			if(j==bases.size()){
				printf("Case #%d: %d\n", casenum, i);
				break;
			}
			i++;
		}
	}
	return 0;
}
