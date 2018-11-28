#include <iostream>
#include <cmath>
using namespace std;

main(){
	int z;
	cin >> z;
	
	for(int l=1; l<=z; l++){
		int n, m, a;
		
		cin >> n >> m >> a;
		
		int ok = 0;
		
		for(int x1=0; x1<=n; x1++){
			for(int x2=0; x2<=n; x2++){
				for(int y1=0; y1<=m; y1++){
					for(int y2=0; y2<=m; y2++){
						if(abs(x1*y2-y1*x2) == a){
							ok = 1;
							printf("Case #%d: %d %d %d %d %d %d\n", l, 0, 0, x1, y1, x2, y2);
							x1=x2=y1=y2 = 1000000;
							break;
						}
					
					}
				}
			}		
		} 
		

		if(ok == 0){
			printf("Case #%d: IMPOSSIBLE\n", l);
		}
	
	}

}

