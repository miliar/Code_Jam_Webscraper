#pragma hdrstop
#pragma argsused

#include <tchar.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include "iostream.h"

int ler (FILE *fp);

int _tmain(int argc, _TCHAR* argv[])
{
	int iQtdTotal;
	char cTemp[5];	//le a qtd
	char l[4][6], lb[6];	//linhas de 1 a 4 + espaco em branco
	char cSaida[20];
	FILE *fpIn, *fpOut;

   	fpIn = fopen("sample.in", "r");
   	fpOut = fopen("sample.out", "w");

	if (fpIn == NULL)
	{
		std::cout << "Erro ao ler arquivo de entrada!";
		system("pause");
		return 0;
	}
	if (fpOut == NULL)
	{
		cout << "Erro ao ler arquivo de saida!";
 		system("pause");
		return 0;
	}

	fgets(cTemp, 20000, fpIn);
	iQtdTotal = strtoul(cTemp, NULL, 10);

	cout << "Qtd Total: " << iQtdTotal << "\n" << endl;

	//--le caso a caso--//
	for (int i=0; i < iQtdTotal; i++)
	{
		bool bResult = false;
		fgets(l[0], 6, fpIn);
		fgets(l[1], 6, fpIn);
		fgets(l[2], 6, fpIn);
		fgets(l[3], 6, fpIn);
		fgets(lb, 6, fpIn);

		for (int z=0; z < 2; z++)
		{
			char cComp;

			//--verifica se X ganhou--//
			if (z == 0) cComp = 'X';
			//--verifica se O ganhou--//
			else cComp = 'O';

			//horizontal
			int cont1=0, cont2=0, cont3=0, cont4=0;
			for (int j=0; j < 4; j++)
			{
				if (l[0][j] == 'T' || l[0][j]==cComp) cont1++;
				if (l[1][j] == 'T' || l[1][j]==cComp) cont2++;
				if (l[2][j] == 'T' || l[2][j]==cComp) cont3++;
				if (l[3][j] == 'T' || l[3][j]==cComp) cont4++;
			}
			if (cont1 == 4 || cont2 == 4 || cont3 == 4 || cont4 == 4)
			{
				sprintf(cSaida, "Case #%d: %c won\n", i+1, cComp);
				bResult = true;
				break;
			}
			//vertical
			cont1=0; cont2=0; cont3=0; cont4=0;
			for (int j=0; j < 4; j++)
			{
				if (l[j][0] == 'T' || l[j][0]==cComp) cont1++;
				if (l[j][1] == 'T' || l[j][1]==cComp) cont2++;
				if (l[j][2] == 'T' || l[j][2]==cComp) cont3++;
				if (l[j][3] == 'T' || l[j][3]==cComp) cont4++;
			}
			if (cont1 == 4 || cont2 == 4 || cont3 == 4 || cont4 == 4)
			{
				sprintf(cSaida, "Case #%d: %c won\n", i+1, cComp);
				bResult = true;
				break;
			}
			//diagonais
			if ((l[0][0] == 'T' || l[0][0]==cComp) &&
				(l[1][1] == 'T' || l[1][1]==cComp) &&
				(l[2][2] == 'T' || l[2][2]==cComp) &&
				(l[3][3] == 'T' || l[3][3]==cComp))
			{
				sprintf(cSaida, "Case #%d: %c won\n", i+1, cComp);
				bResult = true;
				break;
			}
			if ((l[3][0] == 'T' || l[3][0]==cComp) &&
				(l[2][1] == 'T' || l[2][1]==cComp) &&
				(l[1][2] == 'T' || l[1][2]==cComp) &&
				(l[0][3] == 'T' || l[0][3]==cComp))
			{
				sprintf(cSaida, "Case #%d: %c won\n", i+1, cComp);
				bResult = true;
				break;
			}
		}
		if (!bResult)
		{
			//--verifica se jogo nao terminou ou se deu empate--//
			int contPontinhos = 0;
			for (int k = 0; k < 4; k++)
			{
				for (int m = 0; m < 4; m++)
				{
					if (l[k][m] == '.') contPontinhos++;
				}
			}
			if (contPontinhos > 0)
			{
				sprintf(cSaida, "Case #%d: Game has not completed\n", i+1);
			}
			else {
				sprintf(cSaida, "Case #%d: Draw\n", i+1);
			}
		}
		fputs(cSaida, fpOut);
	}

	fcloseall();
	return 0;
}
