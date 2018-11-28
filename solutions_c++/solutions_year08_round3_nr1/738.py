#include <iostream>
#include <vector>
#include <map>
#include <sstream>
#include <deque>
#include <algorithm>
using namespace std;


void main()
{
	int t_case=1;
	int N, P, K, L;
	int i,j,k;
	int freq;
	int sol;

//	vector< vector<int> > keys;
	vector<int> input;

	scanf_s("%d",&N);
	for(; t_case < N+1; ++t_case)
	{
		scanf_s("%d %d %d", &P, &K, &L);
		
		input.reserve(L);
		for(i=0; i< L; ++i){
			scanf_s("%d",&freq);
			input.push_back(freq);
		}
		sort(input.begin(), input.end(), greater<int>());
		
		k=0;
		sol=0;
		for(i=0; i < P ; ++i){
			for(j=0; j < K && k < L; ++j, ++k){
				sol += input[k]*(i+1);
			}
		}
		printf("Case #%d: %d\n",t_case, sol);
		input.clear();
	}
}
