#include <iostream>
#include <string>
#include <fstream>
#include <math.h> 
 
using namespace std;

 
ifstream fin("d:\\A-large.in");
ofstream fout("d:\\A-large.out");
 
#define cin fin
#define cout fout

 
long int N;
long int K;
 
int main()
{
  long int T;
  cin >> T;

  for (long int i = 0; i < T; ++i)
  { 
    cin >> N >> K;
    long int t=1,pow;
	for (pow=0; pow < N ; pow++)
	{
		t=t * 2; 
	}
    int flag = ( K +1) % t;
	if ( flag == 0)
	{
      cout << "Case #" << i + 1 << ": " <<  "ON"  << endl;
	}
    else
      cout << "Case #" << i + 1 << ": " <<  "OFF"  << endl;
  }
  return 0;
}