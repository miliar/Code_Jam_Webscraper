#include <fstream>
#include <cstring>
#include <sstream>
#include <map>
#include <iostream>
#include <cmath>

using namespace std;
double distmin,timemin;

void solve(ifstream &filein)
{
    int N;
    filein>>N;

    bool debug = true;

    double xv=0,yv=0,zv=0;
    double x=0,y=0,z=0;

    for(int i = 0; i < N; i++)
    {
        double tx,ty,tz;
        double txv,tyv,tzv;

        filein>>tx>>ty>>tz;
        filein>>txv>>tyv>>tzv;

        xv+=txv;
        yv+=tyv;
        zv+=tzv;

        x+=tx;
        y+=ty;
        z+=tz;


    }

    xv/= double(N);
    yv/= double(N);
    zv/= double(N);

    x/= double(N);
    y/= double(N);
    z/= double(N);

    if(debug)
    cout<<xv<<" "<<yv<<" "<<zv<<" "<<x<<" "<<y<<" "<<z<<" "<<endl;


    double vlen = sqrt(xv*xv+yv*yv+zv*zv);
    double len = sqrt(x*x+y*y+z*z);
    if(debug)
    cout<<vlen<<" "<<len<<endl;

    if(vlen <= 0.0 || len <= 0.0)
        {
            distmin=len;
            timemin=0;
            return;
        }

   x=-x;
   y=-y;
   z=-z;

   double mint = (x*xv+y*yv+z*zv)/vlen;
if(debug)
   cout<<mint<<endl;

   if(mint < 0)
   {
       distmin = len;
       timemin = 0;
       return;
   }

    double nelio = len*len-mint*mint;
    if(nelio < 0)
        nelio = 0;
    distmin = sqrt(nelio);
    timemin=mint/vlen;
    if(debug)
    cout<<distmin<<" "<<timemin<<endl;
}


int main()
{
  ifstream filein("input2.txt");
  ofstream fileout("output2.txt");


  int t;
  filein>>t;
  char buff[511];

  for(int i = 0; i < t; i++)
  {
    solve(filein);

    fileout<<"Case #"<<i+1<<": "<<distmin<<" "<<timemin<<endl;
    cout<<"Case #"<<i+1<<": "<<distmin<<" "<<timemin<<endl;
  }



  filein.close();
  fileout.close();

  return 0;
}
