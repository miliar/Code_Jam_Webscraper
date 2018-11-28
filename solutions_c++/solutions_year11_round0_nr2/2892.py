#include <iostream>
#include <cstring>
#include <string>
#include <map>
#include <list>

using namespace std;

int main()
{
    map<char, list<char> > opposed;
    int in_sequence['Z'-'A'+1];
    char combine['Z'-'A'+1]['Z'-'A'+1];
    int T, C, D, N;
    cin >> T;

    for (int i = 0; i < T; i++)
    {
        opposed.clear();
        memset(combine, -1, sizeof(combine));
        memset(in_sequence, 0, sizeof(in_sequence));

        cin >> C;
        for (int j = 0; j < C; j++)
        {
            string comb;
            cin >> comb;
            combine[comb[0]-'A'][comb[1]-'A'] = 
                combine[comb[1]-'A'][comb[0]-'A'] = comb[2];
        }

        cin >> D;
        for (int j = 0; j < D; j++)
        {
            string opp;
            cin >> opp;
            opposed[opp[0]].push_back(opp[1]);
            opposed[opp[1]].push_back(opp[0]);
        }

        string final = "";
        string input;
        cin >> N;
        cin >> input;
        for (int j = 0; j < N; j++)
        {
            if (final.size() == 0)
            {
                final += input[j];
                in_sequence[input[j]-'A']++;
            }
            else if (final.size() > 0 && 
                combine[final[final.size()-1]-'A'][input[j]-'A'] != -1)
            {
                in_sequence[final[final.size()-1]-'A']--;
                final[final.size()-1] = 
                    combine[final[final.size()-1]-'A'][input[j]-'A'];
                in_sequence[final[final.size()-1]-'A']++;
            }
            else
            {
                for (list<char>::iterator itr = opposed[input[j]].begin();
                     itr != opposed[input[j]].end(); itr++)
                    if (in_sequence[*itr-'A'] > 0)
                    {
                        final.clear();
                        memset(in_sequence, 0, sizeof(in_sequence));
                        break;
                    }

                if (final.size() > 0)
                {
                    final += input[j];
                    in_sequence[input[j]-'A']++;
                }
            }
        }

        cout << "Case #" << i+1 << ": [";
        for (size_t i = 0; i < final.size(); i++)
        {
            cout << final[i];
            if (i+1 < final.size())
                cout << ", ";
        }
        cout << "]" << endl;
    }
    
    return 0;
}
