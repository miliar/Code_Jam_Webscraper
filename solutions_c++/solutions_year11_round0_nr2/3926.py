#include<stdio.h>
#include<vector>
#include<map>
#include<string>
#include <algorithm>

using namespace std;

int main(int argc, char **argv)
{
    char tipos[] = { 'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F' };

    int casos;

    scanf("%d", &casos);

    for(int k = 1; k <= casos; k++)
    {

        int c;
        scanf("%d", &c);

        map<string, char> junta;
        map<char, char> oposto;

        vector<char> seq;

        for(int i = 0; i < c; i++)
        {
            scanf("%*c");

            char entrada[5];
            char elementoNovo;

            scanf("%s", entrada);

            elementoNovo = entrada[2];
            char temp[3];
            temp[0] = entrada[0];
            temp[1] = entrada[1];
            temp[2] = '\0';

            string nova = temp;

            junta[nova] = elementoNovo;

            temp[0] = entrada[1];
            temp[1] = entrada[0];
            nova = temp;

            junta[nova] = elementoNovo;
        }

        int d;

        scanf("%d", &d);

        char elementoAtual;
        char elementoOposto;

        for(int i = 0; i < d; i++)
        {
            scanf("%*c");

            scanf("%c%c", &elementoAtual, &elementoOposto);

            oposto[elementoAtual] = elementoOposto;
            oposto[elementoOposto] = elementoAtual;
        }

        int n;
        scanf("%d", &n);

        for(int i = 0; i < n; i++)
        {
            if(i == 0)
            {
                scanf("%*c");
            }

            char temp;
            scanf("%c", &temp);

            seq.push_back(temp);

            if(i > 0)
            {
                bool acheiJunto = false;

                char tentativa[3];
                tentativa[1] = temp;
                tentativa[2] = '\0';

                for(int j = 0; j < 8; j++)
                {
                    if(acheiJunto)
                    {
                        break;
                    }

                    tentativa[0] = tipos[j];

                    string busca = tentativa;

                    map<string, char>::iterator it;

                    it = junta.find(busca);

                    if(it != junta.end() && seq.size() >= 2)
                    {
                        char ultimo = seq[seq.size()-1];
                        char pen = seq[seq.size()-2];

                        if( (ultimo == tentativa[0] && pen == tentativa[1]) || (ultimo == tentativa[1] && pen == tentativa[0]) )
                        {
                            seq.erase( seq.end()-2, seq.end() );
                            seq.push_back(it->second);
                            acheiJunto = true;
                        }
                    }
                }

                if(!acheiJunto)
                {
                    map<char, char>::iterator itMap;
                    itMap = oposto.find(temp);

                    if(itMap != oposto.end())
                    {
                        char buscaOposto = itMap->second;

                        vector<char>::iterator itVector;

                        itVector = find(seq.begin(), seq.end(), buscaOposto);

                        if( itVector != seq.end() )
                        {
                            seq.clear();
                        }
                    }
                }
            }
        }

        printf("Case #%d: ", k);
        printf("[");
        for(int i = 0; i < seq.size(); i++)
        {
            if(i < seq.size() - 1)
            {
                printf("%c, ", seq[i]);
            }
            else
            {
                printf("%c", seq[i]);
            }
        }
        printf("]\n");

    }

    return 0;
}
