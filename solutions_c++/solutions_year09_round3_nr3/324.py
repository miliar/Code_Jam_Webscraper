#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include<cstdlib>
#include<cstring>
#include<string>


using namespace std;

#define pb push_back
#define sz size
#define all(a)  a.begin(),a.end()
#define SZ(v) ((int)(v).size())
#define gcj_print(ans) {cout << "Case #" << ((test)+1) << ": " << (ans) << endl;}


typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef vector<string> vs;
typedef long long  ll;

int main()
{
   int t,test=0;
   cin>>t;
   while(t--)
   {
      int p,q;
      cin>>p>>q;
      vector<int> cell(q);
      for(int i=0;i<q;i++)cin>>cell[i];
      int ans=10000000;
      
      do{
         
         int cal=0;
         int pp[500];for(int j=0;j<500;j++)pp[j]=1;
         for(int i=0;i<q;i++)
         {
            pp[cell[i]]=0;
            //for(int j=1;j<=p;j++)if(pp[j]==1)cal++;
            for(int j=cell[i]+1;j<=p && pp[j]==1;j++)cal++;
            for(int j=cell[i]-1;j>0 && pp[j]==1;j--)cal++;
            
         }
         if(cal<ans)ans=cal;
        
        } while(next_permutation( all(cell) ));
        
        cout << "Case #" << ((test)+1) << ": " << (ans) << endl;
        test++;
    }     
        
   
      
      
   return 0;
}   
