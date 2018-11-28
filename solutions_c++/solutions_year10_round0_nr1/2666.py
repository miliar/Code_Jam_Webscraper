#include <iostream>

using namespace std;

int main(){
	int ts, n, k;

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	scanf("%d",&ts);

	for(int t=1;t<=ts;t++){
		scanf("%d %d",&n,&k);

		bool flag = true;
		for(int i=0;i<n;i++){
			if(((1<<i)&k) == 0)
				flag = false;
		}
		printf("Case #%d: %s\n", t,flag ? "ON" : "OFF");
	}

	return 0;
}