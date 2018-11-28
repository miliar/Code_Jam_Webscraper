#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <fstream>

using namespace std;
int main(void)
{
  int t;
  size_t size = 101;
  char *str;
  char map[] = {"yhesocvxduiglbkrztnwjpfmaq"};
  str = (char*)malloc(101*sizeof(char));
  int j=1;
  ifstream ifs("A-small-attempt1.in");
  ofstream ofs("output.txt");
  ifs.getline(str, 101, '\n');
  t = atoi(str);
  while(j<=t)
  {
//     gets(str);
    ifs.getline(str, 101, '\n');
    ofs<<"Case #"<<j<<": ";
    for(int i=0;i<strlen(str);i++)
    {
      if(str[i]==' ')
	ofs<<' ';
      else if(str[i]=='\n');
      else
	ofs<<(map[str[i]-97]);
      
	
    }
    ofs<<'\n';
    j++;
  }
  return 0;
}