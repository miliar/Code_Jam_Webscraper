#include <fstream.h>
using namespace std;


int main()
{
	int T, N, read, cnt;

	fstream fin("goro.txt",ios::in);
	FILE *fout = fopen("goro_out.txt","w");

	fin >> T;
	for (int t=0; t<T; t++)
	{
		fin >> N;
		cnt = 0;
		for (int n = 1; n < N + 1; n++)
		{
			fin >> read;
			if (read != n)
			        cnt++;
		}

		fprintf(fout, "Case #%d: %d.000000\n", t + 1, cnt);
	}

	fin.close();
	fclose(fout);

	return 0;
}
