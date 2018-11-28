#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
	int max = -1;

	char *tmpToken;

	int inputValue[3] = {0}; // R, K, N
	int groups[100] = {0};
	int newGroups[100] = {0};

	int riders = 0;
	int totalEuro = 0;

	int caseCount = 1;

	char buf[100];

	int i = 0;
	int j = 0;
	int k = 0;

	bool isFull = false;

	FILE *input;
	if((input = fopen("C-small-attempt1.in", "rt")) == NULL)
	{
		return -1;
	}

	FILE *output;
	if((output = fopen("output.txt", "w")) == NULL)
	{
		return -1;
	}

	do
	{
		if(max < 0)
		{
			fgets(buf, 10, input);
			max = atoi(buf);

			if(max < 0 || max > 50)
				max = -1;
		}
		else
		{
			totalEuro = 0;

			// R, K, N
			fgets(buf, 100, input);

			i = 0;
			tmpToken = strtok(buf, " ");
			while(tmpToken != NULL)
			{
				inputValue[i] = atoi(tmpToken);

				tmpToken = strtok(NULL, " ");
				i++;
			}

			// group
			fgets(buf, 100, input);

			// 그룹 자르기
			i = 0;
			tmpToken = strtok(buf, " ");
			while(tmpToken != NULL)
			{
				groups[i] = atoi(tmpToken);
				tmpToken = strtok(NULL, " ");
				i++;
			}

			// 롤러코스터 횟수 만큼 반복
			for(i=0; i<inputValue[0]; i++)
			{
				k = 0;
				riders = 0;
				isFull = false;

				// 그룹수 만큼 반복
				for(j=0; j<inputValue[2]; j++)
				{
					// 수용 인원 체크
					if(riders + groups[j] <= inputValue[1] && !isFull)
					{
						// 탑승
						riders += groups[j];
					}
					// 다음 탑승자 준비
					else
					{
						// 탑승 종료
						isFull = true;
					}

					if(isFull)
					{
						newGroups[k] = groups[j];
						k++;
					}					
				}

				// 총 금액 누적
				totalEuro += riders;

				// 탑승자 다시 탑승
				for(j=0; j<inputValue[2]; j++)
				{
					newGroups[k] = groups[j];
					k++;
				}

				// 탑승 준비
				for(j=0; j<inputValue[2]; j++)
				{
					groups[j] = newGroups[j];
				}
			}

			fprintf(output, "Case #%d: %d\n", caseCount++, totalEuro);
		}

		// 초기화
		for(i=0; i<100; i++)
		{
			groups[i] = 0;
			newGroups[i] = 0;
		}
	}
	while(caseCount <= max);

	fclose(input);
	fclose(output);

	return 0;
}