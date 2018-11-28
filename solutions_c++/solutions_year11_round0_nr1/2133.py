#include <list>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <string>
#include <math.h>

size_t find_task(size_t start, std::vector<std::pair<bool, int>> const & tasks, bool orange)
{
   for (size_t l = start; l != tasks.size(); ++l)
   {
      if (tasks[l].first == orange)
         return l;
   }

   return -1;
}

int main()
{
   size_t C = 0;
   std::cin >> C;

   for (size_t tc = 1; tc != C + 1; ++tc)
   {
      size_t N = 0;
      std::cin >> N;

      std::vector<std::pair<bool, int>> events;
      for (size_t l = 0; l != N; ++l)
      {
         char R;
         int P;
         std::cin >> R >> P;
         events.push_back(std::make_pair(R == 'O', P));
      }

      int o_pos = 1;
      int b_pos = 1;

      size_t o_task = find_task(0, events, true);
      size_t b_task = find_task(0, events, false);

      size_t res = 0;
      while (o_task != -1 || b_task != -1)
      {
         if (o_task == b_task)
         {
            throw "fail";
         }


         if (o_task < b_task)
         {
            size_t o_time = abs(o_pos - events[o_task].second) + 1;
            res += o_time;
            o_pos = events[o_task].second;

            if (b_task != -1)
            {
               size_t b_time = abs(b_pos - events[b_task].second);
               if (b_time <= o_time)
                  b_pos = events[b_task].second;
               else
                  b_pos += o_time * (b_pos < events[b_task].second ? 1 : -1);
            }

            o_task = find_task(o_task + 1, events, true);
         }
         else
         {
            size_t b_time = abs(b_pos - events[b_task].second) + 1;
            res += b_time;
            b_pos = events[b_task].second;

            if (o_task != -1)
            {
               size_t o_time = abs(o_pos - events[o_task].second);
               if (o_time <= b_time)
                  o_pos = events[o_task].second;
               else
                  o_pos += b_time * (o_pos < events[o_task].second ? 1 : -1);
            }

            b_task = find_task(b_task + 1, events, false);
         }
      }


      std::cout << "Case #" << tc << ": " << res << std::endl;
   }

   return 0;
}

