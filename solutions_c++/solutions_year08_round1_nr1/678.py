#include <cstdlib>
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>
#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
	FILE *in  = fopen("A-small-attempt1.in","r");
	FILE *out = fopen("A-small-attempt1.out","w");
	int tests;
	
	fscanf(in,"%d",&tests);
	for(int t = 0; t<tests; t++){
		vector<int> X,Y;
		int ret = 0;
		int n,tmp;
		fscanf(in,"%d",&n);
		
		for(int i = 0; i<n; i++){
			fscanf(in,"%d",&tmp);
			X.push_back(tmp);
		}

		for(int i = 0; i<n; i++){
			fscanf(in,"%d",&tmp);
			Y.push_back(tmp);
		}
		
		sort(X.begin(), X.end());
		sort(Y.begin(), Y.end(), greater<int>());
		long long sum = 0;
		for(int i = 0; i<X.size(); i++)
			sum += X[i]*Y[i];
		fprintf(out,"Case #%d: %I64d\n",t+1,sum);
	}
	
	fscanf(in,"\n");
    return EXIT_SUCCESS;
}
