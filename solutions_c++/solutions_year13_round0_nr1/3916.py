#include <cstdio>
#include<algorithm>

using namespace std;

FILE *fout;
FILE *fin;

struct Tot
{
	int nbX;
	int nbO;
	int nbT;
};

void trouveSol(int curT)
{
	Tot lignes[4];
	Tot cols[4];
	Tot diag[2];
	char carac;
	bool pasFini = false;
	for(int curI = 0; curI < 4; curI++)
	{
		lignes[curI].nbX = 0;
		lignes[curI].nbO = 0;
		lignes[curI].nbT = 0;
		cols[curI].nbX = 0;
		cols[curI].nbO = 0;
		cols[curI].nbT = 0;
		diag[curI % 2].nbX = 0;
		diag[curI % 2].nbO = 0;
		diag[curI % 2].nbT = 0;
	}

	for(int curL = 0; curL < 4; curL++)
	{
		fscanf(fin, "%c", &carac);
		//fprintf(fout, "\n");
		for(int curC = 0; curC < 4; curC++)
		{
			fscanf(fin, "%c", &carac);
			//fprintf(fout, "%c", carac);
			if(carac == 'X')
			{
				lignes[curL].nbX++;
				cols[curC].nbX++;
				if(curL == curC)
					diag[0].nbX++;
				if(curL + curC == 3)
					diag[1].nbX++;
			}
			if(carac == 'O')
			{
				lignes[curL].nbO++;
				cols[curC].nbO++;
				if(curL == curC)
					diag[0].nbO++;
				if(curL + curC == 3)
					diag[1].nbO++;
			}
			if(carac == 'T')
			{
				lignes[curL].nbT++;
				cols[curC].nbT++;
				if(curL == curC)
					diag[0].nbT++;
				if(curL + curC == 3)
					diag[1].nbT++;
			}
			if(carac == '.')
				pasFini = true;
		}
	}

	for(int curL = 0; curL < 4; curL++)
	{
		if(lignes[curL].nbX + lignes[curL].nbT == 4)
		{
			fprintf(fout, "Case #%d: X won\n", curT);
			return;
		}
		if(lignes[curL].nbO + lignes[curL].nbT == 4)
		{
			fprintf(fout, "Case #%d: O won\n", curT);
			return;
		}
	}
	for(int curC = 0; curC < 4; curC++)
	{
		if(cols[curC].nbX + cols[curC].nbT == 4)
		{
			fprintf(fout, "Case #%d: X won\n", curT);
			return;
		}
		if(cols[curC].nbO + cols[curC].nbT == 4)
		{
			fprintf(fout, "Case #%d: O won\n", curT);
			return;
		}
	}
	for(int curD = 0; curD < 2; curD++)
	{
		//printf(fout, "curD : %d\nnbX : %d et nbO : %d et nbT : %d\n\n", curD, diag[curD].nbX, diag[curD].nbO, diag[curD].nbT);
		if(diag[curD].nbX + diag[curD].nbT == 4)
		{
			fprintf(fout, "Case #%d: X won\n", curT);
			return;
		}
		if(diag[curD].nbO + diag[curD].nbT == 4)
		{
			fprintf(fout, "Case #%d: O won\n", curT);
			return;
		}
	}
	if(pasFini)
		fprintf(fout, "Case #%d: Game has not completed\n", curT);
	else
		fprintf(fout, "Case #%d: Draw\n", curT);
}

int main()
{
	fin = fopen ("A-Small.in", "r");
	fout = fopen ("A-Small.out", "w");

	int nbTests;
	char carac;
	fscanf(fin, "%d", &nbTests);
	for(int curT = 1; curT <= nbTests; curT++)
	{
		trouveSol(curT);
		fscanf(fin, "%c", &carac);
	}
    return 0;
}
