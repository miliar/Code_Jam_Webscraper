#include <iostream>
#include <fstream>
#include <math.h>
#include <set>
#include <vector>
#include <map>

using namespace std;

// num_to_set[num] == set # of num
map<int,int>           num_to_set; 
// set_to_nums[set_num] == all nums in that set
map<int,set<int> >  set_to_nums;

vector<int> primes;

void add_new_set(int x)
{
   num_to_set[x] = x;
   set_to_nums[x].insert(x);
}

void join_sets(int X, int Y)
{
   int updated_set = num_to_set[X];
   int other_set = num_to_set[Y];

   if(updated_set == other_set)
      return;

   set<int>::iterator b = set_to_nums[other_set].begin();
   for(; b != set_to_nums[other_set].end(); ++b)
   {
      num_to_set[*b] = updated_set; // update all nums to be in combined set
      set_to_nums[updated_set].insert(*b);
   }

   map<int,set<int> >::iterator i = set_to_nums.find(other_set);
   set_to_nums.erase(i);
}

// vector<int> unshared(int A)
// {
   // return all numbers A currently isn't in a set with
// }

int solve(int A, int B, int P)
{
   num_to_set.clear();
   set_to_nums.clear();
   for(int i = A; i <= B; ++i)
   {
      add_new_set(i);
   }

   int x = sqrt(B);
 
   // need all primes from P to x
   int p = 1;

   vector<int>::iterator p_iter = primes.begin();

   for( ; p_iter != primes.end(); ++p_iter)
   {
      p = *p_iter;
      if(p < P)
         continue;
      for(int i = A; i <= B; ++i)
      {
         if(i % p != 0)
            continue;
         // TODO:  only unshared numbers
         //   currently this is very bubble sort like
         for(int j = i; j <= B; ++j)
         {
            if( (j % p == 0) )
            {
               join_sets(i,j);
            }
         }
      }
   }

   return set_to_nums.size();
}

void calc_primes(int max)
{
   bool p[max];

   for(int i = 0; i < max; ++i)
   {  
      p[i] = true;
   }

   p[0] = false;

   for(int i = 4; i < max; i+=2)
   {  
      p[i] = false;
   }

   for(int i = 3; i < sqrt(max); i += 2)
   {
      int start = i * i;
      p[start] = false;
      for(int j = start; j < max; j += i * 2)
      {
         p[j] = false;
      }
   }

   for(int i = 2; i < max; ++i)
   {
      if(p[i])
         primes.push_back(i);
   }
}

int main(int argc, char **argv)
{
   if(argc < 2)
   {
      cout << "need one input file" << endl;
      return 0;
   }

   calc_primes(1000);

   ifstream inf(argv[1]);
   int rows;
   inf >> rows;
   int cnt = 1;

   for(int i = 0; i < rows; ++i)
   {
      int A, B, P;
      inf >> A >> B >> P;
      int sets = solve(A,B,P);
      cout << "Case #" << i+1 << ": " << sets << endl;
   }

   // int sets = solve(10,20,5);
   // cout << "sets: " << sets << endl;
   // sets = solve(10,20,3);
   // cout << "sets: " << sets << endl;
}
