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
    int n, num;
    FILE *fout = fopen ("candy.out", "w+");
    FILE *fin = fopen ("C-large.in", "r");
    fscanf (fin, "%d", &n);
    int potency[50];
    for (int i = 0; i < 50; i++) potency[i] = 0;
    int smallest = 0;
    long long int sum = 0;
    for (int k = 0; k < n; k++){
        for (int i = 0; i < 50; i++) potency[i] = 0;
        sum = 0;
        smallest = -1;
        fscanf (fin, "%d", &num);
        for (int j = 0; j < num; j++){
            int a;
            fscanf (fin, "%d", &a);
            if (a < smallest || smallest < 0) smallest = a;
            sum += a;
            for (int i = 0; i < 35; i++){
                double k = pow(2.0, i);
                //printf ("%d %lf\n", a, k);
                if (a&((int)k)){
                    potency[i]++;
                    //printf ("%d %d %d\n", a, (int)k, i);
                }
            }
        }
        int possible = 1;
        for (int i = 0; i < 35; i++){
            if (potency[i]%2){
                //printf ("%d %d\n", i, potency[i]);
                possible = 0;
            }
        }
        if (possible){
            fprintf (fout, "Case #%d: %lld\n",k+1, sum-smallest);
        }
        else fprintf (fout, "Case #%d: NO\n", k+1);
    }

	system ("PAUSE");
	return 0;
}
