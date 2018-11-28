#include<iostream>
#include<string>
#include<vector>
#include<set>
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>

using namespace std;



string f(string N)
{
  int s = N.size();
  for( int k = s-1; k > 0;--k)
    {
      if(N[k] > N[k-1])
	{
	  char x = N[k-1];
	  sort(N.begin()+k,N.end());
	  int q = k;
	  N[k-1] = N[q];
	  while( N[q] <= x ) { ++q;  N[k-1] = N[q]; }
	  N[q] = x;

	  return N;
	}

    }
  sort(N.begin(),N.end());
  int q = 0;
  char x = N[0];  
  while( x == '0' ) { ++q; x = N[q]; }

  N[q] = '0';
  return x + N;
}

int main()
{
  long T;

  string N;

  cin >> T;
  for( int t=1; t<=T; ++t )
    {
      cin >>N;
      N=f(N);
      


      cout <<"Case #"<<t<<": ";
      cout << N<<endl;
    }
}
