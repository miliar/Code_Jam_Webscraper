#include <iostream>
#include <map>
#include <string>
#include <sstream>

int main()
{
   std::map<char, char> googlerese;

   googlerese.insert(std::pair<char, char>('a', 'y'));
   googlerese.insert(std::pair<char, char>('b', 'h'));
   googlerese.insert(std::pair<char, char>('c', 'e'));
   googlerese.insert(std::pair<char, char>('d', 's'));
   googlerese.insert(std::pair<char, char>('e', 'o'));
   googlerese.insert(std::pair<char, char>('f', 'c'));
   googlerese.insert(std::pair<char, char>('g', 'v'));
   googlerese.insert(std::pair<char, char>('h', 'x'));
   googlerese.insert(std::pair<char, char>('i', 'd'));
   googlerese.insert(std::pair<char, char>('j', 'u'));
   googlerese.insert(std::pair<char, char>('k', 'i'));
   googlerese.insert(std::pair<char, char>('l', 'g'));
   googlerese.insert(std::pair<char, char>('m', 'l'));
   googlerese.insert(std::pair<char, char>('n', 'b'));
   googlerese.insert(std::pair<char, char>('o', 'k'));
   googlerese.insert(std::pair<char, char>('p', 'r'));
   googlerese.insert(std::pair<char, char>('q', 'z'));
   googlerese.insert(std::pair<char, char>('r', 't'));
   googlerese.insert(std::pair<char, char>('s', 'n'));
   googlerese.insert(std::pair<char, char>('t', 'w'));
   googlerese.insert(std::pair<char, char>('u', 'j'));
   googlerese.insert(std::pair<char, char>('v', 'p'));
   googlerese.insert(std::pair<char, char>('w', 'f'));
   googlerese.insert(std::pair<char, char>('x', 'm'));
   googlerese.insert(std::pair<char, char>('y', 'a'));
   googlerese.insert(std::pair<char, char>('z', 'q'));
   googlerese.insert(std::pair<char, char>(' ', ' '));

   int tests = 0, currTest = 0;

   std::cin >> tests;
   std::string currLine;
   std::getline(std::cin, currLine);

   while (currTest < tests + 1)
   {
      if (currTest != 0)
      {
         std::string outputLine;
         std::stringstream s;

         s << currTest;

         std::getline(std::cin, currLine);
         outputLine += "Case #" + s.str();
         outputLine += ": ";

         for (int i = 0; i < currLine.length(); i++)
         {
            outputLine += googlerese.at(currLine.at(i));
         }

         std::cout << outputLine << "\n";
      }

      currTest++;
   }

   return 0;
}