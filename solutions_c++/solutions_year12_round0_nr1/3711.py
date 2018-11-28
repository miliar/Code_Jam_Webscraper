/* 
 * Problem A. Speaking in Tongues
 *  Google Code.jam 2012
 *  George Vafiadis
 *  gvafiadis@gmail.com
 */

#include <iostream>
#include <cstdlib>
using namespace std;

#define NUM_CHARS 101

int main(int argc, char **argv)
{
  int T;
  char buffer[NUM_CHARS];
  char result[NUM_CHARS];
  const char * mapper = "yhesocvxduiglbkrztnwjpfmaq";
  
  cin.getline(buffer, NUM_CHARS, '\n');

  T = atoi(buffer);

  for(int test = 0; test < T; ++test)
    {   
      cin.getline(buffer, NUM_CHARS, '\n');
      char * s = buffer;
      char * r = result;
       
      while( *s )
	{
          if( *s == ' ' ) *r = ' ';
          else            *r = mapper[*s - 'a'];
          ++s;
          ++r;
        }
  
      *r = '\0';

      cout << "Case #" << (test+1) << ": "  << result << endl; 
    }      
 
  return 0;
}
