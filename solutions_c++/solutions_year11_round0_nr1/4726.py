#include<fstream>
#include<cstdlib>
using namespace std;

ifstream fin("in.txt");
ofstream fout("out.txt");

int main()
{
    int N, T, O[101], B[101], i, j, k, t, L, M, pozO, pozB, time;

    struct
    {
        char robot;
        int button;
    }task[101];

    fin >> T;

    for(t = 1; t <= T; t++)
    {

        fin >> N; L = M = 0;

        for(i = 1; i <= N; i++)
        {
            fin >> task[i].robot >> task[i].button;

            if(task[i].robot == 'O') O[++L] = task[i].button;
            else B[++M] = task[i].button;
        }

        /*DEBUG*/
        /*for(i=1;i<=L;i++) fout<<O[i]<<' ';
        fout<<'\n';
        for(i=1;i<=M;i++) fout<<B[i]<<' ';*/

        time = 0; j = k = 1; pozO = pozB = 1;

        for(i = 1; i <= N; i++)
            if(task[i].robot == 'O')
            {
                time += abs(task[i].button - pozO) + 1;

                if(k <= M)
                {
                    if(pozB <= B[k])
                        if(pozB + abs(task[i].button - pozO) + 1 <= B[k])
                            pozB += abs(task[i].button - pozO) + 1;
                        else
                            pozB = B[k];
                    else
                        if(pozB - (abs(task[i].button - pozO) + 1) >= B[k])
                            pozB -= (abs(task[i].button - pozO) + 1);
                        else
                            pozB = B[k];
                }

                pozO = task[i].button; j++;
            }
            else
            {
                time += abs(task[i].button - pozB) + 1;

                if(j <= L)
                {
                    if(pozO <= O[j])
                        if(pozO + abs(task[i].button - pozB) + 1 <= O[j])
                            pozO += abs(task[i].button - pozB) + 1;
                        else
                            pozO = O[j];
                    else
                        if(pozO - (abs(task[i].button - pozB) + 1) >= O[j])
                            pozO -= (abs(task[i].button - pozB) + 1);
                        else
                            pozO = O[j];
                }

                pozB = task[i].button; k++;
            }

            fout << "Case #" << t << ": " << time << '\n';
    }

    fin.close(); fout.close();

    return 0;
}
