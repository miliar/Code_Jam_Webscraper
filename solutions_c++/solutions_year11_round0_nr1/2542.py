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

char hall[maxn];
int pos[maxn];
struct robot{
  int pos;
  int time;
};
int main(int argc, char ** argv)
{
  int i,t,n,j, curtime, step, choose;
  fstream fin;
  ofstream fout;
  fin.open(argv[1]);
  fout.open(argv[2]);
  string s;
  fin >> t;
  getline(fin,s);
  struct robot r[2];//r[0] :orange; r[1] : blue
 
  for ( j = 1;j <= t;j ++)
  {
    getline(fin, s); 
    istringstream istring(s,istringstream::in);
    istring >> n;
    curtime = 0;
    for (i = 0;i < 2;i ++)
    {
      r[i].pos = 1;
      r[i].time = 0;
    }
 

    for (i = 0;i < n;i ++)
    {
      istring >> hall[i];
      istring >> pos[i];
      if (hall[i] == 'O')
      {
        choose = 0;
      } else {
        choose = 1;
      }
      step = abs(pos[i] - r[choose].pos);
      if (step > curtime - r[choose].time)
        curtime = step + r[choose].time;
      curtime ++;
      //fout << "step " << i << " choose " << choose << " step " << step << " curtime "<< curtime << endl;
      r[choose].time = curtime;
      r[choose].pos = pos[i];
    }
    fout << "Case #" << j<< ": " << curtime << endl;
  }
  fin.close();
  fout.close();
  return 0;
}
