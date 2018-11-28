#include<iostream>
#include<cctype>
#include<cstdlib>
#include<vector>
#include<cmath>
#include<string>
#include<algorithm>
#include<stack>
#include<sstream>
#include<conio.h>
#include<cctype>
#include<fstream>
#include<iomanip>
using namespace std;

int main()
{
 ifstream fin("A.in",ios::in);
 ofstream fout("A.out",ios::out);
 
 int tests,test,n;
 fin>>tests;
 for(test=1;test<=tests;test++)
 {
 vector<string> tm;
 tm.clear();
 string s;
 fin>>n;
 int i;
 for(i=0;i<n;i++)
 {fin>>s;
 tm.push_back(s);
}

int jt[105][2];
double wp[105],owp[105],oowp[105];
for(i=0;i<105;i++) { jt[i][0]=jt[i][1]=0; }
int z,o,j;
for(i=0;i<n;i++)
{  z=0;o=0;
 for(j=0;j<n;j++)
 {
  if(tm[i][j]=='0') z++;
  else if(tm[i][j]=='1') o++;
 }
 jt[i][0]=z; jt[i][1]=o;
 wp[i]=float(o)/(o+z);
}              
double sum; int k;
for(i=0;i<n;i++)
{  sum=0; k=0;
  for(j=0;j<n;j++)
  {
  if(j!=i) {
  if(tm[j][i]=='0') { sum+=(float(jt[j][1])/(jt[j][1]+jt[j][0]-1)); k++;}
  else if(tm[j][i]=='1') { sum+=(float(jt[j][1]-1)/(jt[j][1]+jt[j][0]-1)); k++; }
}
  }
  owp[i]=sum/k;
}              

for(i=0;i<n;i++)
{  sum=0; k=0;
  for(j=0;j<n;j++)
  {
  if(j!=i) {
  if(tm[j][i]=='0') { sum+=owp[j]; k++;}
  else if(tm[j][i]=='1') { sum+=owp[j]; k++; }
}
  }
  oowp[i]=sum/k;
}              
 double rti;
   fout<<"Case #"<<test<<":\n";
 for(i=0;i<n;i++)
 {
  rti=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
  
  fout<<setprecision(10)<<rti<<endl;
  
 }  
 }

 fin.close();
 fout.close();
 getch();
 return 0;   
}
