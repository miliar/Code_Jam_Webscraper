#include <cstdio>
#include <cstdlib>
#include <vector>
#include <map>
using namespace std;

int main(int argc, const char *argv[])
{
  //freopen("A-small-attempt0.in", "r", stdin);
  //freopen("output.txt", "w", stdout);
  int L; //every word consists of exactly L lowercase letters
  int D; //exactly D words in this language
  int N; //number of test case
  std::vector<char*> alienLangLst;

  scanf("%d %d %d\n", &L, &D, &N);
  for (int i = 0; i < D; i++) {
    char* input = new char[L+1];
    scanf("%s\n", input);
    alienLangLst.push_back(input);
  }

  for (int i = 0; i < N; i++) {
    int K = 0;
    char* pattern = new char[10240];
    scanf("%s\n", pattern);
    vector<char*> tokens;
    for (int j = 0; j < strlen(pattern); j++)
    {
      char* buffer = new char[strlen(pattern)];
      if (pattern[j] != '(')
      {
        buffer[0] = pattern[j];
        buffer[1] = 0;
      }
      else
      {
        int index = 0;
        while (pattern[++j] != ')')
        {
          buffer[index++] = pattern[j];
        }
        buffer[index] = 0;
      }
      //printf("\tBuffer::%s\n", buffer);
      tokens.push_back(buffer);
    }

    //calc
    for (vector<char*>::iterator it = alienLangLst.begin(); it!=alienLangLst.end(); ++it) {
      char* alienLang = *it;
      for (int j = 0; j < strlen(alienLang); j++) {
        if (strchr(tokens[j], alienLang[j]) != NULL)
        {
          //printf("%s", alienLang[j]);
          if (j == strlen(alienLang)-1) {
            K++;
            //printf("\n");
          }
        }
        else
          break;
      }
    }

    printf("Case #%d: %d\n", i+1, K);
  }

  return 0;
}
