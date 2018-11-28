#include <fstream>
#include <cstring>
#include <sstream>
#include <map>
#include <iostream>
#include <cmath>

using namespace std;
double distmin,timemin;


int vangit[1000];
int memory[103][103];


int minimi(int alku, int loppu)
{
    if(memory[alku][loppu])
        return memory[alku][loppu];

    if(alku +1 >= loppu)
        return 1;

    int mini = 999999999;
    for(int i = alku+1; i < loppu; i++)
    {
        int res = minimi(alku,i)+minimi(i,loppu)-2;
        if(res < mini)
            mini = res;
    }

    return memory[alku][loppu] = mini+vangit[loppu]-vangit[alku]  -1;


}

int solve(ifstream &filein)
{
    int p,q;
    filein>>p>>q;
    vangit[0] = 0;
    for(int i = 1; i <= q; i++)
        filein>>vangit[i];

    vangit[q+1] = p+1;


    memset(memory,0,sizeof(memory));
    return minimi(0,q+1)-1;


}




int main()
{
  ifstream filein("input3.txt");
  ofstream fileout("output3.txt");


  int t;
  filein>>t;
  char buff[511];

  for(int i = 0; i < t; i++)
  {
    int res = solve(filein);

    fileout<<"Case #"<<i+1<<": "<<res<<endl;
    cout<<"Case #"<<i+1<<": "<<res<<endl;

  }



  filein.close();
  fileout.close();

  return 0;
}
