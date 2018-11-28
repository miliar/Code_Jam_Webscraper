#include <iostream>
#include <cmath>

using namespace std;

int shift(int num, int shift, int len)
{
  int cutoff = num % int(pow(10, shift));
  int left = num / int(pow(10, shift));
  cutoff *= int(pow(10, len-shift));
  return cutoff + left;
}

int main()
{
  int t, a, b, len;
  int seen[10];
  int seenLen;
  cin >> t;
  for (int i = 0; i < t; i++)
    {
      //cout << "Shift last 3 of 12345: " << shift(12345, 3, 5) << endl;
      cin >> a;
      cin >> b;
      len = log10(a)+1;
      int total = 0;
      int temp;
      // Just try brute force
      for (int j = a; j <= b; j++)
	{
	  seenLen = 0;
	  for (int k = 1; k < len; k++)
	    {
	      temp = shift(j, k, len);
	      if (temp > j && temp <= b && temp >= a)
		{
		  bool ignore = false;
		  for (int l = 0; l < seenLen; l++)
		    {
		      if (temp == seen[l])
			{
			  //cout << "Found a repeat! " << temp << endl;
			  ignore = true;
			  break;
			}
		    }
		  if (!ignore)
		    {
		      //cout << "Found " << j << " " << temp << endl;
		      seen[seenLen] = temp;
		      seenLen++;
		      total ++;
		    }
		}
	    }
	  
	}

      cout << "Case #" << i+1 << ": " << total << endl;
    }
}
