#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <list>

#define INPUT ("/Users/ilango/Projets/code_jam/2011/gorosort/input")
#define OUTPUT ("/Users/ilango/Projets/code_jam/2011/gorosort/output")

typedef std::vector<long int>  vint;
typedef std::vector<char> vchar;

void
getTestInput(std::ifstream& fin,
             long int&   n,
             vint&       vals)
{
   fin >> n;
   for (unsigned long int i = 0; i < n; ++i)
   {
      long int  p;
      fin >> p;
      vals.push_back(p);
   }
}

void
output(std::ofstream& fout,
       long int t,
       long int res)
{
   fout << "Case #" << t + 1
        << ": "<< res << std::endl;
}

long int
run(vint&   vals)
{
   long int res = vals.size();
   for (long int i = 0; i < vals.size(); ++i)
      if (vals[i] == i + 1)
         res--;
   return res;
}

int main()
{
   long int T = 0;

   std::ifstream fin(INPUT);
   std::ofstream fout(OUTPUT);

   fin >> T;

   for (unsigned long int t = 0; t < T; ++t)
   {
      long int  n = 0;
      vint   vals;

      getTestInput(fin, n, vals);

      long int res = run(vals);

      output(fout, t, res);
   }

   fin.close();
   fout.close();

   return 0;
}
