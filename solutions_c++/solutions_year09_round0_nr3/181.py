#include <vector>
#include <string>
#include <iostream>
#include <iomanip>

using namespace std;

long compute(string const &phrase, string const &text)
{
  vector<long> count(text.length(), 1), ncount(text.length());
  size_t last_letter = 0;
  while ( last_letter < phrase.length() )
  {
    for ( size_t i=0; i<text.length(); ++i )
    {
      long prev;
      if ( i > 0 )
      {
        ncount[i] = ncount[i - 1];
        prev = count[i - 1];
      }
      else
      {
        prev = last_letter == 0;
        ncount[0] = 0;
      }
      if ( text[i] == phrase[last_letter] )
        ncount[i] = (ncount[i] + prev) % 10000;
    }
    ncount.swap(count);
    ++last_letter;
  }
  return count[count.size() - 1] % 10000;
}

int main()
{
  string phrase("welcome to code jam");
  int N;
  cin >> N;
  string text;
  getline(cin, text);
  for ( int n=1; n<=N; ++n )
  {
    getline(cin, text);
    long res = compute(phrase, text);
    cout << "Case #" << n << ": " << setfill('0') << setw(4) << res << endl;
  }
  return 0;
}
