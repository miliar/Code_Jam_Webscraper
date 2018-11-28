#include <iostream>
#include <string>

#define MAXN 10001
#define MAXM 101

using namespace std;

string words[MAXN];
int N;

bool shouldGuess(string possibleWords[], int c, char p)
{
     int i, j;
     for (i = 0; i < c; ++i)
         for (j = 0; j < possibleWords[i].size(); ++j)
             if (possibleWords[i][j] == p)
                return true;
     return false;
}

string bestWord(string list)
{
       string wordSoFar;
       string possibleWords[MAXN];
       int i, j, c, k, price, max_price = -1;
       string max_word;
       for (i = 0; i < N; ++i)
       {
           price = 0;
           wordSoFar = "";
           for (j = 0; j < words[i].size(); ++j)
               wordSoFar += "B";
           c = 0;
           for (j = 0; j < N; ++j)
               if (words[j].size() == words[i].size())
                  possibleWords[c++] = words[j];
           int posInList = 0;
           while (c != 1)
           {
                 if (shouldGuess(possibleWords, c, list[posInList]))
                 {
                    bool exists = false;
                    for (j = 0; j < words[i].size(); ++j)
                    {
                        if (words[i][j] == list[posInList])
                        {
                           exists = true;
                           wordSoFar[j] = list[posInList];
                        }
                    }
                    if (!exists)
                       ++price;
                    
                    int c2 = 0;
                     for (j = 0; j < c; ++j)
                     {
                         for (k = 0; k < wordSoFar.size(); ++k)
                         {
                             if (!((wordSoFar[k] == 'B') || (wordSoFar[k] == possibleWords[j][k])))
                                break;
                             if ((!exists) && (possibleWords[j][k] == list[posInList]))
                                break;
                             if ((possibleWords[j][k] == list[posInList]) && (wordSoFar[k] != list[posInList]))   
                                break;
                         }
                         if (k == wordSoFar.size())
                            possibleWords[c2++] = possibleWords[j];
                     }
                     c = c2;
                 }
                 posInList++;
                 
           }
           if (price > max_price)
           {
              max_price = price;
              max_word = words[i];
           }
       }   
       return max_word;    
}

int main()
{
    int T, t, M, i;
    string list;
    cin >> T;
    for (t = 0; t < T; ++t)
    {
        cin >> N >> M;
        for (i = 0; i < N; ++i)
            cin >> words[i];
        cout << "Case #" << t+1 << ": ";
        for (i = 0; i < M; ++i)
        {
            cin >> list;
            cout << bestWord(list);
            if (i < M-1)
               cout << " ";
        }
        cout << endl;
    }
    return 0;
}
