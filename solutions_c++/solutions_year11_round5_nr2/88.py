#include <iostream>
#include <string>
#include <cstring>
#include <string.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>

using namespace std;

int a[11000];

void solve(int tst){
	printf("Case #%d: ",tst);
	int n;
	scanf("%d",&n);
	memset(a,0,sizeof(a));
	for (int i=0; i<n; i++){
		int x;
		scanf("%d",&x);
		a[x]++;
	}

	int ans=1000000;
	for (int i=0; i<11000; i++)
		if (a[i]!=0){
			int curval=a[i];
			for (int j=0; j<curval; j++){
				int tek=1;
				int l=i+1;
				while (a[l]>=a[l-1]) tek++, l++;
				ans=min(ans,tek);
				for (int k=i; k<l; k++)
					a[k]--;
			}
		}
	if (ans==1000000) printf("0\n"); else
		printf("%d\n",ans);
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	scanf("%d",&tests);

	for (int tt=1; tt<=tests; tt++){
		solve(tt);
		cerr<<tt<<endl;
	}

	return 0;
}