#include <iostream>
#include <stdio.h>

using namespace std;

int main(){

	int testCases,i,j,power,digits,a,b,inp,count;
	int work,powerTen;
	int lookedUp[10];
	scanf("%d",&testCases);
	for(int i =1; i<= testCases; i++){
		count = 0;
		scanf("%d",&a);
		scanf("%d",&b);
		int tmp = a;
		int digits = 1;
		int powerTen = 1;
		while(tmp/10){
			digits++;
			tmp = tmp/10;
			powerTen = powerTen * 10;
		}
		
		for(int j=a;j<=b;j++){
			int src = j;
			int tmpCount = 1;
			work = src;
			for(tmp = 1;tmp<digits; tmp++){
				lookedUp[tmp] = -100;
			}
			for(int d = 1;d < digits; d++){
				work = (work % powerTen) * 10 + (work/powerTen);
				//printf("src = %d and work = %d\n",src,work);
				if(work > src && work <= b ){
					int seenFlag = 0;
					for(tmp = 1; tmp < tmpCount; tmp++){
						if(lookedUp[tmp] == work){
							seenFlag = 1;
							break;
						}
					}
					if(seenFlag == 0){
						count++;
						lookedUp[tmpCount++] = work;
					}
				}
			}
		}
		printf("Case #%d: %d\n",i,count);
	}
	return 0;
}
	
		