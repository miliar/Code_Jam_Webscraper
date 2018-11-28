#include <iostream>
#include <fstream>
using namespace std;

int t,o;
int ox[5],oy[5],xx[5],xy[5];
char a[5][5];
bool f,end;
ifstream fin("A-large.in");
ofstream fout("A.out");

bool check(char c)
{
     for (int i=1;i<=4;++i)
     {
         if (!(a[i][i]==c || a[i][i]=='T')) return false;
     }
     return true;
}

bool check2(char c)
{
     for (int i=1;i<=4;++i)
     {
         if (!(a[i][5-i]==c || a[i][5-i]=='T')) return false;
     }
     return true;
}

int main()
{
    fin >> t;
    o = 0;
    while (t--)
    {
          o++;
          f = false;
          memset(ox,0,sizeof(ox));
          memset(oy,0,sizeof(ox));
          memset(xx,0,sizeof(ox));
          memset(xy,0,sizeof(ox));
          for (int i=1;i<=4;++i)
          for (int j=1;j<=4;++j)
          {
              fin >> a[i][j];
              switch (a[i][j])
              {
                     case '.': f = true;
                               ox[i] = ox[i];oy[j] = oy[j];
                               xx[i] = xx[i];xy[j] = xy[j];
                               break;
                     case 'T': ox[i] = ox[i]+1;oy[j] = oy[j]+1;
                               xx[i] = xx[i]+1;xy[j] = xy[j]+1;
                               break;
                     case 'X': xx[i] = xx[i]+1;xy[j] = xy[j]+1;
                               ox[i] = ox[i];oy[j] = oy[j];
                               break;
                     case 'O': ox[i] = ox[i]+1;oy[j] = oy[j]+1;
                               xx[i] = xx[i];xy[j] = xy[j];
                               break;
              }
          }
          fout << "Case #" << o << ": ";
          end = false;
          for (int i=1;i<=4;++i)
          if (ox[i]==4 || oy[i]==4)
          {
              fout << "O won" << endl;
              end = true;
              break;
          }
          if (end) continue;
          if (check('O')) {fout << "O won" << endl;continue;}
          if (check2('O')) {fout << "O won" << endl;continue;}
          for (int i=1;i<=4;++i)
          if (xx[i]==4 || xy[i]==4)
          {
              fout << "X won" << endl;
              end = true;
              break;
          }
          if (end) continue;
          if (check('X')) {fout << "X won" << endl;continue;}
          if (check2('X')) {fout << "X won" << endl;continue;}
          if (f) {fout << "Game has not completed" << endl; continue;}
          fout << "Draw" << endl;
    }
    return 0;
}
