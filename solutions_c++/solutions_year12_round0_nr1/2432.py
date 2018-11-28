#include "stdafx.h"
#include <iostream>

int main()
{ char str[200];
  char map[] = "yhesocvxduiglbkrztnwjpfmaq";
  int i, c;
  freopen( "input.txt", "r", stdin );
  freopen( "output.txt", "w", stdout );
  scanf("%d\n", &i);  
  for(int j=1; j<=i; ++j)
  {std::cin.getline(str, 200);
   for(int k=0; k<strlen(str); ++k)
	   str[k] = str[k]==' ' ? ' ' : map[str[k]-'a'];
   std::cout << "Case #" << j << ": " << str << std::endl;   
  }  
  return 0;
}
