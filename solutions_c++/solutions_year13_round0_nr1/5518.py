#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <array>
#include <ctype.h>
#include <vector>
using namespace std;
const int  XXXX = 352;
const int  OOOO = 316;
const int  T3X = 348;
const int  T3O = 321;




string check4x4(int sum)
{
	if(sum == XXXX || sum == T3X) return "X won";
	else if(sum == OOOO || sum == T3O) return "O won";
	else return "";

}


int main(void)
{		
	FILE * fi = fopen("A-small-attempt0.in","r");
	FILE * fo = fopen("A-small-attempt0.out","w");

	//fscanf(fi, "%d", &N);
	char line[4];
	int N = atoi(fgets(line,4,fi));
	//fgets(line,2,fi);
	for(int i = 0; i < N; i++)
	{
		char game[4][5];
		for(int i1 = 0; i1 < 4; i1++)
		{			
			fgets(game[i1], sizeof(game[i1]), fi); fgets(line,2,fi);						
		}
		fgets(line,2,fi);	
		int totalRow = 0, totalCol = 0, diagonal1 = 0, diagonal2 = 0;
		bool isFound = false;
		bool hasEmpty = false;
		for (int i2 = 0; i2 < 4 ; i2++) 
		{
			for(int i3 =0; i3 < 4 ; i3++) {
				
				totalRow +=  game[i2][i3]; 
				totalCol +=  game[i3][i2]; 
				
				if(i2 == i3) diagonal1 += game[i2][i3];
				if((i2 + i3) == 3) diagonal2 += game[i2][i3];

				if((game[i2][i3]) == '.') hasEmpty = true;
				
			}
			string result = check4x4(totalRow).append(check4x4(totalCol ));
			if(result != "") {
				isFound = true;
				fprintf(fo, "Case #%d: %s\n", i + 1, result.c_str());		
				break;
			}
			totalRow = 0, totalCol = 0;
				
		}
		
		if(isFound) continue;
		
		string  result = check4x4(diagonal1).append(check4x4(diagonal2));
		
		if(result != "") {
			fprintf(fo, "Case #%d: %s\n", i + 1, result.c_str());	
			continue;
		}
		
		fprintf(fo, "Case #%d: %s\n", i + 1, hasEmpty ? "Game has not completed" : "Draw");				
	}

	fclose(fi);
	fclose(fo);
	return 0;
}
