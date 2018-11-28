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

	FILE *fin = fopen("C-small-attempt0.in", "r");
	FILE *fout = fopen("C-small-attempt0.out", "w");
    int T, R, k, N;
	fscanf (fin, "%d\n", &T);

	for (int i = 1; i <= T; i++){
	    fscanf (fin, "%d %d %d\n", &R, &k, &N);
	    int matrix[1010];
	    for (int z = 1; z <= N; z++){
	        fscanf (fin, "%d", &matrix[z]);
	    }
	    int pointer = 1;
	    int money = 0;
	    for (int z = 1; z <= R; z++){
	        int cash = 0;
	        int beginer = pointer;
	        while (1){
	            cash += matrix[pointer];
	            pointer++;
	            if (pointer > N) pointer = 1;
	            if (cash + matrix[pointer] > k || beginer == pointer) break;
	        }
	        money += cash;
	    }
	    fprintf (fout, "Case #%d: %d\n", i, money);
	}
    fclose (fin);
    fclose (fout);
	system ("PAUSE");
	return 0;
}
