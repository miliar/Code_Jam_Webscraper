//---------------------------------------------------------------------------

#pragma hdrstop

//---------------------------------------------------------------------------
#include <math.h>
#include <vector>
#include <string>
#include <stdio.h>
#include <conio.h>
#include <map>
#include <set>
#include <algorithm>
#include <iostream.h>
using namespace std;

#include <vcl.h>
vector<int> v1,v2;
#pragma argsused
long double myp(long double val,int n);
string Sol[31];

int main(int argc, char* argv[])
{
  
Sol[1] = "005";
Sol[2] = "027";
Sol[3] = "143";
Sol[4] = "751";
Sol[5] = "935";
Sol[6] = "607";
Sol[7] = "903";
Sol[8] = "991";
Sol[9] = "335";
Sol[10] = "047";
Sol[11] = "943";
Sol[12] = "471";
Sol[13] = "055";
Sol[14] = "447";
Sol[15] = "463";
Sol[16] = "991";
Sol[17] = "095";
Sol[18] = "607";
Sol[19] = "263";
Sol[20] = "151";
Sol[21] = "855";
Sol[22] = "527";
Sol[23] = "743";
Sol[24] = "351";
Sol[25] = "135";
Sol[26] = "407";
Sol[27] = "903";
Sol[28] = "791";
Sol[29] = "135";
Sol[30] = "647";
  FILE *ent,*sal;
  ent = fopen("C-small-attempt2.in","rt");
  sal = fopen("Pot2.out","wt");
  int i, j,t, k, l, m, n;
  fscanf(ent,"%d",&n);
  __int64 res;

  char val[4];
  val[4] = '\0';
  int ind;
  long double pen,z = 3+sqrt(5);
  for(i=0;i<n;i++)
  {
    fscanf(ent,"%d",&t);
    fprintf(sal,"Case #%d: %s\n",i+1,Sol[t].c_str());
  }

  fclose(ent);
  fclose(sal);
  //getch();
  return 0;
}
long double myp(long double val,int n)
{
  if(n==1)
    return val;
  long double resp;
  resp = myp(val,n/2);
  resp = pow(resp,2);
  //resp = resp-(int)(resp/1000)*1000;
  if (n%2)
    resp*=val;
  //resp = resp-(int)(resp/1000)*1000;
  return resp;

}
//---------------------------------------------------------------------------
 