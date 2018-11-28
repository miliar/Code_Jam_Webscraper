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

			// �׷� �ڸ���
			i = 0;
			tmpToken = strtok(buf, " ");
			while(tmpToken != NULL)
			{
				groups[i] = atoi(tmpToken);
				tmpToken = strtok(NULL, " ");
				i++;
			}

			// �ѷ��ڽ��� Ƚ�� ��ŭ �ݺ�
			for(i=0; i<inputValue[0]; i++)
			{
				k = 0;
				riders = 0;
				isFull = false;

				// �׷�� ��ŭ �ݺ�
				for(j=0; j<inputValue[2]; j++)
				{
					// ���� �ο� üũ
					if(riders + groups[j] <= inputValue[1] && !isFull)
					{
						// ž��
						riders += groups[j];
					}
					// ���� ž���� �غ�
					else
					{
						// ž�� ����
						isFull = true;
					}

					if(isFull)
					{
						newGroups[k] = groups[j];
						k++;
					}					
				}

				// �� �ݾ� ����
				totalEuro += riders;

				// ž���� �ٽ� ž��
				for(j=0; j<inputValue[2]; j++)
				{
					newGroups[k] = groups[j];
					k++;
				}

				// ž�� �غ�
				for(j=0; j<inputValue[2]; j++)
				{
					groups[j] = newGroups[j];
				}
			}

			fprintf(output, "Case #%d: %d\n", caseCount++, totalEuro);
		}

		// �ʱ�ȭ
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