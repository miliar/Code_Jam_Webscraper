#include <string>
#include <iostream>
#include <cstdlib>

using namespace std;

// starts on 97 and finishes in 122
static const char map[] = {
  'y',
  'h',
  'e',
  's',
  'o',
  'c',
  'v',
  'x',
  'd',
  'u',
  'i',
  'g',
  'l',
  'b',
  'k',
  'r',
  'z',
  't',
  'n',
  'w',
  'j',
  'p',
  'f',
  'm',
  'a',
  'q'
};

static int offset(97), linesize(256);

char getMappedChar(char symbol)
{
  // space char
  if (symbol == 32) 
    return symbol;

  // FIXME: according to the exercise it's impossible to have values out of range a-z
  return map[symbol - offset];
}

string getTranslatedString(const string &input)
{
  int inputSize(input.length());
  string output;
  output.reserve(inputSize);
  for (int i(0); i < inputSize; i++) {
    output += getMappedChar(input[i]);
  }
  return output;
}

int main(int argc, char **argv)
{
  char line[linesize];

  cin.getline(line,linesize);

  int numOfTests(atoi(line));
  
  for (int i(1); i <= numOfTests; i++) {
    cin.getline(line,linesize);
    cout << "Case #" << i << ": " << getTranslatedString(line) << endl;
  }

  return 0;
}
