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

using namespace std;
const int maxn = 200;

int main(int argc, char ** argv)
{
  int i,j,n,t;
  fstream fin;
  ofstream fout;
  fin.open(argv[1]);
  fout.open(argv[2]);
  string s;
  fin >> t;
  long result, cur, sum, normalsum;
  for ( j = 1;j <= t;j ++)
  {
    fin >> n;
    sum =0; 
    result = -1;
    normalsum = 0;
    for (i = 0; i < n;i ++)
    {
      fin >> cur;
      sum = (sum ^ cur);
      if (result < 0 || cur < result)
        result = cur;
      normalsum += cur;
    }
     fout << "Case #" << j<< ": " ;
    if (sum != 0)
      fout << "NO" << endl;
    else
      fout << normalsum - result << endl;

  }
  fin.close();
  fout.close();
  return 0;
}
