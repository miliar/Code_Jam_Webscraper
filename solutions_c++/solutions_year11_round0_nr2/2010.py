#include <iostream>
#include <cstring>
#include <cstdio>
#include <list>

using namespace std;

char comb[255][255];
list<char> opp[255];
int listhas[255];

int main()
{
  int T, C, D, N;
  cin >> T;
  for (int t=1; t<=T; t++)
    {
      memset(comb, 0, 255*255*sizeof(char));
      memset(listhas, 0, 255*sizeof(int));
      for (int i=0; i<255; i++)
        opp[i].clear();

      cin >> C;
      for (int i=0; i<C; i++)
        {
          char a, b, c;
          scanf(" %c%c%c", &a, &b, &c);
          comb[a][b]=c;
          comb[b][a]=c;
        }

      cin >> D;
      for (int i=0; i<D; i++)
        {
          char a, b;
          scanf(" %c%c", &a, &b);
          opp[a].push_back(b);
          opp[b].push_back(a);
        }

      cin >> N;
      char c;
      list<char> l;
      for (int i=0; i<N; i++)
        {
          scanf(" %c", &c);
          if (!l.empty() && comb[l.back()][c] != 0)
            {
              listhas[l.back()]--;
              l.back()=comb[l.back()][c];
              listhas[l.back()]++;
            }
          else
            {
              int cleared=0;
              for (list<char>::iterator d=opp[c].begin(); d!=opp[c].end(); d++)
                {
                  if (listhas[*d]>0)
                    {
                      memset(listhas, 0, 255*sizeof(int));
                      l.clear();
                      cleared = 1;
                      break;
                    }
                }
              if (!cleared)
                {
                  l.push_back(c);
                  listhas[c]++;
                }
            }
        }

      printf("Case #%d: [", t);
      for (list<char>::iterator i=l.begin(); i!=l.end(); i++)
        {
          if (i!=l.begin())
            printf(", ");
          printf("%c", *i);
        }
      printf("]\n");
    }

  return 0;
}
