#include <stdio.h>
#include <stdlib.h>

int main(){

	int testy,x, i, rozsah1,rozsah2, num1,num2,pocet,predpona,pripona,pocitadlo;

	scanf("%d", &testy);

	for(x=1;x<=testy;x++){
		scanf("%d %d", &rozsah1,&rozsah2);

		pocitadlo = 0;


		if (rozsah1>(-1) && rozsah2<10)                  // dvojciferne
			printf("Case #%d: %d\n", x, pocitadlo);

		if (rozsah1>9 && rozsah2<100){
			for (i=rozsah1;i<=rozsah2;i++){
				pripona = i/10;
				predpona = i % 10;
				num2 = predpona*10 + pripona;

				if ((num2 > i) && (num2 <= rozsah2) && (num2 >= rozsah1)){
					//printf("%d ",num2);
					pocitadlo++;
				}
			}
			printf("Case #%d: %d\n", x, pocitadlo);
		}

		if (rozsah1>99 && rozsah2<1000){					// trojciferne
			
			for (i=rozsah1;i<=rozsah2;i++){
				pripona = i/10;
				predpona = i % 10;
				num2 = predpona*100 + pripona;

				if ((num2 > i) && (num2 <= rozsah2) && (num2 >= rozsah1)){
					//printf("%d ",num2);
					pocitadlo++;
				}

			}

			for (i=rozsah1;i<=rozsah2;i++){
				pripona = i/100;
				predpona = i % 100;
				num2 = predpona*10 + pripona;

				if ((num2 > i) && (num2 <= rozsah2) && (num2 >= rozsah1)){
					//printf("%d ",num2);
					pocitadlo++;
				}

			}

			printf("Case #%d: %d\n", x, pocitadlo);
		}

		if (rozsah1>999 && rozsah2<10000){					// stvorciferne
			
			for (i=rozsah1;i<=rozsah2;i++){
				pripona = i/10;
				predpona = i % 10;
				num2 = predpona*1000 + pripona;

				if ((num2 > i) && (num2 <= rozsah2) && (num2 >= rozsah1)){
					//printf("%d ",num2);
					pocitadlo++;
				}

			}

			for (i=rozsah1;i<=rozsah2;i++){
				pripona = i/100;
				predpona = i % 100;
				num2 = predpona*100 + pripona;

				if ((num2 > i) && (num2 <= rozsah2) && (num2 >= rozsah1)){
					//printf("%d ",num2);
					pocitadlo++;
				}

			}
			for (i=rozsah1;i<=rozsah2;i++){
				pripona = i/1000;
				predpona = i % 1000;
				num2 = predpona*10 + pripona;

				if ((num2 > i) && (num2 <= rozsah2) && (num2 >= rozsah1)){
					//printf("%d ",num2);
					pocitadlo++;
				}

			}

			printf("Case #%d: %d\n", x, pocitadlo);
		}

	}

	return 0;

}