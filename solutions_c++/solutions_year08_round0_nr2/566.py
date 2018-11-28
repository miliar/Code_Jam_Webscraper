#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string.h>

using namespace std;
FILE* in = fopen("B-large.in","r");

int processTestCase(int* saiA, int* saiB)
{
    // turnaround time
    int T;
    fscanf(in,"%d", &T);
    //cout << "T: " << T << endl;

    // detais schedule
    int NA, NB;
    fscanf(in,"%d %d", &NA, &NB);
    //cout << "NA: " << NA << endl;
    //cout << "NB: " << NB << endl;

    vector<int> departureA, departureB;
    vector<int> availableA, availableB;

    int departTime, availTime;

    int na;
    for(na = 0; na < NA; na++)
    {
        int departH, departM, arivH, arivM;
        fscanf(in,"%d:%d %d:%d", &departH, &departM, &arivH, &arivM);

        // Horário de saída em minutos do dia
        departTime = departH*60 + departM;
        departureA.push_back(departTime);

        // Horário de disponibilidade do trêm na estação B
        availTime = arivH*60 + arivM + T;
        availableB.push_back(availTime);

        //cout << "departure from A: " << departTime << " " << "available at B:" << availTime << endl;
    }

    int nb;
    for(nb = 0; nb < NB; nb++)
    {
        int departH, departM, arivH, arivM;
        fscanf(in,"%d:%d %d:%d", &departH, &departM, &arivH, &arivM);

        // Horário de saída em minutos do dia
        departTime = departH*60 + departM;
        departureB.push_back(departTime);

        // Horário de disponibilidade do trêm na estação B
        availTime = arivH*60 + arivM + T;
        availableA.push_back(availTime);

        //cout << "departure from B: " << departTime << " " << "available at A:" << availTime << endl;
    }

    sort(availableA.begin(),availableA.end());
    sort(availableB.begin(),availableB.end());

    sort(departureA.begin(),departureA.end());
    sort(departureB.begin(),departureB.end());

    int trem, disp;

    for(trem = 0, disp = 0; trem < departureA.size(); trem++)
    {
        // se algum trem chegará a estação ...
        if(!availableA.empty())
        {
            // Se não há um trem esperando, coloque um na linha
            if(departureA[trem] < availableA[disp])
            {
                (*saiA)++;
            }
            // Senão, use algum disponível
            else
            {
                disp++;

                // Se todos os trens já foram usados
                if(disp >= availableA.size())
                    availableA.clear();
            }
        }
        // senão ...
        else
        {
            (*saiA)++;
        }
    }

    for(trem = 0, disp = 0; trem < departureB.size(); trem++)
    {
        // se algum trem chegará a estação ...
        if(!availableB.empty())
        {
            // Se não há um trem esperando, coloque um na linha
            if(departureB[trem] < availableB[disp])
            {
                (*saiB)++;
            }
            // Senão, use algum disponível
            else
            {
                disp++;

                // Se todos os trens já foram usados
                if(disp >= availableB.size())
                    availableB.clear();
            }
        }
        // senão ...
        else
        {
            (*saiB)++;
        }
    }

    return 0;
}

int main()
{

    FILE* outfile = fopen("output.dat","w");

    // test cases number
    int N;
    fscanf(in, "%d", &N);

    //cout << "N: " << N << endl;

    int n;
    // para cada test case
    for(n = 1; n <= N; n++)
    {
        int saiA, saiB;
            saiA = 0;
            saiB = 0;
        processTestCase(&saiA, &saiB);

        //printf("Case #%d: %d %d\n",n,saiA, saiB);
        fprintf(outfile, "Case #%d: %d %d\n",n,saiA, saiB);
        //getchar();
    }

    return 0;
}
