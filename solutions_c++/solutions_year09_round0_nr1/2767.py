#include <iostream>
#include <string>

using namespace std;

int main()
{
    int l, d, n;
    string palavra;
    cin >> l >> d >> n;
    string dicionario[d];
    for (int i = 0; i < d; i++)
    {
        cin >> palavra;
        dicionario[i] = palavra;
    }
    int quantidade;
    for (int i = 1; i <= n; i++)
    {
        quantidade = 0;
        cin >> palavra;
        int atual = 0;
        string tokens[l];
        bool parenteses = false;
        for (int j = 0; j < palavra.length(); j++)
        {
            if (palavra[j] == '(')
            {
                parenteses = true;
                continue;
            }
            if (palavra[j] != '(' && palavra[j] != ')') tokens[atual] += palavra[j];
            if (!parenteses) atual++;
            if (palavra[j] == ')')
            {
                parenteses = false;
                atual++;
            }
        }
        for (int j = 0; j < d; j++)
        {
            bool contem = true;
            for (int k = 0; k < l; k++)
            {
                int pos = tokens[k].find(dicionario[j][k]);
                if (pos == string::npos)
                {
                    contem = false;
                    break;
                }
            }
            if (contem) quantidade++;
        }
        cout << "Case #" << i << ": " << quantidade << endl;
    }
    return 0;
}
            
