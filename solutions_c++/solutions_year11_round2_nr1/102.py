#include <iostream>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <set>
#include <string>
#include <map>

using namespace std;

vector< string > p;
vector< double > WP;
vector< double > OWP;
vector< double > OOWP;
int n;


double calcWPwithout(int i, int restr)
{
  int total = 0;
  int win = 0;
  for (int j=0; j<n; j++)
    if (p[i][j] == '1' && j!=restr)
      total++, win++;
    else if (p[i][j] == '0' && j!=restr)
      total++;
    
  return win*1.0/total;
}
  
inline int solve(int testnum)
{
  scanf("%d\n", &n);
  
  p.resize(n);
  for (int i=0; i<n; i++)
    getline(cin, p[i]);
  
  WP.resize(n);
  for (int i=0; i<n; i++)
  {
    int total = 0;
    int win = 0;
    for (int j=0; j<n; j++)
      if (p[i][j] == '1')
	total++, win++;
      else if (p[i][j] == '0')
	total++;
      
    WP[i] = win*1.0/total;
  }
  
  OWP.resize(n);
  for (int i=0; i<n; i++)
  {
    int kol = 0;
    double sum = 0;
    for (int j=0; j<n; j++)
      if (i!=j && p[i][j] != '.')
	sum += calcWPwithout(j, i), kol++;
      
    OWP[i] = sum/kol;
  }
  
  OOWP.resize(n);
  for (int i=0; i<n; i++)
  {
    int kol = 0;
    double sum = 0;
    for (int j=0; j<n; j++)
      if (i!=j && p[i][j] != '.')
	kol++, sum += OWP[j];
      
    OOWP[i] = sum/kol;
  }
  
  cout.precision(30);
  cout.setf(ios::fixed);
  cout << "Case #" << testnum+1 << ":" << endl;
  for (int i=0; i<n; i++)
    cout << WP[i]*0.25 + OWP[i]*0.5 + 0.25*OOWP[i] << endl;
}

int numoftests;
int main()
{
  scanf("%d\n", &numoftests);
  
  for (int i=0; i<numoftests; i++)
    solve(i);
}