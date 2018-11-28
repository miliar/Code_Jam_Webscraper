#include<iostream>
#include<sstream>
using namespace std;

string ToString(int n)
{
      stringstream s;
      s << n;
      return s.str();
}

int main()
{
   char mapper[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

  int num_test =0;
  cin>>num_test;
  cin.ignore(1000,'\n');
  string input;
  int index = 0;
  int testCaseIndex =0;
  string output;

   while(++testCaseIndex <= num_test)
   {
       index = 0;
       getline(cin,input);
       output += "Case #" + ToString(testCaseIndex)  +": ";
       while(input[index] != '\0')
       {
           if( input[index] == ' ')
               output+= input[index];
           else
               output+= mapper[input[index] - 'a'];

           index++;
       }
       output += "\n";
   }
  cout<<output;
   return 0;
}

