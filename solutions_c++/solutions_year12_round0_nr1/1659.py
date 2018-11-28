#include <iostream>
#include <fstream>
#include <string>

#include <libgen.h>
#include <stdlib.h>
#include <unistd.h>

using namespace std;

#define ALPHABET_SIZE 26

char GOOGLERESE[] = {'y','b','c','d','e','f','g','h','i','j','k','l','m','n','e','p','q','r','s','t','u','v','w','x','y','q'};

string getExecutablePath() {
  char buffer[BUFSIZ] = {0};
  readlink("/proc/self/exe", buffer, BUFSIZ);
  return dirname(buffer);
}

void buildGooglerese() {
  const char* sampleInput[] = {
    "ejp mysljylc kd kxveddknmc re jsicpdrysi",
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
    "de kr kd eoya kw aej tysr re ujdr lkgc jv",
    NULL
  };

  const char* sampleOutput[] = {
    "our language is impossible to understand",
    "there are twenty six factorial possibilities",
    "so it is okay if you want to just give up",
    NULL
  };
  
  int i = 0;
  while (sampleInput[i] != NULL) {
    const char* inputStr = sampleInput[i];
    const char* outputStr = sampleOutput[i];
    int j = 0;

    while (inputStr[j] != '\0') {
      char inputChar = inputStr[j];
      char outputChar = outputStr[j];
      
      if (inputChar != ' ') {
        GOOGLERESE[(inputChar - 'a')] = outputChar;
      }
      
      j++;
    }

    i++;
  }

  char missingChar = '\0';

  for (int i = 0; i < ALPHABET_SIZE; i++) {
    bool found = false;

    for (int j = 0; j < ALPHABET_SIZE; j++) {
      if (('a' + i) == GOOGLERESE[j]) {
        found = true;
        break;
      }
    }

    if (!found) {
      missingChar = 'a' + i;
    }
  }

  for (int i = 0; i < ALPHABET_SIZE; i++) {
    if (('a' + i) == GOOGLERESE[i]) {
      GOOGLERESE[i] = missingChar;
    }
  }

}

int main(int argc, char **argv) {
  int lineCount = 0;
  int caseTotal = 0;
  int caseCount = 0;
  string inputFile = getExecutablePath() + "/../input/A-small.in";
  ifstream file (inputFile.c_str());

  buildGooglerese();

  if (file.is_open()) {
    while (file.good()) {
      string line;
      getline (file, line);
      lineCount++;
      if (lineCount == 1) {
        caseTotal = atoi(line.c_str());
        continue;
      }
      
      if (caseCount < caseTotal) {
        for (int i = 0; i < line.length(); i++) {
          char c = line[i];
          if (c != ' ') {
            line.replace(i, 1, 1, GOOGLERESE[(c-'a')]);
          }
        }
        
        cout  << "Case #" << caseCount+1 << ": " << line << endl;
        caseCount++;
      }
      else {
        break;
      }
    }

    file.close();
  }

  return 0;
}

