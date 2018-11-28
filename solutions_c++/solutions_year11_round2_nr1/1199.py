#include <fstream>
using namespace std;
char a[300][300];
void main()
{
 ifstream inp("input.txt");
 ofstream oup("output.txt");
 int nn;
 inp>>nn;
 for (int ni=1;ni<=nn;ni++)
 {
  oup<<"Case #"<<ni<<":"<<endl;
  int k;
  inp>>k;
  double wns[300]={0};
  double mts[300]={0};
  double owp[300]={0};
  for (int i=0;i<k;i++)
  {
   inp>>a[i][0];
   if (a[i][0]=='1')
    wns[i]++;
   if (a[i][0]!='.')
    mts[i]++;
   for (int j=1;j<k;j++)
   {
    inp.get(a[i][j]);
    if (a[i][j]=='1')
     wns[i]++;
    if (a[i][j]!='.')
     mts[i]++;
   }
  }
  for (int i=0;i<k;i++)
  {
   double m=0,m2=0;
   for (int j=0;j<k;j++)
    if (a[i][j]!='.')
	{
	 m++;
	 double l2=mts[j]-1,l1=wns[j];
	 if (a[i][j]=='0')
	  l1--;
	 m2+=l1/l2;
	}
   owp[i]=m2/m;
  }
  for (int i=0;i<k;i++)
  {
   double res=0.25*(wns[i]/mts[i])+0.5*owp[i],q=0,q2=0;
   for (int j=0;j<k;j++)
    if (a[i][j]!='.')
	{
	 q++;
	 q2+=owp[j];
	}
   res+=0.25*q2/q;
   oup.precision(8);
   oup<<res<<endl;
  }
 }
 inp.close();
}