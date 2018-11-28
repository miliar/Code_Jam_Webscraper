#include <fstream>
#include <iostream>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>

#define MAXN 100000
#define forn(i, n) for (i=0; i<n; i++)

using namespace std;

int plan[50][3];


double d(int a, int b){
       double x, y, res;
       x=plan[a][0]-plan[b][0];
       y=plan[a][1]-plan[b][1];
       res=sqrt(x*x+y*y);
       return res;
    }
int main(){
    freopen ("d.out", "w", stdout);
    ifstream in("d.in");
    ofstream out("d.out");
    int c, k=0, i, n;
    in>>c;
    double res=MAXN;
    double dist;
    while (k<c){
          res=MAXN;
          k++;
          in>>n;
          forn (i, n){
               in>>plan[i][0]>>plan[i][1]>>plan[i][2];
               }
          if (n==1){
             res=plan[0][2];
             }
          if (n==2){
             res=max(plan[0][2], plan[1][2]);
          }
          if (n==3){
             dist=d(0, 1);
             dist+=plan[0][2]+plan[1][2];
             dist/=2.0;
             if (dist<plan[2][2])dist=plan[2][2];
             if (dist<res)res=dist;

             dist=d(0, 2);
             dist+=plan[0][2]+plan[2][2];
             dist/=2.0;
             if (dist<plan[1][2])dist=plan[1][2];
             if (dist<res)res=dist;

             dist=d(2, 1);
             dist+=plan[2][2]+plan[1][2];
             dist/=2.0;
             if (dist<plan[0][2])dist=plan[0][2];
             if (dist<res)res=dist;

          }
          cout.setf(ios::fixed,ios::floatfield);
          cout.precision( 6);

          cout<<"Case #"<<k<<": "<<res<<endl;
          //printf("%.5lf",(double)res);
//          out<<endl;
          }
    
    
    
    
    }
