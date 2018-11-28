#include <iostream>

using namespace std;

bool arr[100];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	scanf("%d",&t);
	int test = 0;
	while (t--){
		int n,k;
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",++test);
		if (((k + 1) % (1 << n)) == 0)
			printf("ON\n");
		else
			printf("OFF\n");			
	}

	return 0;
}