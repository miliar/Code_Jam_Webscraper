#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <fstream>

using namespace std;
int main(void)
{
  int t,n,s,p,lar,eq;
  int tot[100];
  int mod[100];
  int max[100][2];
  int j=1;
  ifstream ifs("B-large.in");
  ofstream ofs("outputdancinglarge.txt");
  ifs>>t;
  while(j<=t)
  {
//     gets(str);
    lar = 0;
    eq = 0;
    ifs>>n;
    ifs>>s;
    ifs>>p;
    for(int i=0;i<n;i++)
    {
      ifs>>tot[i];
    }
    ofs<<"Case #"<<j<<": ";
    for(int i=0;i<n;i++)
    {
      if(tot[i]==0)
      {
	max[i][0] = 0;
	max[i][1] = 0;
      }
      else if(tot[i]==1)
      {
	max[i][0] = 1;
	max[i][1] = 1;
      }
      else
      {
	mod[i] = tot[i]%3;
	switch(mod[i])
	{
	  case 0: max[i][0] = tot[i]/3;
		  max[i][1] = tot[i]/3 + 1;
		  break;
	  case 1: max[i][0] = tot[i]/3 + 1;
		  max[i][1] = tot[i]/3 + 1;
		  break;
	  case 2: max[i][0] = tot[i]/3 + 1;
		  max[i][1] = tot[i]/3 + 2;
		  break;
	}
      }
      if(max[i][0]>=p)
	  lar++;
      else if(s>=1 && max[i][1]>=p)
      {
	lar++;
	s--;
      }
    }
    
    ofs<<lar<<'\n';
    j++;
  }
  return 0;
}