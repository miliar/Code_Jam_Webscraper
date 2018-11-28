#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int cmp(const void * elem1, const void * elem2){
	if(strcmp((char*)elem1, (char*)elem2) == 0){
		if(*((char*)elem1 + 9) == 'T')
			return -1;
		else if(*((char*)elem2 + 9) == 'T')
			return 1;
	}
	return strcmp((char*)elem1, (char*)elem2);
}

int main(){
	int		a, b, i, j, k, n, N, T, NA, NB, ptrA, ptrB, useA, useB, ableA, ableB;
	char	timeA[105][10], timeB[105][10];
	FILE	*fout;
	fout = fopen("Bout.txt", "w");
	scanf("%d", &N);
	n = 1;
	while(n <= N){
		scanf("%d%d%d", &T, &NA, &NB);
		for(i = 0; i < 2 * NA; i += 2){
			scanf("%s%s", timeA[i], timeA[i + 1]);
			timeA[i][9] = 'F';
			timeA[i + 1][9] = 'T';
			if(atoi(timeA[i + 1] + 3) + T < 60){
				b = (atoi(timeA[i + 1] + 3) + T) % 10;
				a = (atoi(timeA[i + 1] + 3) + T) / 10;
				timeA[i + 1][4] = b + 48;
				timeA[i + 1][3] = a + 48;
			}
			else{
				timeA[i + 1][2] = '\0';
				b = (atoi(timeA[i + 1]) + 1) % 10;
				a = (atoi(timeA[i + 1]) + 1) / 10;
				timeA[i + 1][1] = b + 48;
				timeA[i + 1][0] = a + 48;
				b = (atoi(timeA[i + 1] + 3) + T - 60) % 10;
				a = (atoi(timeA[i + 1] + 3) + T - 60) / 10;
				timeA[i + 1][4] = b + 48;
				timeA[i + 1][3] = a + 48;
				timeA[i + 1][2] = ':';
			}
		}
		for(i = 0; i < 2 * NB; i += 2){
			scanf("%s%s", timeB[i], timeB[i + 1]);
			timeB[i][9] = 'F';
			timeB[i + 1][9] = 'T';
			if(atoi(timeB[i + 1] + 3) + T < 60){
				b = (atoi(timeB[i + 1] + 3) + T) % 10;
				a = (atoi(timeB[i + 1] + 3) + T) / 10;
				timeB[i + 1][4] = b + 48;
				timeB[i + 1][3] = a + 48;
			}
			else{
				timeB[i + 1][2] = '\0';
				b = (atoi(timeB[i + 1]) + 1) % 10;
				a = (atoi(timeB[i + 1]) + 1) / 10;
				timeB[i + 1][1] = b + 48;
				timeB[i + 1][0] = a + 48;
				b = (atoi(timeB[i + 1] + 3) + T - 60) % 10;
				a = (atoi(timeB[i + 1] + 3) + T - 60) / 10;
				timeB[i + 1][4] = b + 48;
				timeB[i + 1][3] = a + 48;
				timeB[i + 1][2] = ':';
			}
		}
		qsort(timeA, 2 * NA, 10 * sizeof(char), cmp);
		qsort(timeB, 2 * NB, 10 * sizeof(char), cmp);
		/*for(i = 0; i < 2 * NA; i ++){
			printf("ya = %s type = %c\n", timeA[i], timeA[i][9]);
		}
		for(i = 0; i < 2 * NB; i ++){
			printf("no = %s type = %c\n", timeB[i], timeB[i][9]);
		}*/
		ptrA = 0;
		ptrB = 0;
		ableA = 0;
		ableB = 0;
		useA = 0;
		useB = 0;
		while(ptrA != 2 * NA || ptrB != 2 * NB){
			if(ptrA != 2 * NA && strcmp(timeA[ptrA], timeB[ptrB]) < 0){
 				//printf("A < B A = %s B = %s type = %c type = %c\n", timeA[ptrA], timeB[ptrB], timeA[ptrA][9], timeB[ptrB][9]);
				//system("pause");
				if(timeA[ptrA][9] == 'F'){
					if(ableA == 0){
						useA ++;
					}
					else if(ableA > 0){
						ableA --;
					}
				}
				else if(timeA[ptrA][9] == 'T'){
					ableB ++;
				}
				ptrA ++;
			}
			else if(ptrB != 2 * NB && strcmp(timeA[ptrA], timeB[ptrB]) > 0){
				//printf("A > B A = %s B = %s type = %c type = %c\n", timeA[ptrA], timeB[ptrB], timeA[ptrA][9], timeB[ptrB][9]);
				//system("pause");
				if(timeB[ptrB][9] == 'F'){
					if(ableB == 0){
						useB ++;
					}
					else if(ableB > 0){
						ableB --;
					}
				}
				else if(timeB[ptrB][9] == 'T'){
					ableA ++;
				}
				ptrB ++;
			}
			else if(strcmp(timeA[ptrA], timeB[ptrB]) == 0){
				//printf("A = B A = %s B = %s type = %c type = %c\n", timeA[ptrA], timeB[ptrB], timeA[ptrA][9], timeB[ptrB][9]);
				//system("pause");
				if(timeA[ptrA][9] == 'T'){
					ableB ++;
					ptrA ++;
				}
				else if(timeB[ptrB][9] == 'T'){
					ableA ++;
					ptrB ++;
				}
				else if(timeA[ptrA][9] == 'F'){
					if(ableA == 0){
						useA ++;
					}
					else if(ableA > 0){
						ableA --;
					}
					ptrA ++;
				}
				else if(timeB[ptrB][9] == 'F'){
					if(ableB == 0){
						useB ++;
					}
					else if(ableB > 0){
						ableB --;
					}
					ptrB ++;
				}
			}
			else{
				if(ptrA == 2 * NA){
					if(timeB[ptrB][9] == 'F'){
						if(ableB == 0){
							useB ++;
						}
						else if(ableB > 0){
							ableB --;
						}
					}
					else if(timeB[ptrB][9] == 'T'){
						ableA ++;
					}
					ptrB ++;
				}
				else if(ptrB == 2 * NB){
					if(timeA[ptrA][9] == 'F'){
						if(ableA == 0){
							useA ++;
						}
						else if(ableA > 0){
							ableA --;
						}
					}
					else if(timeA[ptrA][9] == 'T'){
						ableB ++;
					}
					ptrA ++;
				}
			}
			//printf("useA = %d useB = %d ableA = %d ableB = %d\n", useA, useB, ableA, ableB);
			//system("pause");
		}
		//printf("Case #%d: %d %d\n", n, useA, useB);
		fprintf(fout, "Case #%d: %d %d\n", n, useA, useB);
		n ++;
	}
	//system("pause");
	return 0;
}
