#include <iostream>
#include <math.h>
using namespace std;
int main( int argc, const char* argv[] )
{
  int n, count;
  cin >> n;
  for (int i = 1; i<n+1; i++)
  {
    count = 0;
    int a, b;
    cin >> a >> b;
    for (int j = a; j <= b; j++)
    {
      int cut[10], k=0, sums[10], sumnum=0;
      for (int slice=j/10, digit=j%10; slice+digit!=0; digit=slice%10, slice/=10, k++)
      {
	cut[k]=digit;
      }
      for (int ii=0; ii<k; ii++)
      {
	int sum = 0;
	for (int jj=0; jj<k; jj++)
	{
	  sum += pow(10,jj)*cut[(jj+ii)%k];
	}
	if (sum >=a && sum <= b && j < sum)
	{
	  for (int kk = 0; kk < sumnum; kk++)
	  {
	    if (sum == sums[kk]) count--;
	    break;
	  }
	  count++;
	  sums[sumnum]=sum;
	  sumnum++;
	  //cout << j << " rot " << sum << "\n";
	}
      }
    }
    cout << "Case #" << i << ": " << count << endl;
  }
}