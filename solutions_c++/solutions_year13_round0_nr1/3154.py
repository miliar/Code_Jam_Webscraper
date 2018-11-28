#include<stdio.h>
#include<string.h>
#include<iostream>

using namespace std;

FILE *ptr;

int solve(int count){
	int a = 0,b = 0;
	int point = 0;
	char map[5][5];
	char mapa[5][5];
	char mapb[5][5];
	int find = 0;
	//Create Map
	for(int i=0;i<4;i++){
		cin >> map[i];
	}
	
	//Count Point & Replace
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(map[i][j] == '.') point ++;
			mapa[i][j] = map[i][j];
			mapb[i][j] = map[i][j];		
			if(map[i][j] == 'T'){
				mapa[i][j] = 'X';
				mapb[i][j] = 'O';
			}	
		}
	}
	
	//Find
	char ans = 'X';
	
	if(mapa[0][0] == mapa[0][1] && mapa[0][0] == mapa[0][2] && mapa[0][0] == mapa[0][3] && mapa[0][0] == ans) a ++;
	if(mapa[1][0] == mapa[1][1] && mapa[1][0] == mapa[1][2] && mapa[1][0] == mapa[1][3] && mapa[1][0] == ans) a ++;
	if(mapa[2][0] == mapa[2][1] && mapa[2][0] == mapa[2][2] && mapa[2][0] == mapa[2][3] && mapa[2][0] == ans) a ++;
	if(mapa[3][0] == mapa[3][1] && mapa[3][0] == mapa[3][2] && mapa[3][0] == mapa[3][3] && mapa[3][0] == ans) a ++;
	
	if(mapa[0][0] == mapa[1][0] && mapa[0][0] == mapa[2][0] && mapa[0][0] == mapa[3][0] && mapa[0][0] == ans) a ++;
	if(mapa[0][1] == mapa[1][1] && mapa[0][1] == mapa[2][1] && mapa[0][1] == mapa[3][1] && mapa[0][1] == ans) a ++;
	if(mapa[0][2] == mapa[1][2] && mapa[0][2] == mapa[2][2] && mapa[0][2] == mapa[3][2] && mapa[0][2] == ans) a ++;
	if(mapa[0][3] == mapa[1][3] && mapa[0][3] == mapa[2][3] && mapa[0][3] == mapa[3][3] && mapa[0][3] == ans) a ++;

	if(mapa[0][0] == mapa[1][1] && mapa[0][0] == mapa[2][2] && mapa[0][0] == mapa[3][3] && mapa[0][0] == ans) a ++;
	if(mapa[0][3] == mapa[1][2] && mapa[0][3] == mapa[2][1] && mapa[0][3] == mapa[3][0] && mapa[0][3] == ans) a ++;
	
	if(a > 0) a = 1;

	ans = 'O';
	
	if(mapb[0][0] == mapb[0][1] && mapb[0][0] == mapb[0][2] && mapb[0][0] == mapb[0][3] && mapb[0][0] == ans) b ++;
	if(mapb[1][0] == mapb[1][1] && mapb[1][0] == mapb[1][2] && mapb[1][0] == mapb[1][3] && mapb[1][0] == ans) b ++;
	if(mapb[2][0] == mapb[2][1] && mapb[2][0] == mapb[2][2] && mapb[2][0] == mapb[2][3] && mapb[2][0] == ans) b ++;
	if(mapb[3][0] == mapb[3][1] && mapb[3][0] == mapb[3][2] && mapb[3][0] == mapb[3][3] && mapb[3][0] == ans) b ++;
	
	if(mapb[0][0] == mapb[1][0] && mapb[0][0] == mapb[2][0] && mapb[0][0] == mapb[3][0] && mapb[0][0] == ans) b ++;
	if(mapb[0][1] == mapb[1][1] && mapb[0][1] == mapb[2][1] && mapb[0][1] == mapb[3][1] && mapb[0][1] == ans) b ++;
	if(mapb[0][2] == mapb[1][2] && mapb[0][2] == mapb[2][2] && mapb[0][2] == mapb[3][2] && mapb[0][2] == ans) b ++;
	if(mapb[0][3] == mapb[1][3] && mapb[0][3] == mapb[2][3] && mapb[0][3] == mapb[3][3] && mapb[0][3] == ans) b ++;

	if(mapb[0][0] == mapb[1][1] && mapb[0][0] == mapb[2][2] && mapb[0][0] == mapb[3][3] && mapb[0][0] == ans) b ++;
	if(mapb[0][3] == mapb[1][2] && mapb[0][3] == mapb[2][1] && mapb[0][3] == mapb[3][0] && mapb[0][3] == ans) b ++;
	
	if(b > 0) b = 1;

	if(a > b) cout << "Case #"<< (count) << ": X won" << endl;
	else if(a < b) cout << "Case #"<< (count) << ": O won" << endl;
	else if(a == b && point > 0) cout << "Case #"<< (count) << ": Game has not completed" << endl;
	else cout << "Case #"<< (count) << ": Draw" << endl;

	if(a > b) fprintf(ptr,"Case #%d: X won\n",count);
	else if(a < b) fprintf(ptr,"Case #%d: O won\n",count);
	else if(a == b && point > 0) fprintf(ptr,"Case #%d: Game has not completed\n",count);
	else fprintf(ptr,"Case #%d: Draw\n",count);

}

int main(){
	int n;
	cin >> n;
	ptr = fopen("ans.txt","w");
	for(int i=0;i<n;i++){
		solve(i+1);		
	}
	fclose(ptr);
	return 0;
}