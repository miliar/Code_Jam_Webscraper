#include <vector>
#include <iostream>
#include <fstream>
#include <iterator>
#include <stdint.h>

struct group_queue
{
   int pos;
   std::vector<int> queue;

   group_queue() : pos(0)
   {
   }

   void add_group(int size) 
   { 
      queue.push_back(size); 
   }

   void next()
   {
      pos++;
      if (pos == queue.size()) pos = 0;
   }

   int peek()
   {
      return queue[pos];
   }

   int size()
   {
      return queue.size();
   }
};

uint64_t simulate(group_queue& gp, int rc_size, int ride_count)
{
   uint64_t total = 0;

   for ( ; ride_count > 0; --ride_count)
   {
      int passengers = 0;
      int added_groups = 0;
      while ((passengers + gp.peek()) <= rc_size && added_groups < gp.size())
      {
         passengers += gp.peek();
         added_groups++;
         gp.next();
      }

      total += passengers;
   }

   return total;
}

void run_case(std::istream_iterator<int>& iit, int num)
{
   int rc_size = 0;
   int ride_count = 0;
   int n = 0;

   ride_count = *iit++;
   rc_size = *iit++;
   n = *iit++;

   group_queue gp;
   for ( ; n > 0; --n) gp.add_group(*iit++);

   std::cout << "Case #" << num << ": "
             << simulate(gp, rc_size, ride_count)
             << std::endl;
}

int main()
{
   std::ifstream file("input.dat");
   std::istream_iterator<int> iit(file);

   iit++; // to skip case count

   int num = 0;
   while (!file.eof())
   {
      run_case(iit, ++num);
   }

   return 0;
}
