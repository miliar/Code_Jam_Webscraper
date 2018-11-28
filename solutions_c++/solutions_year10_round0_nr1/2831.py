#include <iostream>
#include <stdint.h>

using namespace std;

#define MAX 0xffffffff

#define GETBITS(n) (MAX >> (32-n))

int main()
{
	uint32_t t;
	uint32_t caseno;
  uint32_t op = 0;
  uint32_t n, k;
	
	cin >> t;
	
	for (caseno = 1; caseno <= t; ++caseno)
	{    
    cin >> n >> k;

    op = (k & GETBITS(n)) == GETBITS(n);
    
    cout << "Case #" << caseno << ": " << ((op) ? "ON" : "OFF") << endl;
  }
  return 0;
}

