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

vector<int> v1,v2;
#pragma argsused
bool cmp1(const int &a,const int &b)
{ return a<b;
}
bool cmp2(const int &a,const int &b)
{ return a>b;
}
int main(int argc, char* argv[])
{

  FILE *ent,*sal;
  ent = fopen("a.ini","rt");
  sal = fopen("a.out","wt");
  int i, j,t, k, l, m, n;
  fscanf(ent,"%d",&n);
  __int64 res;
  for(i=0;i<n;i++)
  {
    fscanf(ent,"%d",&t);
    v1.resize(t);
    v2.resize(t);
    for(j=0;j<t;j++)
    {
      fscanf(ent,"%d",&k);
      v1[j]=k;
    }
    for(j=0;j<t;j++)
    {
      fscanf(ent,"%d",&k);
      v2[j]=k;
    }
    sort(v1.begin(),v1.end(),cmp1);
    sort(v2.begin(),v1.end(),cmp2);
    res = 0;
    for(j=0;j<t;j++)
      res+= v1[j]*v2[j];
    cout<<"Perro";
  }

  fclose(ent);
  fclose(sal);
  getch();
  return 0;
}
//---------------------------------------------------------------------------
 