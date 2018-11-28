
#include <iostream>
#include <fstream>
#include <list>


using namespace std;
int resolver(int times, int capacity, list<int> &grupos)
{
   int profit = 0;
   for(int i(0); i <times ; ++i)
   {
      int people_in = 0;
      list<int> grupos_in;
      while(!grupos.empty() && people_in + grupos.front()<=capacity)
      {
         people_in += grupos.front();
         grupos_in.push_back(grupos.front());
         grupos.pop_front();
      }
      profit += people_in;
      for(list<int>::iterator it = grupos_in.begin(); it!= grupos_in.end(); ++it)
      {
         grupos.push_back(*it);
      }
   }
   return profit;
}
int main()
{
   ifstream input("C-small.in");
   ofstream output("output.out");
   int n;
   input >> n;
   for(int i(0); i < n; ++i)
   {
      int r, k, g;
      input >> r >> k >> g;
      list<int> grupos;
      for(int j(0); j < g; ++j)
      {
         int temp;
         input >> temp;
         grupos.push_back(temp);
      }
      output << "Case #" << i+1 << ": " << resolver(r, k, grupos) << endl;
   }
}
