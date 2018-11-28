#include <iostream>
using namespace std;


int test,n,k,t;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	scanf("%i",&test);
	for (int tt=1; tt<=test; tt++) {
		printf("Case #%i: ",tt);
		scanf("%i%i",&n,&k);

		k++;
		t=1;
		for (int i=0; i<n; i++)
			t*=2;
		if (k%t==0) printf("ON\n");
		else printf("OFF\n");
	}
	
	return 0;
}
