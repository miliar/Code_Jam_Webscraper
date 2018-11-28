#include <stdio.h>
#include <stdlib.h>
#include <string.h>
const int MAX = 1024;


int main()
{
	FILE *fread = fopen("H:\\C-small-attempt0.in", "r");
	FILE *fwrite = fopen("H:\\C-small-attempt0.out", "w");

	int TestCase, firstLoop, secondLoop, thirdLoop;
	int *min_range, *max_range;
	char buffer[MAX], result[MAX];
	char *num;
	int temp;
	char ch;	//로테이션을 위한 템프 
	char *token;
	int i, count;

	fgets(buffer, MAX, fread);
	TestCase = atoi(buffer);
	min_range = (int*)malloc(TestCase*sizeof(int)); 
	max_range = (int*)malloc(TestCase*sizeof(int));


	
	for(firstLoop = 0; firstLoop < TestCase; firstLoop++){
		
		count = 0;
		/* 읽어들어온 파일의 토큰을 잘라 min 과 max 범위 생성 */
		fgets(buffer, MAX, fread);
		token = strtok(buffer, " ");
		min_range[firstLoop] = atoi(token);
		printf("min_range%d : %d \n",firstLoop, min_range[firstLoop]);
		token = strtok(NULL, " ");	

		if(token != NULL)
			max_range[firstLoop] = atoi(token);


		/* 범위 조정 끝										*/

		num = (char *)malloc(sizeof(char)*(max_range[firstLoop] - min_range[firstLoop] + 1));
		//num = (char *)realloc(num, sizeof(char)*(max_range[firstLoop] - min_range[firstLoop] + 1));

	
		for(secondLoop = min_range[firstLoop] ; secondLoop < max_range[firstLoop] ; secondLoop++)
		{	
				temp = secondLoop;
				_itoa(secondLoop, num, 10);				// 정수를 character 값으로 변환

				for(thirdLoop = 0; thirdLoop < strlen(num); thirdLoop++)
				{
					
					/* Rotatition */
					ch = num[0];

					for(i = 0; i < strlen(num)-1; i++){
							num[i] = num[i+1];
					}
					num[strlen(num)-1] = ch;
					/*		       */

					temp = atoi(num);
	
					if(temp > secondLoop && temp <= max_range[firstLoop] && temp >= min_range[firstLoop])
					{
						
						count++;
					}

				}
		}
		printf("Case #%d: %d\n", firstLoop+1, count);
		sprintf(result, "Case #%d: %d\n", firstLoop+1, count);
		fputs(result, fwrite);
	}
	


}