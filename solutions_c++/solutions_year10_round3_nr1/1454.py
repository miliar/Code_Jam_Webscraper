#include <iostream>
#include <conio>
#include <stdio>
#include <math>
main()
{
	freopen("in.txt", "r", stdin);
   freopen("out.txt", "w", stdout);

	int t, a[2], b[2], n;
   cin>>t;
   int i, j, k=0;
   for(i = 0; i<t; i++)
   {
   	cin>>n;
      a[0]=b[0]=a[1]=b[1]=0;
      for(j = 0; j<n; j++)
      	cin>>a[j]>>b[j];
      for(j = 0;j<n; j++)
      {
      	if(a[j] <a[j+1] && b[j]>b[j+1] && j<(n-1))
         	k++;
         else if( a[j]>a[j+1] && b[j]<b[j+1] &&j<(n-1))
         	k++;
      }
      cout<<"Case "<<(i+1)<<":"<<k<<endl;
   }
	getch();
}
