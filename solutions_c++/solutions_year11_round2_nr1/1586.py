#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <list>

#define INPUT ("/Users/ilango/Projets/code_jam/2011/rpi/input")
#define OUTPUT ("/Users/ilango/Projets/code_jam/2011/rpi/output")

typedef long int lint;
typedef std::vector<long int>  vint;
typedef std::vector<char> vchar;

#define N_MAX    (101)
typedef char   imat[N_MAX][N_MAX];

void
getTestInput(std::ifstream& fin,
             lint&   N,
             imat    board)
{
   fin >> N;

   for (unsigned int i = 0; i < N; ++i)
   {
      fin >> board[i];
   }
}

void
output(std::ofstream& fout,
       lint t,
       lint n,
       double res[N_MAX])
{
   fout << "Case #" << t + 1 << ":" << std::endl;
   for (unsigned int i = 0; i < n; ++i)
      fout << res[i] << std::endl;
}

double
getWP(lint n, char b[N_MAX], lint except = -1)
{
   lint tot = 0;
   double wins = 0;
   for (lint i = 0; i < n; ++i)
   {
      if (i == except)
         continue;

      if (b[i] == '1')
      {
         wins++;
         tot++;
      }
      else if (b[i] == '0')
         tot++;
   }

   if (tot)
      return wins / tot;
   else
      return 0;
}

double
getOWP(lint n, imat b, lint p)
{
   lint tot = 0;
   double res = 0;

   for (lint i = 0; i < n; ++i)
   {
      if (b[p][i] != '.')
      {
         tot++;
         res += getWP(n, b[i], p);
      }
   }
   if (tot)
      return res / tot;
   else
      return 0;
}

double
getOOWP(lint n, char b[N_MAX], double owp[N_MAX])
{
   lint tot = 0;
   double res = 0;

   for (lint i = 0; i < n; ++i)
   {
      if (b[i] != '.')
      {
         res += owp[i];
         tot++;
      }
   }

   if (tot)
      return res / tot;
   else
      return 0;
}

long int
run(lint N,
    imat board,
    double res[N_MAX])
{
   double WP[N_MAX];
   double OWP[N_MAX];
   double OOWP[N_MAX];

   for (lint i = 0; i < N; ++i)
   {
      WP[i] = getWP(N, board[i]);
      OWP[i] = getOWP(N, board, i);
   }

   for (lint i = 0; i < N; ++i)
      OOWP[i] = getOOWP(N, board[i], OWP);

   for (lint i = 0; i < N; ++i)
      res[i] = .25 * WP[i] + .5 * OWP[i] + .25 * OOWP[i];

   return 0;
}



int main()
{
   lint T = 0;

   std::ifstream fin(INPUT);
   std::ofstream fout(OUTPUT);
   fout.precision(12);

   fin >> T;

   for (unsigned long int t = 0; t < T; ++t)
   {
      lint   N;
      imat   board;
      double res[N_MAX];
      
      getTestInput(fin, N, board);

      run(N, board, res);

      output(fout, t, N, res);
   }

   fin.close();
   fout.close();

   return 0;
}
