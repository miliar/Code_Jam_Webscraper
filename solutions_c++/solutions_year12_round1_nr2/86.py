#pragma disable warning(4996)

#include<stdio.h>

int a[2000];
int b[2000];
int c[2000];

int main()
{
	int T;

	FILE* fin = fopen("input.txt", "r");
	FILE* fout = fopen("output.txt","w");

	fscanf(fin, "%d\n", &T);

	for(int i = 1; i <= T; i++)
	{
		int N;
		fscanf(fin, "%d", &N);

		for(int j = 0; j < N; j++)
		{
			fscanf(fin, "%d%d", a+j, b+j);
			c[j] = 0;
		}
		int star = 0;

		for(int j = 1;; j++)
		{
			// 1�ܰ�: 0->2�� 1->2 �� �Ǹ� ������ �Ѵ�.
			for(int k = 0; k < N; k++)
			{
				if(c[k] < 2 && b[k] <= star)
				{
					star += 2-c[k];
					c[k] = 2;
					goto good;
				}
			}
			// 2�ܰ�: 1�ܰ谡 �Ұ����ϸ� 0->1�� �Ǵ°� �� 2��Ÿ �䱸������ ���� ū���� �Ѵ�.
			int max = -1;
			int maxp = -1;
			int p = 0;
			for(; p < N; p++)
			{
				if(c[p] == 0 && a[p] <= star && b[p] > max)
				{
					max = b[p];
					maxp = p;
				}
			}
			if(maxp == -1) goto hell; // �ƹ��͵� ���ϸ� Too Bad
			c[maxp] = 1;
			star++;
good:
			if(star == 2 * N)
			{
				fprintf(fout,"Case #%d: %d\n", i, j);
				break;
			}
		}
		continue;
hell:
		fprintf(fout,"Case #%d: Too Bad\n", i);
	}
	return 0;
}
