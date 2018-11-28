#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;

int calc(vector<int>& input, vector<int>& perm){
	vector<int> v;
	int k = perm.size();
	for(int i = 0; i < input.size(); ++i){
		int base = i - (i % k);
	       	v.push_back(input[base + perm[i % k]]);
	}
	if (input.size() == 0) return 0;
	int ret = 1;
	for(int i = 1; i < v.size(); ++i) if (v[i] != v[i-1]) ret++;
	return ret;
}


int main(){
	int t;
	scanf("%d\n",&t);
	for(int testCase = 1; testCase <= t; ++testCase){
		int k;
		char buffer[1024];
		scanf("%d\n",&k);
		scanf("%s\n",buffer);
		vector<int> perm;
		for(int i = 0; i < k; ++i) perm.push_back(i);
		vector<int> input;
		for(int i = 0; i < strlen(buffer); ++i) input.push_back(buffer[i]-'a');
		int ret = input.size();
		do{
			//printf("perm...\n");
			//for(int i=0; i < perm.size(); ++i) printf("%d ",perm[i]);
			//printf("\n");
			ret = min(ret, calc(input, perm));

		}while(next_permutation(perm.begin(), perm.end()));

		printf("Case #%d: %d\n",testCase, ret);

	}

}
