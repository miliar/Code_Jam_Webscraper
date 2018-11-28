#include<stdio.h>
#include<string>
#include<vector>
#include<iostream>
#include<utility>
#include<algorithm>
#include<set>
#include<stack>
#include<sstream>
#include<math.h>

using namespace std;

#define PB push_back
#define VI vector<int>
#define VS vector<string>
#define VL vector<long long>
#define ll long long

int main(int argc, char** argv)
{
  int cases;
  cin >> cases;
  for(int caseNo = 0; caseNo < cases; ++caseNo)
    {
      int N;
      cin >> N;
      int A[N], B[N];
      for(int i = 0; i < N; i++)
	{
	  int a, b;
	  cin >> a >> b;
	  A[i] = a;
	  B[i] = b;
	}
      ll count = 0;
      for(int i = 0; i < N-1; i++)
	{
	  for(int j = i+1; j < N; j++)
	    {
	      if((A[i] <= A[j] && B[i] >= B[j]) || (A[i] >= A[j] && B[i] <= B[j]))
		{
		  count++;
		}
	    }
	}      
      cout << "Case #" << caseNo + 1 << ": " << count << endl;
    }
}
