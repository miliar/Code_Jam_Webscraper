#include<stdio.h>
#include<math.h>

int getLen(int number)
{
	for(int h=1; h<8; h++)
		if((number / (int)pow(10, h)) == 0)
			return h;
}

int recycle(int number)
{
	if(number < 10)
		return number;

	int size=1;
	do
	{
		int first=number % (int)pow(10, size);
		if(first > 0)
		{
			number=(number-first) / (int)pow(10, size);
			return 	((int)pow(10, getLen(number)) * first + number);
		}
		size++;
	}while(size<getLen(number));
	return number;
}

int main()
{
	int count, a, b, n, m, total;
	int h;

	FILE *fin=fopen("input.txt", "r");
	FILE *fout=fopen("output.txt", "w");

	fscanf(fin, "%d\n", &count);
	
	for(h=0; h<count; h++)
	{
		total=0;
		fscanf(fin, "%d %d\n", &a, &b);

		for(n=a; n<=b; n++)
		{
			m=recycle(n);
			while(m!=n)
			{
				if(a<=m && b>=m  && n<m)
					total++;
				m=recycle(m);
			}
		}

		fprintf(fout, "Case #%d: %d\n",h+1, total);
		printf("Case #%d: %d\n",h+1, total);
	}

	fclose(fin);
	fclose(fout);
}
