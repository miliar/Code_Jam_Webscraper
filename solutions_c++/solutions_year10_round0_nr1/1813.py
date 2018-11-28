#include <iostream>
using namespace std;

char ans[2][5] = {"OFF","ON"};
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	int index = 0;
	int n,k;
	cin>>T;
	while (T--){
		cin>>n>>k;
		n = 1 << n;
		int res = (k % n == n-1);
		printf("Case #%d: %s\n",++index,ans[res]);
	}
    return 0;
}
