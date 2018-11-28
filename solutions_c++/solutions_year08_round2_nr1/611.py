#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

int main()
{
	int N;
	int c = 1;

   long long pointx[1000],pointy[1000];
   
  	freopen("r2a.in","r",stdin);
  	
   cin>>N;
   
   long long n,A,B,C,D,xo,yo,M;
	while (N--)
	{
		// Read Input
		cin>>n>>A>>B>>C>>D>>xo>>yo>>M;
		
      int X = xo;
      int Y = yo;
      pointx[0] = X;
      pointy[0] = Y;

      for (long i = 1;i<=n-1;i++)
      {
          X = (A * X + B) % M;
          Y = (C * Y + D) % M;
          pointx[i] = X;
          pointy[i] = Y;
      }

      long count = 0;      
		
      for (int i=0;i<n-2;i++)      
         for (int j=i+1;j<n-1;j++)      
            for (int k=j+1;k<n;k++)
            {      
               if ( (((pointx[i]+pointx[j]+pointx[k]) % 3) == 0)
					 && (((pointy[i]+pointy[j]+pointy[k]) % 3) == 0) )
					 	count++;
				}

      cout<<"Case #"<<c++<<": "<<count<<endl;
	}	
	
	return 1;
}
