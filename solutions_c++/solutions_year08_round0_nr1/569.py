#include <iostream>
#include <fstream>
#include <vector>
#include <string.h>

using namespace std;

ifstream in("A-large.in");

int processTestCase()
{
    // number of search engines
    int S;
    in >> S;
    //cout << "S: " << S << endl;

    vector<string> searchEng;
    vector<int> patternMatch;

    int s;
    for(s = 0; s < S; s++)
    {
        // lê nome das engines
        char engine[105] = "";
        while(strlen(engine) <= 0)
            in.getline(engine,105);

        // Armazena nome das engines
        searchEng.push_back(engine);
        patternMatch.push_back(0);
    }

    // search patterns
    int Q;
    in >> Q;
    //cout << "Q: " << Q << endl;

    int changes = 0;
    int full = 0;

    int q;
    for(q = 0; q < Q; q++)
    {
        // lê nome dos padrões de busca
        char pattern[105] = "";
        while(strlen(pattern) <= 0)
            in.getline(pattern,105);

        //cout << "pattern: " << pattern << endl;

        int s1;
        // Compara o nome dos padrões de busca com as engines
        for(s1 = 0; s1 < S; s1++)
        {
            // verifica se o padrao combina
            if(strncmp(searchEng[s1].c_str(),pattern,105) == 0)
            {
                //cout << "engine: " << searchEng[s1] << endl;

                if(patternMatch[s1] == 0)
                {
                    //cout << "Match!" << endl;
                    full++;
                }

                patternMatch[s1] = 1;
            }
            // se todos os padrões já estão sendo usados
            if(full == S)
            {
                //cout << "One change!" << endl;
                changes++;

                // reseta
                full = 0;
                int s2;
                for(s2 = 0; s2 < S; s2++)
                {
                    patternMatch[s2] = 0;
                }
                patternMatch[s1] = 1;
                full++;
            }
        }
    }

    return changes;
}

int main()
{

    FILE* outfile = fopen("output.dat","w");

    // test cases number
    int N;
    in >> N;

    //cout << "N: " << N << endl;

    int n;
    // para cada test case
    for(n = 1; n <= N; n++)
    {
        fprintf(outfile, "Case #%d: %d\n",n,processTestCase());
        //getchar();
    }

    return 0;
}
