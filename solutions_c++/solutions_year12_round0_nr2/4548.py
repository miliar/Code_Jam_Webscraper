#include <iostream>
#include <stdio.h>
#include <cstdlib>
#include <cmath>
using namespace std;

bool check(int score, int &s, int p) {
	int num = score/3;
	if(num < p)
		num = score - p;
	else {
		p = num;
		num = score - num;
	}
	if(num >= 0) {
		if (abs(p-num/2)<2) return true;
		
		else
		if (abs(p-num/2)==2 && s >= 1) {
			s--;
			return true;
		}	
	}
	return false;
}

int main() {
	int count,n,s,p,success,score[100];
	scanf("%d", &count);

	for (int i=1; i<=count; ++i) {	
		scanf("%d", &n);
		scanf("%d", &s);
		scanf("%d", &p);
		printf("Case #%d: ", i);
		success = 0;
		for (int j=0; j<n; ++j) {
			scanf("%d", &score[j]);
			if(check(score[j], s, p))
				success++;
		}
		printf("%d\n", success);
	}
	return 0;
}
