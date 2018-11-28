#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <fstream>

using namespace std;

int mtime[1000];
int otime,btime,ostep,bstep;
ifstream iff;
ofstream of;

int main()
{
    int t,n,ltime;
    iff.open("a.in");
    iff>>t;
    of.open("a.out");
    for(int j = 0; j<t; j++)
    {
	iff>>n;
       char a;
       int step;
       ostep=1;bstep=1;otime =0; btime = 0;ltime = -1;
       for(int i=0; i<n; i++)
       {
	  iff>>a;
	  iff>>step;
	  memset(mtime , 0 ,sizeof(mtime));
	  if(a == 'O')
	  {
	     otime += abs(step - ostep);
	     if(otime  <ltime) otime =ltime;
	      otime++;
	     ltime = otime;
	     ostep = step;
	  }
	  else
	  {
	      btime += abs(step - bstep);
		if(btime  <ltime) btime =ltime;
		btime++;
		ltime = btime;
		bstep = step;
	
	  }
      }
      of<<"Case #"<<j+1<<": "<<ltime<<endl;
    }
    return 0;
}