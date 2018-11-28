#include <cstdio>
#include <iostream>
using namespace std;
int main()
{
	int Z, i, li,j, wynik, row[4][2], kol[4][2], diag[2][2];
	string t[4];
	scanf("%d", &Z);
	for(li = 1; li <= Z; li++)
	{
		for(i = 0; i < 4; i++) row[i][0] = row[i][1] = kol[i][0] = kol[i][1] = 0;
		diag[0][0] = diag[0][1] = diag[1][0] = diag[1][1] = 0;
		for(i = 0; i < 4; i++) cin >> t[i];
		for(i = 0; i < 4; i++)
		{
			for(j = 0; j < 4; j++) 
			{
				if(t[i][j] == 'O' || t[i][j] == 'T') row[i][0]++;
				if(t[i][j] == 'X' || t[i][j] == 'T') row[i][1]++;
				if(t[j][i] == 'O' || t[j][i] == 'T') kol[i][0]++;
				if(t[j][i] == 'X' || t[j][i] == 'T') kol[i][1]++;
			}
			if(t[i][i] == 'O' || t[i][i] == 'T') diag[0][0]++;
			if(t[i][i] == 'X' || t[i][i] == 'T') diag[0][1]++;
			if(t[3 - i][i] == 'O' || t[3 - i][i] == 'T') diag[1][0]++;
			if(t[3 - i][i] == 'X' || t[3 - i][i] == 'T') diag[1][1]++;
		}
		wynik = 0;
		
		for(i = 0; i < 4; i++) if(row[i][0] == 4 || kol[i][0] == 4) wynik = 1;
		if(diag[0][0] == 4 || diag[1][0] == 4) wynik = 1;
		
		for(i = 0; i < 4; i++) if(row[i][1] == 4 || kol[i][1] == 4) wynik = 2;
		if(diag[0][1] == 4 || diag[1][1] == 4) wynik = 2;
		
		if(wynik == 1) printf("Case #%d: O won\n", li);
		else if(wynik == 2) printf("Case #%d: X won\n", li);
		else 
		{
			wynik = 0;
			for(i = 0; i < 3; i++)
				for(j = 0; j < 3; j++)
					if(t[i][j] == '.') wynik = 1;
			if(wynik) printf("Case #%d: Game has not completed\n", li);
			else printf("Case #%d: Draw\n", li);
		}
	}
	return 0;
}
