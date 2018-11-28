#include <cstdio>
#include <cstdlib>
#include <vector>
#include <map>
#include <math.h>
using namespace std;

int factorial (int a)
{
  if (a > 1)
   return (a * factorial (a-1));
  else
   return (1);
}


int convert_to_base(int actual_number, int base, int **number)
{
  long long size;
 
	return (int)size;
}

int main(int argc, const char *argv[])
{
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int T; //Number of cases
	std::vector<int> bases;
	std::vector<int> basesResult;

	scanf("%d\n", &T);
	for (int i = 0; i < T; i++) {
    long long result = 0; // the ans
    char* input = new char[62];
    std::map<char, int> charMap;
    int startBase = 0;
    
    scanf("%s\n", input);

    bool zero = false;
    int curr = 1;
    for (int j = 0; j < strlen(input); j++) {
      map<char, int>::iterator it;
      if (j == 0) {
        charMap[input[j]] = curr++;
      }
      else
      {
        it=charMap.find(input[j]);
        if (it == charMap.end()) {
          if (!zero) {
            zero = true;
          }
          else
          {
            charMap[input[j]] = curr++;
          }
        }
        else
        {
        }
      }
      printf("", charMap[input[j]], input[j]);
    }

    startBase = (charMap.size()==1)? 2: (int)charMap.size();

    //printf("startBase:%d\n", startBase);

    for (int j = 0; j < strlen(input); j++) {
      int mul = (int)(pow(startBase, strlen(input)-j-1));
      //printf("j:%d %d %d\n", j, charMap[input[j]], mul);
      result += charMap[input[j]] * mul;
    }
		
		printf("Case #%d: %ld\n", i+1, result);
	}
	
	return 0;
}

