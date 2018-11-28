#include <stdio.h>
#include <math.h>

FILE *fin, *fout;


double one, poww;

int main()
{
	int T, test, result[31], n, i;
	fin = fopen("date.in", "rt");
	fout = fopen("date.out", "wt");

	fscanf(fin, "%d", &T);

	/*calculated at: 
	http://count.ucsc.edu/~bauerle/scientif.htm
	thanks
	*/
	result[2] = 27;
	result[3] = 143;
	result[4] = 751;
	result[5] = 935;
	result[6] = 607;
	result[7] = 903;
	result[8] = 991;
	result[9] = 335;
	result[10] = 47;
	result[11] = 943;
	result[12] = 471;
	result[13] = 55;
	result[14] = 447;
	result[15] = 463;
	result[16] = 991;
	result[17] = 95;
	result[18] = 607;
	result[19] = 263;
	result[20] = 151;
	result[21] = 855;
	result[22] = 527;
	result[23] = 743;
	result[24] = 351;
	result[25] = 135;
	result[26] = 407;
	result[27] = 903;
	result[28] = 791;
	result[29] = 135;
	result[30] = 647;



	for (test = 1; test <= T; test++)
	{
		fscanf(fin, "%d", &n);

		/*one = sqrt(5) + 3;

		poww = one;

		for (i = 0; i < n-1; i++)
		{
			poww = poww * one;

			while (poww > 1000)
				poww -= 1000;
		}

		result = (int)(poww*10);
		result /= 10;	
*/
		fprintf(fout, "Case #%d: ", test);

		if (result[n] < 100)
			fprintf(fout, "0");

		if (result[n] < 10)
			fprintf(fout, "0");

		fprintf(fout, "%d\n", result[n]);
	}


	fclose(fin);
	fclose(fout);

	return 0;
}
