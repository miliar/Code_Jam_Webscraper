#include <iostream>
#include <vector>
#include <assert.h>
#include <string.h>

#define DEBUG 0
#define SIZE 1024

using namespace std;

const char wcj[] = "welcome to code jam";

long long count(const char* s)
{
  vector<vector<long long> > c(sizeof(wcj)+1, vector<long long>(503, -1));

  if(DEBUG)
    cout << "count s = '" << s << "' length: " << strlen(s) << " wcj len: " << strlen(wcj) << "\n";
  // c[a][b] is the number of ways wcj[a:] appears as a subsequence of
  // s[b:].


  // First count how many times the last character in wcj (i.e., 'm')
  // appear in s[b:].
  for(int b = 0; b <= strlen(s)+1; b++) {
    long long count = 0;
    int a = strlen(wcj) - 1;
    for(int i = b; i < strlen(s); i++) {
      if(wcj[a] == s[i])
	count++;
    }

    if(DEBUG)
      cout << "c[" << a << "][" << b << "]: " << count << endl;
    c[a][b] = count;
    c[a+1][b] = 0;
  }

  if(DEBUG)
    cout << "B\n";

  // wcj[a:] occurs zero times in s[strlen(s)] (which is the empty
  // string).
  for(int a = 0; a <= strlen(wcj); a++) {
    c[a][strlen(s)] = 0;
    c[a][strlen(s)+1] = 0;
  }

  if(DEBUG)
    cout << "C\n";
  // how many times does wcj[a:] appear as a subsequence in s?
  for(int b = strlen(s); b >= 0; b--) {
    for(int a = strlen(wcj)-1; a >= 0; a--) {

      if(c[a][b] != -1)
	continue;
      //      cout << "a: " << a << " b: " << b << endl;
      assert(c[a+1][b+1] != -1);
      assert(c[a+1][b] != -1);
      if(wcj[a] == s[b]) {
	c[a][b] = (c[a+1][b+1] + c[a][b+1]) % 10000;
      } else {
	c[a][b] = c[a][b+1];
      }

      if(DEBUG)
	cout << "c " << a << "," << b << " : " << c[a][b] << endl;
    }
  }

  return c[0][0];
}

int main()
{
  int N;
  cin >> N;

  if(DEBUG)
    cout << "N: " << N << endl;
  
  char l[SIZE];
  // get rid of the new line character
  cin.getline(l, sizeof(l));
  for(int i = 0; i < N; i++) {
    cin.getline(l, sizeof(l));
    //    char* s = compress(l);
    long long c = count(l);
    if(DEBUG)
      printf("%lld ", c);
    printf("Case #%d: %04lld\n", i+1, c % 10000);
  }

  return 0;
}
