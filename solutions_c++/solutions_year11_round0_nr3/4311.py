#include <iostream>
#include <cstdio>

using namespace std;
#define ll long long 

int main()
{
	int n_test;
	scanf("%d",&n_test);
	for(int i=1; i<=n_test; i++){
		int n_cant;
		scanf("%d", &n_cant);
		int g[n_cant+1];
		for(int j=0; j<n_cant; j++)
			scanf("%d",&g[j]);
		int mayor = -1;
		for(int mask=0; mask < (1<<n_cant); mask++){
			int sumB1=0, sumB2=0, sumD1=0, sumD2=0;
			for(int j=0; j<n_cant; j++){
				if((mask>>j) & 1){
					sumD1 += g[j];
					sumB1 ^= g[j];
					
				}
				else{
					sumD2 += g[j];
					sumB2 ^= g[j]; 
									
				}
			}
			if(sumB1==sumB2 && sumB1 && sumB2)
				mayor = max(mayor, max(sumD1, sumD2));
		}		
		if(mayor!=-1) printf("Case #%d: %d\n",i,mayor);
		else printf("Case #%d: NO\n",i);	
	}	
return 0;}
