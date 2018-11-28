#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <map>
#include <iostream>
#include <string>

typedef std::map<char,char> CharMap;
typedef std::map<char,char>::iterator CharMapIter;
int main()
{
  char strEncr[]="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
  char strStr[]= "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
  CharMap chMap;
  for(int i=0;i<strlen(strEncr);++i)
    {
      chMap.insert(std::pair<char,char>(strEncr[i],strStr[i]));
    }
  chMap.insert(std::pair<char,char>('q','z'));
  chMap.insert(std::pair<char,char>('z','q'));
  CharMapIter chIter=chMap.begin();
  // while(chIter!=chMap.end())
  //   {
  //     std::cout << chIter->first << " " << chIter->second << "\t"; 
  //     ++chIter;
  //   }
  // std::cout << std::endl;
  int nTestCases;
  std::string str;
  std::getline (std::cin,str);
  nTestCases=atoi(str.c_str());
  for (int i=0;i<nTestCases;++i)
    {
      char outStr[1010];
      int outLen=0;
      std::string str;
      std::getline (std::cin,str);
      for(int j=0;j<str.length();++j)
	{
	  outStr[j]=chMap[str[j]];
	}
      outStr[str.length()]='\0';
      printf("Case #%d: %s\n",i+1,outStr);
    }
  return 0;
}
