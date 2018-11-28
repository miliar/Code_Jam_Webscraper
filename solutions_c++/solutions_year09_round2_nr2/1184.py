#include<iostream>
#include<string>
#include<vector>
#include<fstream>
#include<algorithm>
#include<math.h>
#include<time.h>
#include<conio.h>
using namespace std;

#define f(i,x) for(int i = 0; i < x; i++)

ifstream in("B-large.in");
ofstream out("p2.out");

bool sorted(string str)
{
     bool sd = true;
     f(i,str.length()-1)
     {
         if (str[i] >= str[i+1]) continue;
         sd = false;
         break;    
     }
     return sd;
}

string reverse(string str)
{
    string to_return = "";
    f(i,str.length())
    {
      to_return = str[i] + to_return;
    }       
    return to_return;
}

string gF(string str)
{
    f(i,str.length()) {
     if (str[i] == '0') continue;
     char temp = str[i];
     str[i] = str[0];
     str[0] = temp;
     break;                 
    }      
    return str; 
}

string gN(string str)
{
       if (sorted(str)) {
          str = reverse(str); str = "0" + str; str = gF(str);
          return str;              
       } else { 
           next_permutation(str.begin(),str.end());   
           return str;
       }
}

int main()
{
    int cases, temp;
    string tempstr;
    in >> cases;

    f(i,cases)
    {   
        in >> tempstr;
        out << "Case #" << i + 1 << ": " << gN(tempstr) << endl;
    }
    return 0;   
}
