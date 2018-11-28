#include<iostream>
#include<stdio.h>
#include<string>
using namespace std;

char str[4][5];
int rx[4], ro[4], cx[4], co[4], d1x, d1o, d2x, d2o;
bool canbedraw;
int test;
FILE *fo = fopen("output.txt","w");

string check()
{
	for(int i = 0; i < 4; i++) {
		if(rx[i] == 4 || cx[i] == 4 || d1x == 4 || d2x == 4)
			return "X won";
		else if(ro[i] == 4 || co[i] == 4 || d1o == 4 || d2o == 4)
			return "O won";
	}
	if(canbedraw)
		return "Draw";
	return "Game has not completed";
}

int main()
{
	FILE *fp = fopen("A-large.in", "r");
	fscanf(fp, "%d", &test);
	for(int t = 1; t <= test; t++) {
		canbedraw = true;
		for(int i = 0; i < 4; i++) {
			rx[i] = ro[i] = cx[i] = co[i] = 0;
		}
		d1x = d2x = d1o = d2o = 0;

		for(int i = 0; i < 4; i++) {
			fscanf(fp, "%s", str[i]);
		}

		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				if(str[i][j]=='O') ro[i]++;
				else if(str[i][j]=='X') rx[i]++;
				else if(str[i][j]=='T') { rx[i]++; ro[i]++; }
				else if(str[i][j]=='.') canbedraw = false;
			}
		}

		for(int j = 0; j < 4; j++) {
			for(int i = 0; i < 4; i++) {
				if(str[i][j]=='O') co[j]++;
				else if(str[i][j]=='X') cx[j]++;
				else if(str[i][j]=='T') { cx[j]++; co[j]++; }
			}
		}

		for(int i = 0; i < 4; i++) {
			if(str[i][i]=='O') d1o++;
			else if(str[i][i]=='X') d1x++;
			else if(str[i][i]=='T') { d1x++; d1o++; }
		}
		for(int i = 0; i < 4; i++) {
			if(str[i][3-i]=='O') d2o++;
			else if(str[i][3-i]=='X') d2x++;
			else if(str[i][3-i]=='T') { d2x++; d2o++; }
		}

		string res = check();
		if(res == "X won")
			fprintf(fo, "Case #%d: X won\n", t);
		else if(res == "O won")
			fprintf(fo, "Case #%d: O won\n", t);
		else if(res == "Draw")
			fprintf(fo, "Case #%d: Draw\n", t);
		else
			fprintf(fo, "Case #%d: Game has not completed\n", t);
	}

	fclose(fp);
	fclose(fo);
	return 0;
}