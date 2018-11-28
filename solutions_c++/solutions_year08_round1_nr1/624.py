#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <cstdlib>
#include<conio.h>
#include<fstream>
 


#define FOR(i,st,en) for(int i=st;i<=en;i++)
#define sqr(a) a*a
using namespace std;

int main()
{
    FILE *_i,*_o;
    _i=fopen("A-large.in","r");
   // _o=fopen("tst.out","w+");
    ofstream out("A-large.out");
    int N;
    fscanf(_i,"%d",&N);
    
    FOR(k,1,N)
    {//fprintf(_o,"Case #%d: ",k);
    out<<"Case #"<<k<<": ";
    int n;
    vector<int>x,y;
    long long int p=0;
    fscanf(_i,"%d",&n);
    for(int i=0;i<n;i++)
    {int a;
    fscanf(_i,"%d",&a);
    x.push_back(a);
            
            }
    for(int i=0;i<n;i++)
    {int a;
    fscanf(_i,"%d",&a);
    y.push_back(a);
            
            }
    sort(x.begin(),x.end());
    sort(y.begin(),y.end());
     reverse(y.begin(),y.end());
     for(int i=0;i<n;i++)
      p+=((long long)x[i])*y[i];
      cout<<p<<endl;
    //prgram body
      //fprintf(_o,"%ld",p);        
    
    //fprintf(_o,"\n");
      out<<p<<endl;
    }
    cout<<"done";
    fclose(_i);
    //fclose(_o);
    out.close();
getche();
return 0;
}
