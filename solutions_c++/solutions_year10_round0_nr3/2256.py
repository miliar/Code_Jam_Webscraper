#include <cstdio>
#include <cstdlib>
using namespace std;


int main()
{
    FILE * input = fopen("input", "r");
    FILE * output = fopen("output", "w");
    int T;
    fscanf(input, "%d", &T);
    for(int cas = 1; cas <= T; cas++)
    {
        int R, k, N;
        fscanf(input, "%d%d%d", &R, &k, &N);
        int group[N];
        for(int i = 0; i < N; i++) fscanf(input, "%d", &group[i]);
        //
        int next[N];
        int money[N];
        for(int i = 0; i < N; i++)
        {
            int pris = 0;
            next[i] = i;
            while(pris + group[next[i]] <= k)
            {
                pris+=group[next[i]];
                next[i] = (next[i] + 1) % N;
                if(next[i] == i) break;
            }
            money[i] = pris;
        }
        //
        long long fric = 0;
        int tours = 0;
        bool visite[N];
        for(int i = 0; i < N; i++) visite[i] = false;
        int tour[N];
        int argent[N];
        int encours = 0;
        while(visite[encours] == false && tours < R)
        {
            visite[encours] = true;
            tour[encours] = tours;
            argent[encours] = fric;
            tours++;
            fric += money[encours];
            encours = next[encours];
        }
        if(tours < R) // suppr boucles
        {
            int taille_boucle = tours - tour[encours];
            int nb_passagers = fric - argent[encours];
            int nb_repetitions = (R - tours) / taille_boucle;
            tours += nb_repetitions * taille_boucle;
            fric += nb_repetitions * nb_passagers;
        }
        while(tours < R)
        {
            tours++;
            fric += money[encours];
            encours = next[encours];
        }
        fprintf(output, "Case #%d: %lld\n", cas, fric);
    }
     printf("done");
}

