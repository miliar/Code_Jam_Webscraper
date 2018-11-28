#include <iostream>
#include <string>
using namespace std;


const string phrase = "welcome to code jam";
//const string phrase = "helol";
const string::size_type phrase_len = phrase.length();

string line;
string::size_type line_len;

int faind(string::size_type ppos, string::size_type offset)
{
  if( ppos >= phrase_len )
    return 1;

  int matches = 0;
  int count;
  for( string::size_type i=offset; i<line_len; ++i )
  {
    if( line[i] == phrase[ppos] )
      matches += faind(ppos+1, i+1);
    /*
    if( line[i] == phrase[ppos] )
    {
      int j = i+1;
      while( line[j] == phrase[ppos] && j<line_len )
        ++j;
      count = j-i;
      matches += count*faind(ppos+1, i);
    }
    */
  }
  matches = matches % 1000;
  return matches;
}

int main()
{
  int N;
  cin >> N;
  getline(cin, line);
  for( int i=1; i<=N; ++i )
  {
    getline(cin, line);
    line_len = line.length();
    printf("Case #%i: %.4i\n", i, faind(0, 0));
  }

  return 0;
}
