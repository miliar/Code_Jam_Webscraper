#include <algorithm>
#include <iostream>
#include <limits>
#include <set>
#include <sstream>
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

std::set<std::pair<int, int>> viewed;

std::string itos(int i) {
   std::ostringstream oss;
   oss << i;
   return oss.str();
}

std::string rotate(std::string s, std::size_t i) {
   std::rotate(s.begin(), std::next(s.begin(), i), s.end());
   return s;
}

int NumRecycled(int n, int B) {
   std::string I = itos(n);
   int res = 0;
   for (std::size_t r = 0 ; r < I.size() ; ++r) {
      int m = std::stoi(rotate(I, r));
      if (n < m && m <= B && viewed.find({n, m}) == viewed.end()) {
         ++res;
         viewed.insert({n, m});
      }
   }
   return res;
}

void Case() {
   int A = read<int>();
   int B = read<int>();

   viewed = {};
   int res = 0;
   for (int i = A ; i < B ; ++i) {
      res += NumRecycled(i, B);
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
