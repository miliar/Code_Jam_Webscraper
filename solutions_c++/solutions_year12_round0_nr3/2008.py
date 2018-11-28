#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int main(){
	int casos;
	int ans;
	int a,b;
	cin>>casos;
	bool visitados[2000005];
	for (int caso=1; caso<=casos; caso++){
		scanf("%d %d", &a, &b);
		
		for (int i=a; i<=b; i++){
			visitados[i]=false;
		}
		ans=0;
		for (int i=a; i<b; i++){
			if (visitados[i]) continue;
			visitados[i]=true;
			int crot=1;
			int rot=0;
			int p10=1;
			int k=10;
			int m,n;
			while (p10<i) p10*=10;
			while (k<p10){
				rot=(i%k)*(p10/k)+i/k;
				if (rot<=b && rot>i && !visitados[rot]){
					//printf("%d %d %d %d\n", i,rot, p10, k);
					visitados[rot]=true;
					crot++;
				}
				k*=10;
			}
			ans+=crot*(crot-1)/2;
		}
		
		printf("Case #%d: %d\n", caso, ans);
	}
	
	return 0;
}
