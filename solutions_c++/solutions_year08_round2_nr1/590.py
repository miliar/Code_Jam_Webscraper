/*#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
*/

#include <stdio.h>
#include <conio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <limits.h>
#include <string.h>
#include <list>
using namespace std;

#define FOR(v,f) for(int (v)=0;(v)<(f);(v)++)
#define FORS(v,f,s) for(int (v)=0;(v)<(f);(v)=(v)+s)
#define FORI(type,cont,var) for ( type::iterator (var)=(cont).begin(); (var)!=(cont).end(); ++(var))

//#define DEBUG               



typedef pair <long long, long long>  tpc;

template <typename T> inline int minOf(T *min, T i)
{
       if (i<*min) *min = i;
       return (i<*min);
}

int main(void)
{
   int N;
   
	freopen("c:\\GJam\\Round1B\\A-small-attempt0.in", "rt", stdin);
	freopen("c:\\GJam\\Round1B\\A-small.out", "wt", stdout);


	//freopen("c:\\GJam\\Round1B\\A-small.in", "rt", stdin);
	//freopen("c:\\GJam\\Round1B\\A-small.out", "wt", stdout);

	//freopen("c:\\GJam\\Round1B\\A-large.in", "rt", stdin);
	//freopen("c:\\GJam\\Round1B\\A-large.out", "wt", stdout);
	
	
   cin >> N;

   FOR(icase,N)
   {       
        long long n, A, B, C, D, x0, y0, M;
        //long X = x0, Y = y0;
        
        cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;    
                        
        vector < tpc > vc;
        tpc pc;
        
        long long X = x0, Y = y0;
        pc.first = X; pc.second = Y;
        vc.push_back(pc);
        

        #ifdef DEBUG               
                cout << "(" << vc[0].first << "," << vc[0].second << ") ";
        #endif

        
        //print X, Y
        //for i = 1 to n-1
        FOR(itree,n-1)
        {
                X = (A * X + B) % M;
                Y = (C * Y + D) % M;

                pc.first = X; pc.second = Y;
                vc.push_back(pc);
                
        #ifdef DEBUG               
                cout << "(" << vc[itree+1].first << "," << vc[itree+1].second << ") ";
        #endif
                
        }
         
        long count = 0; 
        for (long i=0; i<n-2; i++)
        {
            for (long j=i+1; j<n-1; j++)
            {
                 for (long k=j+1; k<n; k++)
                 {
                     if ( (vc[i].first + vc[j].first + vc[k].first)%3 == 0 )
                       if ( (vc[i].second + vc[j].second + vc[k].second)%3 == 0 )
                          count++;
                 }    
            }
        } 
         
         
/*        for ( vector <tpc>::iterator it1=vc.begin(); it1!=vc.end(); ++vc)
        {
            for ( vector <tpc>::iterator it2=it1; it2!=vc.end(); ++vc)
            {
                for ( vector <tpc>::iterator it1=vc.begin(); it1!=vc.end(); ++vc)
                {
                    
                    
                    
                }
                
            }
            
            
        }      
              
 */             
              
   
   
   
   
   
        //cout << endl;       
        
        
        
 
    
                  
        cout << "Case #" << icase+1 << ": " << count << endl;
   }                 
   
}
           
           
           
           
           
           
           
           
           
           
           
           
           
