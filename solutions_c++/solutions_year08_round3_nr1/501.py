#include <stdio.h>
#include <algorithm>

using namespace std;

int main() {
	int ile = 0;
	int cos;
	long p,k,l;
	long wart[10000];
	long wartmp[10000];

	scanf("%d",&ile);



	for (int i = 0; i < ile; ++i) {
		scanf("%ld",&p);
		scanf("%ld",&k);
		scanf("%ld",&l);
//		 %d %d",&p,&k,&l);
		for (int j = 0; j < l; ++j) 
			scanf("%ld", &wart[j]);
//		if (d * p < l)
//			printf("Case #%d: \n",i+1,);
		sort(wart,wart + l);
	
	  
		// odwracanie na szybko
		for (int j = 0; j < l; ++j)
		  wartmp[j] = wart[l- 1 - j];

//		for (int j =0 ; j < l ; ++j)
//			printf("%d ",wartmp[j]);
//		printf("\n");	
		
		long long wyn = 0;
		int x = 1;
		int pom = 0;
		for (int j =0 ; j < l ; ++j) {
			wyn += wartmp[j] * x;
			++pom;
			if (pom == k) {
				pom = 0;
				++x;	
			}
		}

		printf("Case #%d: %lld\n",i+1,wyn);
	}
	
	
	
	

//	for (int i = 0; i < ile; ++i)
//		printf("Case #%d: \n",i+1);

	return(0);
}
