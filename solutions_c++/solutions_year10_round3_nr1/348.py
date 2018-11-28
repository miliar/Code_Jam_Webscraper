#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

struct node {
	int a, b;
};
node wire[1100];
bool iscross(int i, int j){
	if((wire[i].a-wire[j].a)*(wire[i].b-wire[j].b)<0)
		return true;
	return false;
}

int tc, n, ans;

int main(){
	scanf("%d", &tc);
	int i, j;
	for(int t=1; t<=tc; t++){
		cin>>n;
		for(i=0; i<n; i++){
			cin>>wire[i].a>>wire[i].b;
		}
		ans = 0;
		for(i=0; i<n; i++){
			for(j=i+1; j<n; j++){
				if(iscross(i, j))
					ans++;
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
