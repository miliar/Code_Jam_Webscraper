#include <iostream>
#include <vector>

typedef long long int64;

struct Roller
{
   struct Node
   {
      Node() { next = -1; sales = 0; }
      int   next;
      int64 sales;
      bool  has_next() { return next != -1; }
   };

   int   cycle_start;
   int   cycle_len;
   int64 cycle_sales;

   int R;
   int N;
   int k;
   std::vector<int> group_sizes;
   std::vector<Node> nodes;

   void read_input()
   {
      std::cin >> R >> k >> N;
      group_sizes.resize(N);
      nodes.resize(N);
      for (int n = 0; n < N; ++n)
         std::cin >> group_sizes[n];
   }

   void find_next(const int i, int& j, int64& ppl)
   {
      ppl = 0;
      j = i;
      while (group_sizes[j] + ppl <= k)
      {
         ppl += group_sizes[j];
         j = (j+1)%N;

         if (j == i)
            break;
      }         
   }

   void find_cycle(const int i)
   {
      cycle_len = 0;
      cycle_sales = 0;
      int cur = i;
      do
      {
         cycle_sales += nodes[cur].sales;
         cycle_len++;
         cur = nodes[cur].next;
      }
      while (cur != i);

/*      std::cout << "found cycle  at"
                << i
                << " val = "
                << cycle_sales
                << std::endl;*/
   }

   void build_graph(const int i)
   {
      if (nodes[i].has_next())
      {
         cycle_start = i;
         find_cycle(i);
      }
      else
      {
         find_next(i, nodes[i].next, nodes[i].sales);
/*         std::cout << "next to " 
                   << i
                   << " is "
                   << nodes[i].next 
                   << " val = "
                   << nodes[i].sales
                   << std::endl;*/
         build_graph(nodes[i].next);
      }
   }
   
   void build_graph()
   {
      build_graph(0);
   }
   
   int64 find_sales()
   {
      build_graph();

      int64 sales = 0;
      int i = 0;

      while (i != cycle_start && R > 0)
      {
         sales += nodes[i].sales;
         i = nodes[i].next;
         R--;
      }

      sales += (R / cycle_len) * cycle_sales;
      
      for (int r = 0; r < R % cycle_len; ++r)
      {
         sales += nodes[i].sales;
         i = nodes[i].next;
      }

      return sales;         
   }   
};

int main()
{
   int T; std::cin >> T;
   
   for (int t = 0; t < T; ++t)
   {
      Roller r;
      r.read_input();
      std::cout << "Case #" << (t+1) << ": "
                << r.find_sales() << std::endl;
   }   
}


