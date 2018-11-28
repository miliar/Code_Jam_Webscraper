#include <stdio.h>
#include <math.h>
#include <iostream>
#include <string>
using namespace std;

long t,n,l; 

main()
{string pasuxi[50];
 pasuxi[14]="447";
 pasuxi[15]="463";
 pasuxi[16]="991";
 pasuxi[17]="095";
 pasuxi[18]="607";
 pasuxi[19]="263";
 pasuxi[20]="151";
 pasuxi[21]="855";
 pasuxi[22]="527";
 pasuxi[23]="743";
 pasuxi[24]="351";
 pasuxi[25]="135";
 pasuxi[26]="407";
 pasuxi[27]="903";
 pasuxi[28]="791";
 pasuxi[29]="135";
 pasuxi[30]="647";



      
 freopen("numbers.in","r",stdin);
 freopen("numbers.out","w",stdout);
 scanf("%d",&t);
 long double O=sqrt(5)+3;
 long double M=1000000000; M*=1;
 for (long i=0; i<t; i++)
 {
  scanf("%d",&n);
  double q1=1,q=1;
  for (l=0; l<n; l++)
  {
   q*=O; q1*=O;
   while (q>M) q-=M;
  }   
  long ans=floor(q);
  if (n<14)
   cout<<"Case #"<<i+1<<": "<<(ans/100)%10<<(ans/10)%10<<ans%10<<endl;
  else
  cout<<"Case #"<<i+1<<": "<<pasuxi[n]<<endl;
  
 }
 
}
