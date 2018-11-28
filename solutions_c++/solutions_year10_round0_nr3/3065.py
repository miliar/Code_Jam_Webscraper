#include <iostream>
#include <conio>
#include <fstream>

main()
{
	int t, n;
   int r, k;
   ofstream f("result.txt");
   unsigned long int g[1000];
   cin>>t;
   int i, j, a, b, c, d, s;
   for(i = 0; i<t; i++)
   {
   	for( j = 0; j<100; j++)
      	g[j] = 0;
   	cin>>r>>k>>n;
      for(j = 0; j<n; j++)
   		cin>>g[j];

      s = 0;
      for(j = 0; j<r; j++)
      {
      	a = 0;
         b = 0;
         while(a+g[b]<=k && b<n)
         {
         	a = a + g[b];
            s = s + g[b];
            b++;
         }
         for(a = 0; a<b; a++){
         c = g[0];
         for(d = 0; d<(n-1); d++)
         {
         	g[d] = g[d+1];
         }
         g[n-1] = c;
      	}
      }
      cout<<"Case #"<<(i+1)<<": "<<s<<endl;
      f<<"Case #"<<(i+1)<<": "<<s<<endl;
   }
   f.close();
   getch();
}
