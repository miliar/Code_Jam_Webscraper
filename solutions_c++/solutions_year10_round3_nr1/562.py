#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <ctime>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
using namespace std;


struct Point{
    int start;
    int end;  
};
bool cmp(Point a,Point b)
{
    return a.start<b.start;
}

int main() 
{ 
//    freopen("..\\A.in","r",stdin); 
//    freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout); 
//   freopen("A-small-practice.in","r",stdin);freopen("A-small-practice.out","w",stdout); 
    freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout); 
//    freopen("..\\A-small.in","r",stdin);freopen("..\\A-small.out","w",stdout);
    int T;
    int N;
    while (scanf ("%d",&T)!=EOF)
    {
          for (int count=1;count<=T;count++)
          {
                cin>>N;
                Point P[N];
                for (int i=0;i<N;i++)
                    cin>>P[i].start>>P[i].end;
                sort(P,P+N,cmp);
                int res=0;
                for (int i=0;i<N;i++)
                {
                    for (int j=i;j<N;j++)
                    {
                         if (P[i].end>P[j].end)
                            res++;    
                    }    
                }
                
              cout<<"Case #"<<count<<": "<<res<<endl;
          }      
    }
    return 0; 
} 



                 
