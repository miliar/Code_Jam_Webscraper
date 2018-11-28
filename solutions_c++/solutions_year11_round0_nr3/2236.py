#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>

using namespace std;

string toBinary(int a)
{
  if(a == 0)
    return "0";

  string ba = "";
  while(a > 0)
  {
    ba += ('0' + a % 2);
    a /= 2;
  }
  return ba;
}

int binary_addition(int a, int b)
{
  string ba = toBinary(a),
	 bb = toBinary(b);

  if(bb.length() > ba.length())
  {
    string mem = bb;
    bb = ba;
    ba = mem;
  }
  
  if(ba.length() != bb.length())  
    bb = bb + string(ba.length() - bb.length(), '0'); 
  
  int result = 0;
  for(int i = 0; i < ba.length(); i++)
  {
    if((ba[i] == '1' && bb[i] == '0') || (bb[i] == '1' && ba[i] == '0'))
      result += (int)pow(2, i);
  }

  return result;
}

int main()
{
  
  int T;
  cin >> T;

  for(int i = 0; i < T; i++)
  {
    int N;
    cin >> N;

    vector<int> candies;
    for(int j = 0; j < N; j++)
    {
      int C;
      cin >> C;

      candies.push_back(C);
    }

    int maxSum = -1;

    sort(candies.begin(), candies.end());
    
    int sum1 = 0;

    for(int j = 0; j < candies.size(); j++)
      sum1 = binary_addition(sum1, candies[j]);

    if(sum1 == 0)
    {
      sum1 = 0;
      for(int j = 0; j < candies.size() - 1; j++)
      {
	int realSum = 0;
	int sum2 = 0;

	sum1 = binary_addition(sum1, candies[j]);

	for(int k = j + 1; k < candies.size(); k++)
	{
	  realSum += candies[k];
	  sum2 = binary_addition(sum2, candies[k]);
	}

	if(sum1 == sum2)
	{
	  maxSum = realSum;
	  break;
	}
      }
    }

    if(maxSum == -1)
      cout << "Case #" << i + 1 << ": " <<  "NO"  << endl;
    else
      cout << "Case #" << i + 1 << ": " <<  maxSum  << endl;
  }
}
