#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <cmath>
#include <map>
#include <cstdio>
#include <algorithm>


using namespace std;

int main()
{
  long long N;
  long long n, A, B, C, D, x0, y0, M;
  
  long X, Y;
    
  cin >> N;
  for(int i =0; i< N; i++)
  {
    cin >> n;
    cin >> A;
    cin >> B;
    cin >> C;
    cin >> D;
    cin >> x0;
    cin >> y0;
    cin >> M;
    X = x0;
    Y = y0;
    
    int som[n][2];
    
    for(int j = 0; j<n; j++)
    {
      som[j][0] = X;
      som[j][1] = Y;
      X = (A * X + B)%M;
      Y = (C * Y + D)%M;
      
    }
    long long result=0;
    for(int j=0; j<n; j++)
    {
      for(int k=(j +1); k<n; k++)
      {
        for(int l=(k+1); l<n; l++)
        {
          double X1 = (double(((double) som[j][0]) + ((double) som[k][0]) + ((double) som[l][0]))) / 3.0; 
          double X2 = (((double) som[j][1]) + ((double) som[k][1]) + ((double) som[l][1])) / 3.0;
          
          if((floor(X1) == X1) && (floor(X2)==X2))
          {
            result ++;
          }
        }
      }
    }
    
    
    
    printf("Case #%d: %d\n",i+1, result);
  }  
	return 0;
}
