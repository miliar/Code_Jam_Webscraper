#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void swap(char *a, char *b)
{
	char temp;
	temp = *a;
	*a = *b;
	*b = temp;
}

int main(int argc, char* argv[])
{
	FILE *f;
	int many;
	int A[50], B[50];
	char n_to_str[10];
	char pieceofn[10];
	int copy_str;
	int chk;
	int result[50]={0,};
	//int iwanttoshow[50][1000];
	//int ind[50]={0,};
	//bool samenumchk[200][1000] = {false, };
	//int xindex = 0, yindex = 0;

	f = fopen("input.txt", "r");
	
	fscanf(f, "%d\n", &many);
	for(int i=0; i<many; i++)
	{
		fscanf(f, "%d", &A[i]);
		fscanf(f, "%d", &B[i]);
	}

	for(int i=0; i<many; i++)
		printf("%d %d\n", A[i], B[i]);

	for(int i=0; i<many; i++)
	{
		for(int n=A[i]; n<=B[i]; n++)
		{
			itoa(n, n_to_str, 10);

 			for(int qwer=1; qwer<strlen(n_to_str); qwer++)
			{
				for(int cat=1; cat<=qwer; cat++)
				{
					pieceofn[cat-1]=n_to_str[strlen(n_to_str)-cat];
				}
				pieceofn[qwer] = NULL;

				for(int z=0; z<strlen(pieceofn)/2; z++)
					swap(&pieceofn[z], &pieceofn[strlen(pieceofn)-(z+1)]);

				copy_str = atoi(n_to_str);
				n_to_str[strlen(n_to_str)-qwer] = NULL;

				strcat(pieceofn, n_to_str);
				chk = atoi(pieceofn);

				if(chk <= B[i] && chk>n)//&& !samenumchk[chk/1000][chk%1000])
				{
					result[i]++;
					//iwanttoshow[i][ind[i]++] = n;
					//samenumchk[chk/1000][chk%1000] = true;
				}

				itoa(copy_str, n_to_str, 10);
			}
		}
	}

	fclose(f);

	//for(int i=0; i<many; i++)
	//	printf("%d\n", result[i]);

	//for(int i=0; i<ind[3]; i++)
	//	printf("%d %d\n", iwanttoshow[3][i], i+1);

	FILE *f2;
	f2 = fopen("output.txt", "w");

	for(int i=0; i<many; i++)
		fprintf(f2, "Case #%d: %d\n", i+1, result[i]);

	fclose(f2);

	return 0;
}