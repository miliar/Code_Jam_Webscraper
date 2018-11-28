#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Tocka
{
      public:
             int h;
             int smjer;
             char oznaka;
      Tocka ()
      {
            h = 0;
            smjer = -1;
            oznaka = '!';
      }
};

class Polje
{
      public:
             int r;
             int s;
      Polje () {}
      Polje (int _r, int _s)
      {
            r = _r;
            s = _s;
      }
};
            
int main()
{
    int T;
    scanf ("%d", &T);
    for (int t = 1; t <= T; t++)
    {
        int R, S;
        scanf ("%d %d", &R, &S);
        
        vector < vector <Tocka> > voda (R, vector <Tocka> (S));
        vector < Polje > sink;
        
        for (int r = 0; r < R; r++)
            for (int s = 0; s < S; s++)
                cin >> voda[r][s].h;    /* tu je gotov unos */
        
        for (int r = 0; r < R; r++)     /* upisem smjerove i odredim sinkove */
            for (int s = 0; s < S; s++)
            {
                int MIN = 999999;
                int kuda = -1;
                
                if (r-1 >= 0)              /* gore */
                   if (voda[r-1][s].h < MIN)
                   {
                      MIN = voda[r-1][s].h;
                      kuda = 0;
                   }
                if (s-1 >= 0)              /* lijevo */
                   if (voda[r][s-1].h < MIN)
                   {
                      MIN = voda[r][s-1].h;
                      kuda = 3;
                   }
                if (s+1 < S)              /* desno */
                   if (voda[r][s+1].h < MIN)
                   {
                      MIN = voda[r][s+1].h;
                      kuda = 1;
                   }
                if (r+1 < R)              /* dolje */
                   if (voda[r+1][s].h < MIN)
                   {
                      MIN = voda[r+1][s].h;
                      kuda = 2;
                   }
                
                if (MIN < voda[r][s].h)
                   voda[r][s].smjer = kuda;
                else
                {
                    Polje tmp(r,s);
                    sink.push_back(tmp); //cout << tmp.r << " " << tmp.s << endl;
                }
            }                          /* */
        
        char slovo = 'a';
        
        for (int i = 0; i < sink.size(); i++) /* radi bfs */
        {
            int p, k;
            vector < Polje > queue;
            
            queue.push_back(sink[i]);
            p = -1; k = 0;
            
            while (p < k)
            {
                  p++;
                  voda[queue[p].r][queue[p].s].oznaka = slovo;
                  
                  if (queue[p].r-1 >= 0)
                     if (voda[queue[p].r-1][queue[p].s].smjer == 2)
                     {
                        k++;
                        Polje tmp(queue[p].r-1,queue[p].s);
                        queue.push_back(tmp);
                     }
                  if (queue[p].s+1 < S)
                     if (voda[queue[p].r][queue[p].s+1].smjer == 3)
                     {
                        k++;
                        Polje tmp(queue[p].r,queue[p].s+1);
                        queue.push_back(tmp);
                     }
                  if (queue[p].r+1 < R)
                     if (voda[queue[p].r+1][queue[p].s].smjer == 0)
                     {
                        k++;
                        Polje tmp(queue[p].r+1,queue[p].s);
                        queue.push_back(tmp);
                     }
                  if (queue[p].s-1 >= 0)
                     if (voda[queue[p].r][queue[p].s-1].smjer == 1)
                     {
                        k++;
                        Polje tmp(queue[p].r,queue[p].s-1);
                        queue.push_back(tmp);
                     }
            }  
            slovo++;
        }
        
        vector <char> zamj (26,'?');
        char SLOVO = 'a';
        
        cout << "Case #" << t << ":" << endl;
        for (int r = 0; r < R; r++)
        {
            for (int s = 0; s < S-1; s++)
            {
                if (zamj[voda[r][s].oznaka-'a'] == '?')
                {
                   zamj[voda[r][s].oznaka-'a'] = SLOVO;
                   SLOVO++;
                }
                printf("%c ", zamj[voda[r][s].oznaka-'a']);
            }
            if (zamj[voda[r][S-1].oznaka-'a'] == '?')
            {
               zamj[voda[r][S-1].oznaka-'a'] = SLOVO;
               SLOVO++;
            }
            printf("%c\n", zamj[voda[r][S-1].oznaka-'a']);
        }
    }
    
    //system ("Pause");
    return 0;
}
