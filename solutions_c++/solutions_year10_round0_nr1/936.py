#include <windows.h>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool light(unsigned long n, unsigned long k)
{
	unsigned long i = 0;

	for(i = 0 ; i < n ; ++i)
	{
		if(k%2 == 0)
		{
			return false;
		}
		else
		{
			k /= 2;
		}
	}

	return true;
}

int 
main(int argc, const char *argv[])
{
  unsigned long t, n, k, i;

  cin >> t;

  for(i = 0; i < t ; ++i)
  {
    cin >> n;
    cin >> k;

    if(light(n,k))
	{
		cout << "Case #" << i+1 << ": ON" << endl;
	}
	else
	{
		cout << "Case #" << i+1 << ": OFF" << endl;
	}
  }

  return 0;
}