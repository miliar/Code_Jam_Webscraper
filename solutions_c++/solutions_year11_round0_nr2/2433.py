/*
 * =====================================================================================
 *
 *       Filename:  a.cpp
 *
 *    Description:  i
 *
 *        Version:  1.0
 *        Created:  05/07/2011 03:03:45 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *        Company:  
 *
 * =====================================================================================
 */
#include <iostream>
#include <sstream>
#include <stdlib.h>
#include <fstream>
#include <string.h>

using namespace std;
const int maxn = 30;
const int maxl = 200;

int r[maxl];
int combine[maxn][maxn];
bool opp[maxn][maxn];
int main(int argc, char ** argv)
{
  int i,j,n,t, c, d, k,l;
  char a,b,f;
  fstream fin;
  ofstream fout;
  fin.open(argv[1]);
  fout.open(argv[2]);
  string s;
  fin >> t;
  for ( j = 1;j <= t;j ++)
  {
    memset(combine, -1, sizeof(combine));
    memset(opp, false, sizeof(opp));
    fin >> c;
    for (i = 0;i < c;i ++)
    {
      fin >> a >> b >> f;
      combine[a-'A'][b-'A'] = f - 'A';
      combine[b-'A'][a-'A'] = f - 'A';
    }
    fin >> d;
    for (i = 0;i < d;i ++)
    {
      fin >> a >> b;
      opp[a-'A'][b-'A'] = true;
      opp[b-'A'][a-'A'] = true;
    }

    fin >> n;
    l = 0;
    for (i = 0;i < n;i ++)
    {
      fin >> a;
      r[l] = a - 'A';
      if (l > 0 && combine[r[l]][r[l-1]] >= 0) {
        r[l-1] = combine[r[l]][r[l-1]];
      } else {
        for (k = 0;k < l;k ++){
	  if (opp[r[l]][r[k]])
	    break;
	}
	if (k == l) {
	  l ++;
	} else {
	  l = 0;
	}
      }

    }
    fout << "Case #" << j<< ": [" ;
    for (i = 0;i < l;i ++)
    {
      if (i > 0)
        fout << ", ";
      fout << char(r[i] + 'A');
    }
    fout << "]" << endl;
  }
  fin.close();
  fout.close();
  return 0;
}
