#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <map>

#define INPUT ("/Users/ilango/Projets/code_jam/2011/magicka/input")
#define OUTPUT ("/Users/ilango/Projets/code_jam/2011/magicka/output")

typedef std::vector<long int>  vint;
typedef std::vector<char> vchar;

typedef std::pair<char, char> cpair;
typedef std::map<char, std::map<char, char> > combi_map;
typedef std::map<char, std::map<char, bool> > oppos_map;

void
getTestInput(std::ifstream& fin,
             combi_map& combi,
             oppos_map& oppos,
             std::string& elts)
{
   int C;
   fin >> C;
   for (unsigned int i = 0; i < C; ++i)
   {
      char c[3];
      fin >> c;
      combi[c[0]][c[1]] = c[2];
      combi[c[1]][c[0]] = c[2];
   }

   int D;
   fin >> D;
   for (unsigned int i = 0; i < D; ++i)
   {
      char c[2];
      fin >> c;
      oppos[c[0]][c[1]] = 1;
      oppos[c[1]][c[0]] = 1;
   }

   int N;
   fin >> N;
   fin >> elts;
}

void
output(std::ofstream& fout,
       long int t,
       vchar&   res)
{
   fout << "Case #" << t + 1
        << ": " << "[";
   for (unsigned int i = 0; i < res.size(); ++i)
   {
      fout << res[i];
      if (i < res.size() - 1)
         fout << ", ";
   }
   fout << "]" << std::endl;
}


void
run(combi_map& combi,
    oppos_map& oppos,
    std::string& elts,
    vchar&   res)
{
   for (unsigned int i = 0; i < elts.size(); ++i)
   {
      // check for combine
      if (res.size() && combi[elts[i]][res.back()] != 0)
      {
         res.back() = combi[elts[i]][res.back()];
         continue;
      }
      
      // check for opposite
      bool opp = false;
      for (unsigned int j = 0; j < res.size(); ++j)
         if (oppos[elts[i]][res[j]])
         {
            opp = true;
            break;
         }
      if (opp)
      {
         res.clear();
         continue;
      }

      res.push_back(elts[i]);
   }
}

int main()
{
   long int T = 0;

   std::ifstream fin(INPUT);
   std::ofstream fout(OUTPUT);

   fin >> T;

   for (unsigned long int t = 0; t < T; ++t)
   {
      combi_map combi;
      oppos_map oppos;
      std::string elts;
      vchar   res;

      getTestInput(fin, combi, oppos, elts);

      run(combi, oppos, elts, res);

      output(fout, t, res);
   }

   fin.close();
   fout.close();

   return 0;
}
