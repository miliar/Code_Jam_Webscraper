#include <cstdio>
#define MAX_N 1000
using namespace std;

void nextCase(int caseNo)
{
  int R, k, N;
  int groups[MAX_N];
  int headOfQueue = 0;
  long result = 0L;

  //input
  scanf("%d %d %d", &R, &k, &N);
  for (int i = 0; i < N; i++)
  {
    scanf("%d", &groups[i]);
  }

  int ridesLeft = R;

  do
  {
    int places = k;
    int g;
    for (g = 0; g < N; g++)
    {
    	int idx = (headOfQueue + g) % N;
	int placesLeft = places - groups[idx];

	if (placesLeft < 0)
	{
	  break;
	}
	
	result += groups[idx];
	places = placesLeft;
    }

    headOfQueue = (headOfQueue + g) % N;
    ridesLeft--;
  } while (ridesLeft > 0 && headOfQueue != 0);

  if (ridesLeft > 0)
  {
	  int oneCycle = R - ridesLeft;
	  int cyclesLeft = ridesLeft / oneCycle;
	  
	  result += result * cyclesLeft;
	  ridesLeft = ridesLeft % oneCycle;

	  while (ridesLeft > 0) {
	    int places = k;
	    int g;
	    for (g = 0; g < N; g++)
	    {
		int idx = (headOfQueue + g) % N;
		int placesLeft = places - groups[idx];

		if (placesLeft < 0)
		{
		  break;
		}
		
		result += groups[idx];
		places = placesLeft;
	    }

	    headOfQueue = (headOfQueue + g) % N;
	    ridesLeft--;
	  }
  }

  //output
  printf("Case #%d: %ld\n", caseNo+1, result);
}

int main()
{
  int t;
  scanf("%d", &t);
  for (int i = 0; i < t; i++) {
    nextCase(i);
  }

  return 0;
}
