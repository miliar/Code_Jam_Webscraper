    /*
Task:
Lang:
*/

#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <stack>

#define SP system("pause")

using namespace std;

string h;
ifstream ff;
ofstream of;
string d;
unsigned long long otg;
void df(int x, int y)
{
     
     for(int i=x; i<d.size() ;i++)
     {
             if(d[i]==h[y])
             {
               // cout<<i<<" "<<d[i]<<" "<<h[y]<<" "<<y<<endl;SP;
                if(y==18)otg++;
                else
                df(i+1,y+1);
             }
     }
}

int main()
{
    h="welcome to code jam";
    ff.open("C5-small.in");
    of.open("C5-small23.out");
    int N;
    ff>>N;
    getline(ff,d);
    for(int z=0; z<N; z++)
    {
            otg=0;
          getline(ff,d);
          df(0,0);  
          //cout<<otg<<endl;SP;
          stringstream str;
          str<<otg;
          string otgs;
          str>>otgs;
          otgs="0000"+otgs;
          int  j=0;
          of<<"Case #"<<z+1<<": ";
          for(int i=otgs.size()-4; j<4; i++,j++)
          of<<otgs[i];
          of<<endl;
    }
    return 0;
}
