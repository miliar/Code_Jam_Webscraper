/*
 * SavingTheUniverse.cpp
 *
 *  Created on: 17/Jul/2008
 *      Author: Joao Azevedo (joao.c.azevedo@gmail.com)
 */

#include <iostream>
#include <map>

using namespace std;

bool all_used(bool used[], int Q)
{
    for (int i = 0; i < Q; i++)
    {
        if (!used[i])
            return false;
    }
    return true;
}

string parseString(string in)
{
    string final = "";
    for (size_t i = 0; i < in.size(); i++)
        if (in[i] >= 'A' && in[i] <= 'Z' ||
            in[i] >= 'a' && in[i] <= 'z' ||
            in[i] >= '0' && in[i] <= '9' ||
            in[i] == ' ')
            final += in[i];
    return final;
}

int main()
{
    int N;
    scanf("%d\n", &N);
    for (int i = 0; i < N; i++)
    {
        map<string, int> searchEngines;
        int S;
        scanf("%d\n", &S);
        for (int j = 0; j < S; j++)
        {
            string searchEngine;
            getline(cin, searchEngine);
            searchEngines[parseString(searchEngine)] = j;
        }
        int queries[1000];
        int Q;
        scanf("%d\n", &Q);
        for (int j = 0; j < Q; j++)
        {
            string searchEngine;
            getline(cin, searchEngine);
            queries[j] = searchEngines[parseString(searchEngine)];
        }
        bool used[1000];
        memset(used, false, sizeof(used));
        int C = 0;
        for (int j = 0; j < Q; j++)
        {
            used[queries[j]] = true;
            if (all_used(used, S))
            {
                C++;
                memset(used, false, sizeof(used));
                used[queries[j]] = true;
            }
        }
        cout << "Case #" << i+1 << ": " << C << endl;
    }
    return 0;
}
