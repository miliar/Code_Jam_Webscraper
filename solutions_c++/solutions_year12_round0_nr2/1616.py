#include <iostream>
#include <limits>
#include <string>

//{{{ Predefined functions : read<T>() and readLine(bool newLine = true)
bool read_LastReadWasLine = true;
template <typename T>
T read() {
    T t;
    std::cin >> t;
    read_LastReadWasLine = false;
    return t;
}
std::string readLine(bool newLine = true) {
    std::string s;
    if (newLine && !read_LastReadWasLine) {
        std::cin.ignore(std::numeric_limits<int>::max(), '\n');
    }
    std::getline(std::cin, s);
    read_LastReadWasLine = true;
    return s;
}
//}}}

void Case() {
   int N = read<int>();
   int S = read<int>();
   int p = read<int>();

   int res = 0;
   for (int i = 0 ; i < N ; ++i) {
      int t = read<int>();
      int best_not_surprising = (t + 2) / 3;
      if (best_not_surprising >= p) {
         ++res;
      } else if (S > 0 && t >= 2 && t <= 28) {
         int best_surprising = (t + 4) / 3;
         if (best_surprising >= p) {
            --S;
            ++res;
         }
      }
   }
   std::cout << res;
}

int main(int, char**)
{
   int T = read<int>();
   for (int i = 1 ; i <= T ; ++i) {
      std::cout << "Case #" << i << ": ";
      Case();
      std::cout << std::endl;
   }
}
