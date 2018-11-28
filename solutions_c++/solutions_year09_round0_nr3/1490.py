// AlienLanguage.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

char searchString[] = "welcome to code jam";
int sequenceCount = sizeof(searchString)-1;

int main(int argc, char* argv[])
{
  int N;
  std::cin >> N;
  char c;
  do
  {
    if(scanf("%c", &c)!=1)
      break;
  } while(c != '\n');
  for(int i = 0; i < N; ++i)
  {
    std::string line;
    do
    {
      if(scanf("%c", &c)!=1)
        break;
      line += c;
    } while(c != '\n');
    std::vector<int> counts(sequenceCount, 0);
    for(int j = line.size()-1; j >= 0; --j)
    {
      for(int k = 0; k < sequenceCount; ++k)
      {
        if(searchString[k] == line[j])
        {
          counts[k] = ((k+1==sequenceCount)?(counts[k]+1):(counts[k]+counts[k+1]))%10000;
        }
      }
    }
    char res[5];
    sprintf(res, "%04d", counts[0]);
    std::cout << "Case #" << (i+1) << ": " << res << "\n";
  }
	return 0;
}

