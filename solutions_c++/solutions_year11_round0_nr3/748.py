#include <fstream.h>
#define FAIL -1
#define DONE -2
using namespace std;

int main()
{
	int T, N;
	long long sum, min, read, xorsum;

	fstream fin("candy.txt",ios::in);
	FILE *fout = fopen("candy_out.txt","w");

	fin >> T;
	for (int t=0; t<T; t++)
	{
		xorsum = sum = 0;
		min = 10000000;
		fin >> N;
		for (int n = 0; n < N; n++)
		{
			fin >> read;
			if (read < min)
				min = read;
			sum += read;
			xorsum = xorsum ^ read;
		}
		sum -= min;
		if (0 == xorsum)
			fprintf(fout, "Case #%d: %lld\n", t + 1, sum);
		else
			fprintf(fout, "Case #%d: NO\n", t + 1);
	}

	fin.close();
	fclose(fout);

	return 0;
}
