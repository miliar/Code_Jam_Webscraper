#include <cstdio>
#include <string.h>

int main (){

    FILE *fin = fopen("B-large.in", "r");
    FILE *fout = fopen ("out.txt", "w");
    int T;
    fscanf (fin, "%d", &T);

    for (int test_case = 0; test_case < T; test_case++){
        int n,s,p;
        fscanf (fin, "%d %d %d", &n, &s, &p);
        int result = 0;
        for (int googlers = 0; googlers < n; googlers++){
            int score;
            int p1 = p-1;
            int p2 = p-2;
            if (p - 1 < 0) p1 = 0;
            if (p - 2 < 0) p2 = 0;
            int test = p + p1 + p1;
            fscanf (fin, "%d", &score);

            if (test <= score){
                result++;
                printf ("normal: %d (%d)\n", score, p);
            }
            else if (s > 0){
                test = p + p2 + p2;
                if (test <= score){
                    s--;
                    result++;
                    printf ("surprising: %d (%d)\n", score, p);
                }
            }

        }
        fprintf (fout, "Case #%d: %d\n", test_case+1, result);


    }
    fclose (fin);
    fclose(fout);

    return 0;
}
