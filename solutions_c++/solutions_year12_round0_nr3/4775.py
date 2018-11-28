#include <stdio.h>
#include <math.h>

int izracunaj(int A, int B)
{
	int i, j, rez = 0, temp, brZnamenki = 0, maska = 1;
	
	
	//FILE *out;
	//out = fopen("test.txt", "a");
	//if (out == NULL) {
	//	printf("Greska prilikom otvaranja izlazne datoteke!\n");
	//	return 1;
	//}


	i = A;
	while (i)
	{
		i/=10;
		maska*=10;
		brZnamenki++;
	}
	maska/=10;
	for (i = A; i <= B; i++)
	{
		temp = i;
		for (j = 1; j < brZnamenki; j++) {
			temp = temp / 10 + (temp % 10) * maska;
			//if (temp >= A && temp <= B)
			if (temp > i && temp <= B)
			{
				rez++;
				//fprintf(out, "(%i %i)\n", i, temp);
			}
		}
	}
	//fclose(out);
	return rez;
	//return rez/2;
}

int main(void)
{
	int brojZadataka = 0, i, j, A, B;
	FILE *in, *out;

	in = fopen("C-small-attempt0.in", "r");
	if (in == NULL) {
		printf("Greska prilikom otvaranja ulazne datoteke!\n");
		return 1;
	}

	out = fopen("C-small-attempt0.out", "w");
	if (out == NULL) {
		printf("Greska prilikom otvaranja izlazne datoteke!\n");
		return 1;
	}

	fscanf(in, "%d\n", &brojZadataka);

	for (i = 1; i <= brojZadataka; i++) {
		fscanf(in, "%d %d\n", &A, &B);
		fprintf(out, "Case #%i: %i\r\n", i, izracunaj(A, B));
	}

	fclose(in);
	fclose(out);

	return 0;
}
