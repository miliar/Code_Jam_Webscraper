#include <stdio.h>
#include <cmath>
#include <iostream>

#define MAX 1005

int t[MAX], l[MAX], n;
int nb_tests, A, B, P, rez;
bool marked[MAX];

void init();
int find(int x);
void uAdd(int x, int y);
bool have(int x, int y);

bool IsPrime(int x)
{
    const int max = static_cast<int>(std::sqrt(static_cast<double>(x))) + 1;
    for (int i = 2; i != max; ++i)
        if (x % i == 0) return false;
    return true;
}

int main()
{
    FILE *fin = fopen("B.in", "r");
    FILE *fout = fopen("Bout.out", "w");
    fscanf(fin, "%d", &nb_tests);
    for (int t = 1; t <= nb_tests; ++t)
    {
        rez = 0;
        memset(marked, 0, sizeof(marked));
        fscanf(fin, "%d%d%d", &A, &B, &P);
        n = B+1;
        init();
        for (int i = A; i <= B; ++i)
            for (int j = i+1; j <= B; ++j)
                if (have(i, j))
                    if (find(i) != find(j))
                        uAdd(find(i), find(j));
        for (int i = A; i <= B; ++i)
            marked[find(i)] = true;
        for (int i = A; i <= B; ++i)
            if (marked[i]) rez++;
        fprintf(fout, "Case #%d: %d", t, rez);
        if (t != nb_tests)
            fprintf(fout, "\n");
        printf("Case #%d\n", t);
    }
    fclose(fin);
    fclose(fout);
    system("pause");
    
    return 0;
}

void init()
{
    for (int i = 0; i < n; ++i)
    {
        t[i] = i;
        l[i] = 0; 
    }    
}   

int find(int x)
{
    if (t[x] == x) return x;
    else
        t[x] = find(t[x]); 
    return t[x];
}    

void uAdd(int x, int y)
{
    if (l[x] > l[y])
        t[y] = x;
    else
        if (l[y] > l[x])
            t[x] = y;
        else
            if (l[x] == l[y])
            {
                t[y] = x;
                l[x]++;
            }    
}   

bool have(int x, int y)
{
    int mm = ((x > y) ? (x) : (y));
    for (int i = P; i <= mm; i++)
        if (IsPrime(i))
            if (x % i == 0 && y % i == 0) 
                return true;
    return false;
}
