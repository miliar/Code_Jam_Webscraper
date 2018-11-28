#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
	int t = 0;

	FILE *fin;
	FILE *fout;

	fin = fopen("C-large.in", "r");
	//	fin = fopen("C-small-sample.in", "r");
	fout = fopen("C-output.out", "w");

	fscanf(fin, "%d ", &t);

	int n, m;
	char cn[10], cm[10];
	int count = 0;
	int pow[8] = {0, 1, 10, 100, 1000, 10000, 100000, 1000000};
	int storage[10000] = {0};
	int n_storage = 0;
	int temp = 0;
	int last = 0;


	for(int cycle = 0; cycle<t; cycle++)
	{		
		count = 0;

		fscanf(fin, "%s %s", cn, cm);
		
		n = atoi(cn);
		m = atoi(cm);

		int digit = strlen(cn);

		for(int i=n; i<=m; i++)
		{
			temp = i;
			last = 0;
			n_storage = 0;

			for(int j=1; j<digit; j++)
			{
				last = temp % 10;
				temp = temp / 10;
				temp = temp + last * pow[digit];
				//	printf("%d ", temp);

				bool flag = true;

				if(temp > i && temp <= m)
				{
					int temp2 = temp;
					int fix_last = temp2 % 10;
					
					flag = false;
					/*
					// 같은 수로 이루어져 있는지 검사
					while(temp2 >= 1)
					{
						if(temp2 % 10 != fix_last)
						{
							flag = false;
							break;
						}
						temp2 /= 10;
					}
					*/
				}


				if(flag == false)
				{
					bool flag2 = false;
					for(int k=0; k<n_storage; k++)
					{
						if(temp == storage[k])
						{
							flag2 = true;
							printf("! %d at %d\n", temp, k);
						}
					}

					if(flag2 == false)
					{
						storage[n_storage] = temp;
						n_storage++;
						count++;
					}
				}
			}
		}
		//	printf("Case #%d: %d\n", cycle+1, count);

		/*
		printf("\nStarage >\n");
		for(int j=0; j<n_storage; j++)
		{
			printf("%d ", storage[j]);
		}
		*/


		fprintf(fout, "Case #%d: %d\n", cycle+1, count);
	}	// end of cycle

	fclose(fin);
	fclose(fout);
}