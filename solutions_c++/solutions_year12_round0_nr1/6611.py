#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

char translation[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

char replace(char c1)
{
  if (c1 == ' ')
    {
      return ' ';
    }

  int index = c1 - 'a';
  return translation[index];
}

std::string replaceLine(const std::string &line)
{
  std::string replacedLine;
  for (int charIndex = 0; charIndex < line.length(); ++charIndex)
    {
      replacedLine += replace(line[charIndex]);
    }
  return replacedLine;
}

bool stringToInteger(const std::string &str, int &integer)
{
  std::istringstream iss(str);
  return !(iss >> std::dec >> integer).fail();
}


int main(int argc, char *argv[])
{
  std::ifstream input;
  input.open(argv[1]);

  std::ofstream output;
  output.open("a.out");

  int numCases = 0;
  char buffer[200];
  int caseIndex = 0;
  while (input.good())
  {      
      input.getline(buffer, 200);

      std::string line = buffer;
      if (numCases == 0)
	{
	  stringToInteger(line, numCases);
	}
      else
	{
	  if (caseIndex == numCases)
	    {
	      break;
	    }

	  output << "Case #" << (caseIndex + 1) << ": " << replaceLine(line) << "\n";
	  ++caseIndex;
	}
    }

  output.flush();
}
