#include <iostream>
using namespace std;

int main()
{
	FILE *fpin, *fpout;
	fpin = fopen("input.txt", "r");
	if (fpin == NULL)
	{
		cout<<"Err desc fis in";
		return -1;
	}
	fpout = fopen("output.txt", "w");
	if (fpout == NULL)
	{
		cout<<"Err desc fis de iesire";
		return -2;
	}
	int T;
	fscanf(fpin, "%d", &T);
	int nt = 0;
	int a, b;
	int n, m;
	int contor;
	char numar[30], numAux[20];
	int i, j, cat, nrCN;
	int copii[30];
	int contP = 0, c;
	for (nt = 0; nt < T; nt++)
	{
		fscanf(fpin, "%d %d", &a, &b);
		n = a;//corect
		contor = 0;
		while (n < b)
		{
			cat = n;
			i = 0;
			while (cat > 0)
			{
				numar[i] = '0' + cat%10;
				cat = cat/10;
				i++;
			}
			numar[i] = '\0';
			nrCN = i;
			int aux;
			for (j = 0; j < nrCN/2; j++)
			{
				aux = numar[j];
				numar[j] = numar[i - 1 - j];
				numar[i - 1 - j] = aux;
			}
			m = atoi(numar);
			j = nrCN - 1;
			c = 0;
			while (j > 0)
			{
				if (numar[j] == '0')
				{
					j--;
					continue;
				}
				int l = 0;
				int k = j;
				while (k < nrCN)
				{
					numAux[l] = numar[k];
					k++;
					l++;
				}
				k = 0;
				while (l < nrCN)
				{
					numAux[l] = numar[k];
					k++;
					l++;
				}
				numAux[nrCN] = '\0';
				m = atoi(numAux);
				int ok = 1;
				if (m > atoi(numar) && m <= b) 
				{
					c = 0;
					while (c < contP)
					{
						if (copii[c] == m) ok = 0;
						c++;
					}
					if (ok)
					{
						copii[contP] = m;
						contP++;
						contor++;
					}
				}
				j--;
			}
			contP = 0;
			n++;
		}
		fprintf(fpout, "Case #%d: %d\n", nt + 1, contor);
	}
	
	fclose(fpin);
	fclose(fpout);

	return 0;
}