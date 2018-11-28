#include <stdio.h>
#include <stdlib.h>

#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> i;

int main() {
	int t,c,n;
	cin>>t;
	
	int casen=1;
	
	while(t--) {
		// read
		cin>>n;
		int xsum=0;
		int sum2=0;
		int min=-1;
		for (int i=0;i<n;i++) {
			cin>>c;
			xsum=xsum^c;
			sum2+=c;
			if (min==-1||min>c) min=c;
		}
		
		//
		printf("Case #%d: ",casen);
		//print result
		if (xsum!=0) {
			printf("NO");
		} else {
			printf("%d",sum2-min);
		}
		//
		printf("\n");
		casen++;
	}
}
