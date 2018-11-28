#include <cstdio>
#include <string>
using namespace std;

FILE* fin;
FILE* fout;

int L,D,N,npat[15];
char inp[500],pattern[15][26];
string dict[5000];

int main()
{
	int t,i,j,k,idx,result;
	bool ok,letok;
	
	fin = fopen ("a.in","r");
	fout = fopen ("a.out","w");
	
	fscanf(fin, "%d %d %d", &L, &D, &N);
	for(i = 0; i < D; i++)
	{
		fscanf(fin, "%s", inp);
		dict[i] = inp;
	}
	
	for(t = 1; t <= N; t++)
	{
		fscanf(fin, "%s", inp);
		idx = 0;
		for(i = 0; i < L; i++)
		{
			npat[i] = 0;
			if(inp[idx] != '(')
				pattern[i][npat[i]++] = inp[idx++];
			else
			{
				idx++;
				while(inp[idx] != ')')
					pattern[i][npat[i]++] = inp[idx++];
				idx++;
			}
			sort(pattern[i], pattern[i]+npat[i]);
		}
		
		result = 0;
		for(i = 0; i < D; i++)
		{
			ok = true;
			for(j = 0; j < L && ok; j++)
			{
				letok = false;
				for(k = 0; k < npat[j] && pattern[j][k] <= dict[i][j] && !letok; k++)
					if(dict[i][j] == pattern[j][k])
						letok = true;
				if(!letok)
					ok = false;
			}
			if(ok)
				result++;
		}
		fprintf(fout, "Case #%d: %d\n", t, result);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
