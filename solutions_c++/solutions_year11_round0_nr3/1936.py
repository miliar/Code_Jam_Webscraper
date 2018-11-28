#include "fstream.h"
using namespace std;
void main()
{
 int t;
 ifstream inp("input.txt");
 ofstream oup("output.txt");
 inp>>t;
 for (int q=1;q<=t;q++)
 {
  int n;
  long s=0,s2=0,min=10000000;
  long a[1000];
  inp>>n;
  for (int i=0;i<n;i++)
  {
   inp>>a[i];
   s=(s|a[i])-(s&a[i]);
   if (a[i]<min)
    min=a[i];
   s2+=a[i];
  }
  oup<<"Case #"<<q<<": ";
  if (s!=0)
   oup<<"NO";
  else
   oup<<(s2-min);
  oup<<endl;
 }
 oup.close();
 inp.close();
}
