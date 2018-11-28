#include <iostream>
#include <string>
#include <map>

using namespace std;

void output(int useCase, string result)
{
   cout<<"Case #"<<useCase<<": "<<result<<endl;
}

int main()
{
   map<char,char> chars;
   chars.insert(pair<char,char>('a', 'y'));
   chars.insert(pair<char,char>('b', 'h'));
   chars.insert(pair<char,char>('c', 'e'));
   chars.insert(pair<char,char>('d', 's'));
   chars.insert(pair<char,char>('e', 'o'));
   chars.insert(pair<char,char>('f', 'c'));
   chars.insert(pair<char,char>('g', 'v'));
   chars.insert(pair<char,char>('h', 'x'));
   chars.insert(pair<char,char>('n', 'b'));
   chars.insert(pair<char,char>('o', 'k'));
   chars.insert(pair<char,char>('l', 'g'));
   chars.insert(pair<char,char>('m', 'l'));
   chars.insert(pair<char,char>('j', 'u'));
   chars.insert(pair<char,char>('k', 'i'));
   chars.insert(pair<char,char>('i', 'd'));
   chars.insert(pair<char,char>('w', 'f'));
   chars.insert(pair<char,char>('v', 'p'));
   chars.insert(pair<char,char>('u', 'j'));
   chars.insert(pair<char,char>('t', 'w'));
   chars.insert(pair<char,char>('s', 'n'));
   chars.insert(pair<char,char>('r', 't'));
   chars.insert(pair<char,char>('p', 'r'));
   chars.insert(pair<char,char>('y', 'a'));
   chars.insert(pair<char,char>('x', 'm'));
   chars.insert(pair<char,char>('q', 'z'));
   chars.insert(pair<char,char>('z', 'q'));
   chars.insert(pair<char,char>(' ', ' '));
   int useCasesNumber;
   cin>>useCasesNumber;
   string input;
   int i = 1;
   getline(cin, input, '\n');
   while(getline(cin, input, '\n'))
   {
      string result;
      for (unsigned int j = 0; j < input.length(); ++j)
      {
         result += chars.find(input[j])->second;
      }
      output(i++, result);
   }
   return 0;
}
