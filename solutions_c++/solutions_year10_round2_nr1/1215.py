#include <stdio.h>
#include <string.h>
#include <iostream.h>
#include <conio.h>


using namespace std;

FILE *f = fopen("in.in", "r");
FILE *g = fopen("out.out", "w");

char sir[500][500], path[500];

int N, M, T; 

int compare(int n)
{
    //comparare path cu sir[n]
    int nr = 0, i = 1;
    int max1 = strlen(path);
    int max2 = strlen(sir[n]);
    int max;
    if (max1 > max2) max = max2;
    else max = max1;
    while ((i < max) && (path[i] == sir[n][i]))
    {
       if (path[i] == '/') nr++;
       i++;
    }
    if ((N >= 10) && (M == 5))
    {
          // cout << "GATA";
          //cout << sir[n] << "\n";
          //cout << "i = " << i << "max1 = " << max1 << " max2 = " << max2 << "\n";
    }
    if ((i == max - 1) && ((path[i] == '/') || (sir[n][i] == '/') || (max1 == max2))) nr++;
    if ((i == max) && ((path[i] == '/') || (sir[n][i] == '/') || (max1 == max2))) nr++;  
    return nr;
}

int main()
{
    
    fscanf(f, "%d\n", &T);
    for (int k = 0; k < T; ++k)
    {
        fscanf(f, "%d %d\n", &N, &M);
        for (int i = 0; i < N; ++i)
        {
            fgets(sir[i], 200, f);
        }
        long long nrMax = 0;
        for (int i = 0; i < M; ++i)
        {
            fgets(path, 200, f);
            if ((N >= 10) && (M == 5)) {
            //cout << "i principal = " << i << "\n";
            //cout << "path = " << path << "\n";
            }
            int maxim = 0;
            for (int j = 0; j < N; ++j)
            {
                int nr = compare(j);
                if (nr > maxim) maxim = nr;
            }
            int nrDeFoldere = 0;
            for (int j = strlen(path) - 1; j >= 0; --j)
            {
                if (path[j] == '/') nrDeFoldere++;
            }
            //cout << "nrDeFoldere = " << nrDeFoldere << " maxim = " << maxim << "\n";
            nrMax += (nrDeFoldere - maxim);
            strcpy(sir[N++], path);
        }
        fprintf(g, "Case #%d: %lld\n",  k + 1, nrMax); 
        //cout << "\n";
        //getch();
        for (int i = 0; i < N; ++i)
            sir[i][0] = '\0';
        path[0] = '\0';
    }
    
    fclose(f);
    fclose(g);
    
    
    return 0;
}
