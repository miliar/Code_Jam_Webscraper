#include <iostream>
#include <algorithm>
using namespace std;

int n, k;

int main(){
	//freopen("g:\\in.txt","r",stdin);
	freopen("g:\\A-large.in","r",stdin);	
	freopen("g:\\out.txt", "w", stdout);
	int num_case;
	scanf("%d",&num_case);
	for( int i=1; i<=num_case; ++i ){
		scanf("%d%d", &n,&k);
		printf("Case #%d: ",i);
		if( (k&((1<<n)-1))==((1<<n)-1) )
			puts("ON");
		else
			puts("OFF");
	}
	return 0;
}
