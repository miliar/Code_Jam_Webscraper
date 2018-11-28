 /*
Task: C
Lang: C++
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

ofstream of;
ifstream ff;
int k,q;
int Q[102];
bool used[102];
int otg;

bool sl(int z,int n)
{
    if(n==q  && otg>z)otg=z;
    for(int i=0; i<q; i++)
    {
            if(used[i]==0)
            {
                          int j=i;
                          int j1=i;
                     while(j!=-1)
                     {
                                 if(used[j]==1)break;
                                 j--;
                                
                     }  
                     while(j1!=q)
                     {
                                 if(used[j1]==1)break;
                                 j1++;
                     }
                     int t;
                     if(j==-1)t=Q[i]-1;
                     else
                     t=Q[i]-Q[j]-1;
                     if(j1==q)t+=k-Q[i];
                     else t+=Q[j1]-Q[i]-1;
                     used[i]=1;
                     //cout<<Q[i]<<" "<<t<<" <-t   ";
                     sl(z+t,n+1);
                     used[i]=0;
            }
    }
}

int main()
{
    ff.open("C-small1.in");
    of.open("C-small1.out");
    int n;
    ff>>n;
    for(int z=0; z<n; z++)
    {
            ff>>k>>q;
            otg=k*q;
            for(int i=0; i<q; i++)
            ff>>Q[i];
            for(int i=0; i<q; i++)
            {used[i]=1;sl(k-1,1);used[i]=0;}
            of<<"Case #"<<z+1<<": "<<otg<<endl;
    } 
  //  SP;
    return 0;
}
