#include <iostream>
#include <vector>

struct vine_t
{
   vine_t()
      : d(0)
      , l(0)
      , max_l(0)
   {}

   size_t d;
   size_t l;
   size_t max_l;
};

size_t intersect(vine_t const & a, vine_t const & b)
{
   return std::min(b.l, b.d - a.d);
}

void update(size_t l, std::vector<vine_t> & vines)
{
   for (size_t t = l + 1; t != vines.size(); ++t)
   {
      if (vines[l].d + vines[l].max_l < vines[t].d)
         return;

      vines[t].max_l = std::max(vines[t].max_l, intersect(vines[l], vines[t]));
   }
}

bool process(std::vector<vine_t> & vines, size_t D)
{
   vines[0].max_l = vines[0].d;

   for (size_t l = 0; l != vines.size(); ++l)
   {
      if (vines[l].max_l && vines[l].d + vines[l].max_l >= D)
         return true;

      update(l, vines);
   }

   return false;
}

int main(int argc, char * argv[])
{
   size_t T = 0;
   std::cin >> T;

   for (size_t x = 0; x != T; ++x)
   {
      size_t N = 0;
      std::cin >> N;
      std::vector<vine_t> vines(N);
      for (size_t l = 0; l != N; ++l)
         std::cin >> vines[l].d >> vines[l].l;

      size_t D = 0;
      std::cin >> D;

      std::cout << "Case #" << x + 1 << ": " << (process(vines, D) ? "YES" : "NO") << std::endl;
   }
}
