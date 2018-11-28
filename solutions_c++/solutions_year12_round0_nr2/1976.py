#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int main(){
	int casos;
	int n,s,p;
	int g,num, mns, ms, pos;
	cin>>casos;
	for (int caso=1; caso<=casos; caso++){
		g=0;
		pos=0;
		printf("Case #%d: ",caso);
		scanf("%d %d %d", &n, &s, &p);
		mns = 3*p-2;
		ms = 3*p-4;
		if (p==1) ms=2;
		for (int i=0; i<n; i++){
			scanf("%d", &num);
			if (num>=mns){
				g++;
				continue;
			}
			if (num>=ms) pos++;
		}
		g+=min(pos,s);
		printf("%d\n",g);
	}
	
	return 0;
}
