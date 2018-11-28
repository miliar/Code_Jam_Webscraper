#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
using namespace std;

//un truc exponentiel pour le petit test
//attention : non empty sets
//ok solved, 30 points normalement, c'est déjà ça

//lol : tout sauf le plus petit ça marche, si la somme xor fait 0

int main()
{
    FILE * input = fopen("input", "r");
    FILE * output = fopen("output", "w");
    int T;
    fscanf(input, "%d", &T);
    for(int cas = 1; cas <= T; cas++)
    {
        int n;
        fscanf(input, "%d", &n);
        int value[n];
        for(int i = 0; i < n; i++)
            fscanf(input, "%d", &value[i]);
        int sxor = 0;
        for(int i = 0; i < n; i++) sxor = sxor ^ value[i];
        if(sxor != 0)
            fprintf(output, "Case #%d: NO\n", cas);
        else
        {
            int m = 100000000;
            int s = 0;
            for(int i = 0; i < n; i++)
                { s += value[i]; m = min(m, value[i]); }
            printf("%d %d\n", cas, m);
            s -= m;
            fprintf(output, "Case #%d: %d\n", cas, s);
        }
    }
	return 0;
}


/*
int maxx (int s1, int s2, int xors1, int xors2, int rang, int n, int * value)
{
    //printf("rang %d s %d xor %d %d\n", rang, s1, xors1, xors2);
    if(rang == n)
    {
        if(xors1 == xors2 && s1 > 0 && s2 > 0) return s1;
        else return -1;
    }
    int a = maxx(s1, s2 + value[rang], xors1, xors2 ^ value[rang],  rang + 1, n, value);
    int b = maxx(s1 + value[rang], s2, xors1 ^ value[rang], xors2, rang + 1, n, value);
    return max(a,b);
}

int main()
{
    FILE * input = fopen("input", "r");
    FILE * output = fopen("output", "w");
    int T;
    fscanf(input, "%d", &T);
    for(int cas = 1; cas <= T; cas++)
    {
        int n;
        fscanf(input, "%d", &n);
        int value[n];
        //printf("n %d. ", n);
        for(int i = 0; i < n; i++)
            { fscanf(input, "%d", &value[i]); }//printf("%d ", value[i]); }
        //printf("\n");
        int xs = 0;
        for(int i = 0; i < n; i++) xs = xs ^ value[i];
        int resultat = maxx(0, 0, 0, 0, 0, n, value);
        if((xs == 0 && resultat < 0) || (xs != 0 && resultat > 0)) printf("contradiction\n");
        int minimum = 10000000;
        for(int i = 0; i < n; i++)
            if(value[i] < minimum) minimum = value[i];
        int essai = 0;
        for(int i = 0; i < n; i++) essai += value[i];
        essai -= minimum;
        if(resultat >= 0 && essai != resultat) printf("%d vrai %d essai %d\n", cas, resultat, essai);
        if(resultat < 0)
            fprintf(output, "Case #%d: NO\n", cas);
        else fprintf(output, "Case #%d: %d\n", cas, resultat);
    }
	return 0;
}*/
