#include <vector>
#include <map>
#include <set>
#include <list>
#include <fstream>
#include <string>
#include <iostream>
#include <sstream>
#include <limits>
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

std::map<char, char> trans{
   {'a', 'y'}, {'b', 'h'}, {'c', 'e'}, {'d', 's'}, {'e', 'o'}, {'f', 'c'},
   {'g', 'v'}, {'h', 'x'}, {'i', 'd'}, {'j', 'u'}, {'k', 'i'}, {'l', 'g'},
   {'m', 'l'}, {'n', 'b'}, {'o', 'k'}, {'p', 'r'}, {'q', 'z'}, {'r', 't'},
   {'s', 'n'}, {'t', 'w'}, {'u', 'j'}, {'v', 'p'}, {'w', 'f'}, {'x', 'm'},
   {'y', 'a'}, {'z', 'q'}};

void train() {
   std::ifstream ifs("a.sample.in"), // Sample taken from GCJ website
                 ofs("a.sample.out");
   std::map<char, char> m;
   char i, o;
   while (ifs.get(i) && ofs.get(o)) {
      if (std::isalpha(i)) {
         m[i] = o;
      }
   }
   std::cout << "{";
   for (auto p : m) {
      std::cout << "{'" << p.first << "', '" << p.second << "'}, ";
   }
   std::cout << "};" << std::endl << std::endl << std::endl;
   std::cout << "REVERSED: " << std::endl;
   std::map<char, char> n;
   for (auto p : m) {
      n[p.second] = p.first;
   }
   for (auto p : n) {
      std::cout << "{'" << p.first << "', '" << p.second << "'}" << std::endl;
   }
   // Notice after running : Missing keys q and z ; Missing values q and z
   // Using the comment <<'a' -> 'y', 'o' -> 'e', and 'z' -> 'q'>> ; the table
   // is filled up by hand !
}

int main(int argc, char**)
{
   if (argc == 2) { // Training
      train();
      return 0;
   }
   int T = read<int>();
   for (int i = 1 ; i <= T ; ++i) {
      std::cout << "Case #" << i << ": ";
      std::string S = readLine();
      for (char c : S) {
         if (std::isalpha(c)) {
            std::cout.put(trans[c]);
         } else {
            std::cout.put(c);
         }
      }
      std::cout << std::endl;
   }
}
