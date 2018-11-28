#include <stdio.h>
//#include <utility>
#include <map>
#include <list>
#include <set>

using namespace std;


int main()
{
  int d;
  scanf("%d", &d);
  for (int p=1; p<=d; p++)
    {
      list<char> let;
      map< pair<char,char>, char > comb;
      int ncomb;
      // wczytanie kombinacji
      scanf("%d",&ncomb);
      while (ncomb--)
        {
          char s[4];
          scanf("%s",s);
          if (s[0]!=s[1])
            {
              comb[make_pair(s[0],s[1])] = s[2];
              comb[make_pair(s[1],s[0])] = s[2];
            }
          else
            comb[pair<char,char>(s[0],s[1])] = s[2];
          //printf("Dodanie pary: (%c,%c) -> %c\n", s[0],s[1],);
        }
      // wczytanie par przeciwnych
      set< pair<char,char> > opos;
      int nopos;
      scanf("%d",&nopos);
      while (nopos--)
        {
          char s[3];
          scanf("%s",s);
          if (s[0]!=s[1])
            {
              opos.insert(make_pair(s[0],s[1]));
              opos.insert(make_pair(s[1],s[0]));
            }
          else
            opos.insert(pair<char,char>(s[0],s[1]));
        }
      // wczytanie liter wraz z uproszczeniem
      int n;
      scanf("%d",&n);
      char* s = new char[n+1];
      scanf("%s",s);
      for (int i=0; i<n; i++)
        {
          char c = s[i];
          if (let.empty())
            let.push_back(c);
          else
            {
              // parse comb
              while (!let.empty())
                {
                  map< pair<char,char>, char >::iterator it=comb.find(pair<char,char>(*let.rbegin(),c));
                  if (it==comb.end())
                    break;
                  //printf("Found pair: %c, %c -> %x\n", *let.rbegin(), c, it->second);
                  let.pop_back();
                  c = it->second;
                }

              // parse opos
              bool found = false;
              if (!let.empty())
                for (list<char>::reverse_iterator it = let.rbegin(); it!=let.rend(); ++it)
                  {
                    if (opos.find(make_pair(c,*it))!=opos.end())
                      {
                        found = true;
                        //let.erase((++it).base(), let.end());
                        let.clear();
                        break;
                      }
                  }
              if (!found)
                let.push_back(c);
            }
        }
      delete [] s;
      // wypisanie wyniku
      printf("Case #%d: [",p);
      if (!let.empty())
        {
          if (let.size()==1)
            {
              printf("%c",*let.begin());
            }
          else
            {
              list<char>::iterator i = let.begin();
              printf("%c",*i);
              for (++i; i!=let.end(); ++i)
                printf(", %c",*i);
            }
        }
      printf("]\n");
    }
  return 0;
}
