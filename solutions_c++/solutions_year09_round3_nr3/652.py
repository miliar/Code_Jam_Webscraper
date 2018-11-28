#include <stdafx.h>
#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

int getcost(int * start, int * end, int prisoners) {
	int prs[101];
	for (int i=0; i<prisoners;i++) prs[i]=1;
	int cost = 0;

	while (start != end) {
		prs[(*start)-1] = 0;
		
		for (int j=(*start);j<prisoners;j++) {
			if (prs[j] > 0) {
				cost++;
			} else break;
		}
		
		for (int j=(*start)-2;j>=0;j--) {
			if (prs[j] > 0) {
				cost++;
			} else break;
		}
		start++;

		
	}
	return cost;
}


int main() {
	freopen("C:\\Users\\Anton\\Documents\\Visual Studio 2008\\Projects\\codejamcpp\\Debug\\input.in", "r", stdin);
	freopen("C:\\Users\\Anton\\Documents\\Visual Studio 2008\\Projects\\codejamcpp\\Debug\\output.out", "w", stdout);
	
	int t = 0;
    int T; 
	scanf("%d",&T); 


	long long res[10000];


	while (T--) 
	{
		t++;
        int P, Q; 
		scanf("%d %d",&P,&Q);
		int torelease[101];
		
		for (int i=0; i<Q; i++) {
			scanf("%d", &torelease[i]);
		}
          int i = 0;
        do
		{
            res[i] = getcost(torelease, torelease+Q, P);
			i++;
			
        }while(next_permutation(torelease, torelease+Q));

		int n = *min_element(res, res+i);
        printf("Case #%d: %d\n",t,n);
    }

	fclose(stdin);
	fclose(stdout);
}
