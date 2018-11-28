#include <iostream>
#include <cstring>
#include <cstdlib>

using namespace std;

char Conv(char c)
{
char list [26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
if(c-97 >= 0 && c-97 <= 25)
return list[c-97];   
else
  return c;
 
   
}

void sent(char * line)
{
  int index = 0 ;
 while (line[index] != '\0')
 {
  line[index] = Conv(line[index]); 
   index++;
 }
  
}

int main()
{
  
  int cases;
  char * line = new char[150];
  cin >> cases;
  cin.ignore();
  for(int k = 0 ; k < cases ; k++)
  {
    int max =0;
    int min = 0;
    cin.getline(line,150);
    sent(line);
   cout << "Case #" << k+1 << ": "<<  line<< endl; 
    
  }
 return 0; 
}