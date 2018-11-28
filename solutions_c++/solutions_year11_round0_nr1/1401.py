#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <list>

#define PATH ("/Users/ilango/Projets/code_jam/2011/bot_trust")
#define INPUT ("/Users/ilango/Projets/code_jam/2011/bot_trust/input")
#define OUTPUT ("/Users/ilango/Projets/code_jam/2011/bot_trust/output")

typedef std::vector<long int>  vint;
typedef std::vector<char> vchar;

void
getTestInput(std::ifstream& fin,
             long int&   n,
             vchar& robot,
             vint&  pos)
{
   fin >> n;
   for (unsigned long int i = 0; i < n; ++i)
   {
      char c;
      long int  p;
      fin >> c;
      fin >> p;
      robot.push_back(c);
      pos.push_back(p);
   }
}

void
output(std::ofstream& fout,
       long int t,
       long int time)
{
   fout << "Case #" << t + 1
        << ": "<< time << std::endl;
}

long int
run(long int&    n,
    vchar&  robot,
    vint&   pos)
{
   long int   total = 0;
   long int   orange_pos = 1;
   long int   blue_pos = 1;

   char  cur_robot = robot[0];
   long int   cur_time = 0;
   
   for (unsigned long int i = 0; i < n; ++i)
   {
      long int time = 0;
      if (robot[i] == 'O')
      {
         time = std::abs(orange_pos - pos[i]);
         orange_pos = pos[i];
      }
      else
      {
         time = std::abs(blue_pos - pos[i]);
         blue_pos = pos[i];
      }

      if (cur_robot != robot[i])
      {
         time = std::max((time - cur_time), (long int)0);
         cur_robot = robot[i];
         cur_time = 0;
      }

      time++;
      cur_time += time;
      total += time;
   }

   return total;
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
      vchar  robot;
      vint   pos;

      getTestInput(fin, n, robot, pos);

      long int time = run(n, robot, pos);

      output(fout, t, time);
   }

   fin.close();
   fout.close();

   return 0;
}

