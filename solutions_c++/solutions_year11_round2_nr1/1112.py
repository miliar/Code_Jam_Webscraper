#include <iostream>
#include <cstdio>
using namespace std;
int n;
char c[128][128];
double w[128];
double a[128];
double wp[128];
double owp[128];
double oowp[128];
void solve ()
{
  
  scanf ("%d\n", &n);
  
  int i, j; 
  for (i = 0; i < 128; i ++)
    w[i] = a[i] = wp[i] = owp[i] = oowp[i] = 0.0;
  
  for (i = 0; i < n; i ++)
  {
    for (j = 0; j < n; j ++)
    {
      scanf ("%c", &c[i][j]);
      if (c[i][j] != '.')
      {
	a[i] += 1;
	if (c[i][j] == '1') w[i] += 1;	
      }
    }
    getchar ();
  }
  /*
  for (i = 0; i < n; i ++)
  {
    for (j = 0; j < n; j ++)
    cout << c[i][j] ;
    cout << endl;
    
  }
  */
    for (i =0; i < n; i ++)
    {
      wp[i] = (a[i] == 0) ? 0.0 : (w[i]/a[i]);
      
      for (j = 0; j < n; j ++)
      {
	double nom = w[j] - (int)(c[j][i] == '1');
	double denom = a[j] - (int)(c[i][j] != '.');
	if (denom != 0 && c[i][j] != '.')
	  owp[i] += nom/denom;
      }
      owp[i] /= a[i];
    }
    
    for (i =0; i < n; i ++)
    {
      
      for (j = 0; j < n; j ++)
      {
	if (c[i][j] != '.')
	  oowp[i] += owp[j];
      }
      oowp[i] /= a[i];
    }
  
  for (i =0; i < n; i ++)
    printf ("%.12lf\n", 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]);
  
  
}

int main ()
{
  
  int t; 
  scanf ("%d", &t);
  
  for (int i = 1; i <= t; i ++)
  {
    printf ("Case #%d:\n", i);
    solve ();
  }
  
}