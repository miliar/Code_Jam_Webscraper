#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <algorithm>
#include <cstring>
#include <cctype>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <sstream>
#include <set>

using namespace std;

struct snap{
       bool status;
       bool current;
       } a[10 + 2];
       
void restart (int m)
{
     for (int i=0; i<m;i++)
     {
         a[i].current = false;
         a[i].status = false;
     }
     a[0].current = true;
}

int main() {
    
    int cases = 0;
    
    string fname = "A-small-attempt2";
	freopen((fname+".in").c_str(), "r", stdin);
	freopen((fname+".out").c_str(), "w", stdout);
	
	
    scanf("%d", &cases);
    int b=0;
    
    while(cases--)
    {
            int N;
            int K;
            scanf("%d %d", &N, &K);
            
            restart(N);
            
            for(int i=0; i <K; i++)
            {
                    for(int j=0; j <N; j++)
                    {
                            if(a[j].current)
                            a[j].status = a[j].status ? false: true;
                    }
                    for(int j =0; j<N; j++)
                    {
                            if(a[j].current && a[j].status)
                            a[j+1].current = true;
                            else
                            a[j+1].current = false;
                    }
            }
            if(a[N-1].current && a[N-1].status)
            {
                 printf("Case #%d: ON\n",++b);
            }
            else
            {
                printf("Case #%d: OFF\n",++b);
            }
    }
                 
     
     int ab = 0;
    cin>>ab;
   /* int n = 0;
    int k = 0;
    string xy = "";
    
    for(int a = int(cases[0])-49; a>=0; a--)
    { 
          getline(fin,xy);    
          n = int(xy[0]-48);
          k = int(xy[2]-48);
          
          if(k== (pow(2,n)-1))
          {
          fout<<"Case #"<<(int(cases[0])-48)-a<<": "<<"ON\n";
          }
          else
          {
          fout<<"Case #"<<(int(cases[0])-48)-a<<": "<<"OFF\n";
          }
          //cout << xy[0]<<xy[2]<<"\n";
          
    }  */
    
    //return 0;
}
