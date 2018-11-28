#include <cstdio>
#include <map>
#include <algorithm>
#include <string>
#include <vector>
#include <ctime>
#include <cmath>
#include <iostream>
#include <utility>

using namespace std;

int main (){

	FILE *fin = fopen ("A-large.in", "r");
	FILE *fout = fopen ("OutSquareTilesLarge.out", "w+");
    int n, r, c;
	fscanf (fin, "%d\n", &n);
    char field[52][52];
	for (int k = 0; k < n; k++){
        printf ("%d\n", k);
        fscanf (fin, "%d %d\n", &r, &c);
        for (int i = 0; i < r; i++){
            for (int j = 0; j < c; j++){
                fscanf (fin, "%c", &field[i][j]);
            }
            fscanf (fin, "\n");
        }
        int impossible = 0;
        for (int i = 0; i < r; i++){
            for (int j = 0; j < c; j++){
                if (field[i][j] == '#'){
                    if (field[i+1][j] != '#' || field[i+1][j+1] != '#' || field[i][j+1] != '#' || i+1 >= r || j+1 >= c){
                        impossible = 1;
                        break;
                    }
                    field[i][j] = '/';
                    field[i+1][j] = '\\';
                    field[i+1][j+1] = '/';
                    field[i][j+1] = '\\';
                }
            }
            if (impossible != 0) break;
        }
        fprintf (fout, "Case #%d:\n", k+1);
        if (impossible != 0) fprintf (fout, "Impossible\n");
        else {
            for (int i = 0; i < r; i++){
                for (int j = 0; j < c; j++){
                    fprintf (fout, "%c", field[i][j]);
                }
                fprintf (fout, "\n");
            }
        }
	}
    fclose(fin);
    fclose(fout);
	system ("PAUSE");
	return 0;
}
