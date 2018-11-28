#include <iostream>
#include <iomanip>
#include <set>
#include <vector>

typedef std::vector <std::string> path; 
typedef std::set <path> paths;

void read_path (paths &ps)
{
   std::string s;
   getline (std::cin, s);
   path p;
   for (size_t i = 0; i < s.size (); ++i)
      if (s [i] == '/')
      {
//         if (!p.empty ()) std::cout << "dir: " << p.back () << std::endl;
         ps.insert (p);
         p.push_back ("");
      }
      else
         p.back () += s [i];

//   if (!p.empty ()) std::cout << "dir: " << p.back () << std::endl;
   ps.insert (p);
}

int main ()
{
   int T;
   std::cin >> T;
   for (int i = 1; i <=T; ++i)
   {
      int N, M;
      std::cin >> N >> M >> std::ws;
      paths ps;
      ps.insert (path ());
      for (int j = 0; j < N; ++j)
         read_path (ps);

      int were = ps.size ();
//      std::cout << "were: " << were << std::endl;
      for (int j = 0; j < M; ++j)
         read_path (ps);
       
      std::cout << "Case #" << i << ": " << (ps.size() - were) << std::endl;
   }
}
