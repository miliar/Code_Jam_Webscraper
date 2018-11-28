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

	FILE *fin = fopen ("A-small-attempt1.in", "r");
	FILE *fout = fopen ("A-small-attempt1.out", "w");
    int T, n, k;
	fscanf (fin, "%d\n", &T);
	for (int i = 1; i <= T; i++){
	    fscanf (fin, "%d %d", &n, &k);
	    int matrix[40] = {0};
        for (int j = 1; j <= k; j++){
            for (int z = 1; z <= n; z++){
                if (matrix[z] == 0){ matrix[z] = 1; break;}
                matrix[z] = 0;
            }
        }
        int bulb = 1;
        for (int j = 1; j <= n; j++){
            if (matrix[j] == 0){ bulb = 0; break;}
        }
        if (bulb == 1){
            fprintf (fout, "Case #%d: ON\n", i);
        }
        else fprintf (fout, "Case #%d: OFF\n", i);
	}
    fclose (fout);
    fclose (fin);
	system ("PAUSE");
	return 0;
}
