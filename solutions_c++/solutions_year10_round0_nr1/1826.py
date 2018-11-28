#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    FILE* fin = fopen("A-large.in", "r");
    FILE* fout = fopen("A-large.out", "w");
    int t;
    fscanf(fin, "%d", &t);
    for (int i = 0; i < t; i++) 
    {
        int n, k;
        fscanf(fin, "%d%d", &n, &k);
        int v = 1;
        for (int j = 0; j < n; j++)
        {
            v *= 2;
        }
        fprintf(fout, "Case #%d: ", i+1);
        if (v-1 == k%v)
        {
           fprintf(fout, "ON\n");
        }
        else
        {
            fprintf(fout, "OFF\n");
        }
    }
    return 0;
}
