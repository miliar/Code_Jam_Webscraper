#include <stdafx.h>

#include <algorithm>
#include <fstream>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <assert.h>

using namespace std;

#undef min
#undef max
int min(int a, int b) { return a < b ? a : b; }
int max(int a, int b) { return a > b ? a : b; }

//vector<int> v;
//for(vector<int>::iterator it = v.begin(), end = v.end(); it != end; ++it)
//{
//}

void Solve()
{
   ifstream input("input.txt");
   ofstream output("output.txt");

   int testCount = 0;
   input >> testCount;
   string rowt;
   getline(input, rowt);

   for (int i = 0; i < testCount; ++i)
   {
      string row;
      getline(input, row);

      map<char, char> dictionary;
      dictionary.insert(make_pair(' ', ' '));
      dictionary.insert(make_pair('a', 'y'));
      dictionary.insert(make_pair('b', 'h'));
      dictionary.insert(make_pair('c', 'e'));
      dictionary.insert(make_pair('d', 's'));
      dictionary.insert(make_pair('e', 'o'));
      dictionary.insert(make_pair('f', 'c'));
      dictionary.insert(make_pair('g', 'v'));
      dictionary.insert(make_pair('h', 'x'));
      dictionary.insert(make_pair('i', 'd'));
      dictionary.insert(make_pair('j', 'u'));
      dictionary.insert(make_pair('k', 'i'));
      dictionary.insert(make_pair('l', 'g'));
      dictionary.insert(make_pair('m', 'l'));
      dictionary.insert(make_pair('n', 'b'));
      dictionary.insert(make_pair('o', 'k'));
      dictionary.insert(make_pair('p', 'r'));
      dictionary.insert(make_pair('q', 'z'));
      dictionary.insert(make_pair('r', 't'));
      dictionary.insert(make_pair('s', 'n'));
      dictionary.insert(make_pair('t', 'w'));
      dictionary.insert(make_pair('u', 'j'));
      dictionary.insert(make_pair('v', 'p'));
      dictionary.insert(make_pair('w', 'f'));
      dictionary.insert(make_pair('x', 'm'));
      dictionary.insert(make_pair('y', 'a'));
      dictionary.insert(make_pair('z', 'q'));

      output << "Case #" << i+1 << ": ";	
         for (int j = 0; j < row.length(); ++j)
         {
            if (dictionary.find(row[j]) == dictionary.end())
            {
               assert(false);
            }
            output << dictionary[row[j]];
         }
         output << "\n";
   }
}
