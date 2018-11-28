#include <iostream>
#include <map>
#include <string>
using namespace std;
typedef map<char,char> Dict;
typedef pair<char,char> Rule;

void SetupDict(Dict& myDict)
{
  myDict.insert(Rule('y','a'));
  myDict.insert(Rule('n','b'));
  myDict.insert(Rule('f','c'));
  myDict.insert(Rule('i','d'));
  myDict.insert(Rule('c','e'));
  myDict.insert(Rule('w','f'));
  myDict.insert(Rule('l','g'));
  myDict.insert(Rule('b','h'));
  myDict.insert(Rule('k','i'));
  myDict.insert(Rule('u','j'));
  myDict.insert(Rule('o','k'));
  myDict.insert(Rule('m','l'));
  myDict.insert(Rule('x','m'));  
  myDict.insert(Rule('s','n'));
  myDict.insert(Rule('e','o'));  
  myDict.insert(Rule('v','p'));
  myDict.insert(Rule('z','q'));
  myDict.insert(Rule('p','r'));  
  myDict.insert(Rule('d','s'));  
  myDict.insert(Rule('r','t'));
  myDict.insert(Rule('j','u'));  
  myDict.insert(Rule('g','v'));  
  myDict.insert(Rule('t','w'));
  myDict.insert(Rule('h','x'));
  myDict.insert(Rule('a','y'));
  myDict.insert(Rule('q','z'));
}

string Translate(const string input, const Dict myDict)
{
   string output;
   for(unsigned int i=0;i<input.length();i++)
   {
	   Dict::const_iterator it = myDict.find(input[i]);
	   if(it != myDict.end())
		   output.append(1,it->second);   
	   else
	       output.append(1,input[i]);
   }
   return output;
}

int main()
{  
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small-out.txt","wt",stdout);
    Dict myDict;
    SetupDict(myDict);
    int num = 0;
    char lines[256];
    cin >> num;
	cin.ignore(1);
    for(int i=0;i<num;i++)
    {
       cin.getline(lines,256);
       string myString(lines);
	   cout << "Case #" << i+1 << ": " << Translate(myString,myDict) << endl;
    }
}