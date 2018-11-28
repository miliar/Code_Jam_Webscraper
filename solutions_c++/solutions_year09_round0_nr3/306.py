// 2009/09/03 Naoyuki Hirayama

#include <iostream>
#include <iomanip>
#include <string>
#include <vector>

char search[20];
char text[502];

int dp[20][502];

int doit(int si, int ti) {
  // std::cerr << "dp " << si << ", " << ti << ": " << dp[si][ti] << std::endl;
  if( 0 <= dp[si][ti] ) { return dp[si][ti]; }
  if (search[si] == 0) { return dp[si][ti]=1; } // found
  if (text[ti] == 0) { return dp[si][ti]=0; } // not found

  int n = doit( si, ti+1 );       // not proceed
  if(search[si] == text[ti]) {
    int  nn = doit( si+1, ti+1 );  // proceed;
    n += nn;
    n %= 10000;
  }
  return dp[si][ti]=n;
}

int main() {

#if 1
  const char* welcome = "welcome to code jam";
  strcpy(search, welcome);

  int N;
  std::cin >> N;

  std::string line;
  std::getline(std::cin, line);

  for( int i = 0 ; i < N ; i++ ) {
    for(int k = 0 ; k < 20  ; k++ ) {
      for( int j = 0 ; j < 502 ; j++ ) {
        dp[k][j] = -1;
      }
    }

    std::getline(std::cin, line);
    strcpy(text, line.c_str());

    int n = doit(0, 0);

    std::cout
        << "Case #" << (i+1) << ": " 
        << std::setw(4) << std::setfill('0')
        << n << std::endl;
  }
#else
  const char* welcome ="ab";
  strcpy(search, welcome);

  strcpy(text, "bab");
  std::cout << doit(0, 1) << std::endl;
  std::cout << doit(0, 2) << std::endl;
  std::cout << doit(1, 1) << std::endl;
  std::cout << doit(0, 0) << std::endl;
#endif
}
