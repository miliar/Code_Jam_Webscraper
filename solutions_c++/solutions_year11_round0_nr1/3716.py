#include <iostream>

const int NMAX = 10000;

FILE *f = fopen("bot.in", "r");
FILE *g = fopen("bot.out", "w");

int T = 0, N = 0, n;
int pozB = 1, pozO = 1, vpozB = 1, vpozO = 1, pozBvector = -1, pozOvector = -1;
char *sir;
int *nr;
int contor;
int rezultat = 0;


int editSir(const char* sir)
{
	int n = strlen(sir);
	int k = 0;
	for (int i = 2; i < n; ++i)
	{
		if ((sir[i] >= '0') && (sir[i] <= '9'))
		{
			int m = 0;
			while ((sir[i] >= '0') && (sir[i] <= '9'))
			{
				m = m * 10 + sir[i] - '0';
				i++;
			}
			nr[k++] = m;
		}
		if (sir[i] == 'B')
		{
			nr[k++] = -1;
		}
		if (sir[i] == 'O')
		{
			nr[k++] = -2;
		}
	}

	return k;
}

int getNextPozB(int* poz, int n)
{
	for (int i = *poz + 1; i < n; ++i)
		if (nr[i] == -1) 
		{
			*poz = i + 1;
			return nr[i + 1];
		}
	return -1; //ERROR
}

int getNextPozO(int* poz, int n)
{
	for (int i = *poz + 1; i < n; ++i)
		if (nr[i] == -2) 
		{
			*poz = i + 1;
			return nr[i + 1];
		}
	return -1; //ERROR
}

int seeFirst(int *poz, int n)
{
	for (int i = *poz; i < n; ++i)
	{
		if (nr[i] == -1)
		{
			*poz = i + 1;
			return 1;
		}
		if (nr [i] == -2)
		{
			*poz = i + 1;
			return 2;
		}
	}
	return -1; //nu ar trebui sa se intample niciodata
}


int main()
{
	fscanf(f, "%d\n", &T);

	for (int t = 0; t < T; ++t)
	{
		sir = new char[NMAX];
		nr = new int[NMAX];
		fgets(sir, NMAX, f);
		N = sir[0] - '0';
		n = editSir(sir);
		pozB = 1; //pozitia pe care se afla B
		pozO = 1;
		vpozB = 1; //viitoarea pozitie pe care se afla B
		vpozO = 1;
		pozBvector = -1; //pozitia pe care se afla B in vector
		pozOvector = -1;
		//viitoarea pozitie a lui B
		vpozB = getNextPozB(&pozBvector, n);
		//viitoarea pozitie a lui O
		vpozO = getNextPozO(&pozOvector, n);
		contor = 0;
		rezultat = 0;
		while ((vpozB != -1) || (vpozO != -1))
		{
			int p = seeFirst(&contor, n);
			if (p == 1) //trebuie sa apese B
			{
				rezultat = rezultat + abs(vpozB - pozB); // l-am pus pe B pe butonul care trebuie
				rezultat++; // apasa butonul
				//incercam sa-l pozitionam cat mai bine pe O
				if (vpozO != -1)
				{
					if (abs(vpozO - pozO) <= (abs(vpozB - pozB) + 1))
					{
						pozO = vpozO;
					}
					else
					{
						if (pozO < vpozO)
						{
							pozO = pozO + abs(vpozB - pozB) + 1;
						}
						else
						{
							pozO = pozO - abs(vpozB - pozB) - 1;
						}
					}
				}
				pozB = vpozB;
				vpozB = getNextPozB(&pozBvector, n);
			}

			if (p == 2)
			{
				rezultat = rezultat + abs(vpozO - pozO); // l-am pus pe O pe butonul care trebuie
				rezultat++; // apasa butonul
				//incercam sa-l pozitionam cat mai bine pe B
				if (vpozB != -1)
				{
					if (abs(vpozB - pozB) <= (abs(vpozO - pozO) + 1))
					{
						pozB = vpozB;
					}
					else
					{
						if (pozB < vpozB)
						{
							pozB = pozB + abs(vpozO - pozO) + 1;
						}
						else
						{
							pozB = pozB - abs(vpozO - pozO) - 1;
						}
					}
				}
				pozO = vpozO;
				vpozO = getNextPozO(&pozOvector, n);
			}
		}

		fprintf(g, "Case #%d: %d\n", t + 1, rezultat); 

		delete[] sir;
		delete[] nr;
	}

	return 0;
}