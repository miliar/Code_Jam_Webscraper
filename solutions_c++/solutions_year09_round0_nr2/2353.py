#include <map>
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


using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int,int> pii;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()
#define FOREACH(it, X) for(__typeof(X.begin()) it = X.begin(); it != X.end(); ++it)
#define present(container, element) (container.find(element) != container.end()) 
#define cpresent(container, element) (find(All(container),element) != container.end()) 



template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

const double pi = 2*acos(0.0);
const double eps = 1e-9;

int s2i(string &s){
  int x;
  sscanf(s.c_str(), "%d", &x);
  return x;
}
        /* 
        vector<string> nazwy;
        
        string s;
        int n=0;
        while (1){
      cin >> s;
      if (!isdigit(s[0])) nazwy.pushback(s);
      else break;
    }
    ceny[0]=atoi(s.c_str());
    */
int findsink(int x, vector< vi > &sink, vector< vi > &trusink, int w )
{
     if( trusink[x/w][x%w] ==-1)
     {
          if(sink[x/w][x%w] != -1)
                                trusink[x/w][x%w] = findsink( sink[x/w][x%w], sink, trusink, w);
          
          else
                                trusink[x/w][x%w] = x;
          }
     
     return trusink[x/w][x%w];
     }


int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int t;
	scanf("%d", &t);
	For(test, 1, t) {
                int h,w;
             cin>>h>>w;
             
              vector< vi > drain(h,vi(w,0)), alt(h,vi(w,0)), sink(h,vi(w,0)),trusink(h,vi(w,-1)) ;
            
             For(i,0,h-1)
                         For(j,0,w-1)
                                     cin>>alt[i][j];
                                     
             ;
             For(i,0,h-1)
             {
                         For(j,0,w-1)
                         {
                                     if( ( i ? (alt[i][j]<=alt[i-1][j]):1 ) && ( j ? (alt[i][j]<=alt[i][j-1]):1 )&& ( (i<h-1) ? (alt[i][j]<=alt[i+1][j]):1 )&& ( (j<w-1) ? (alt[i][j]<=alt[i][j+1]):1 ) )
                                     {
                                         sink[i][j] =-1;
                                         continue;
                                         
                                         }
                                     if(i)
                                     if( ( (j)? (alt[i-1][j]<=alt[i][j-1]):1 ) && ( ((j<w-1)) ? (alt[i-1][j]<=alt[i][j+1]):1 )&& ( ((i<h-1) ) ?(alt[i-1][j]<=alt[i+1][j]):1 ) )
                                     {
                                         sink[i][j] = ((i-1)*w)+j;
                                         continue;
                                         
                                         }
                                     if(j)
                                     if( ( (i ) ? (alt[i][j-1]<=alt[i-1][j]):1 ) && ( ( (j<w-1)) ? (alt[i][j-1]<=alt[i][j+1]):1 )&& ( ((i<h-1)) ?(alt[i][j-1]<=alt[i+1][j]):1 ) )
                                     {
                                         sink[i][j] = ((i)*w)+j-1;
                                         continue;
                                         
                                         }
                                    if(j<w-1)     
                                      if( ( (i  ) ? (alt[i][j+1]<=alt[i-1][j]):1 ) && ( (j ) ? (alt[i][j+1]<=alt[i][j-1]):1 )&& ( ((i<h-1)  ) ?(alt[i][j+1]<=alt[i+1][j]):1 ) )
                                     {
                                         sink[i][j] = ((i)*w)+j+1;
                                         continue;
                                         
                                         }
                                     if(i<h-1)
                                      if( ( (i ) ? (alt[i+1][j]<=alt[i-1][j]):1 ) && ( (  (j<w-1)) ? (alt[i+1][j]<=alt[i][j+1]):1 )&& ( (  j) ?(alt[i+1][j]<=alt[i][j-1]) :1 ) )
                                     {
                                         sink[i][j] = ((i+1)*w)+j;
                                         continue;
                                         
                                         }                                  
                                     
                                     
                                     }
             
                                     }
        
        /*
              For(i,0,h-1)
              {
                         cout<<"\n";
                         For(j,0,w-1)
                                     cout<<sink[i][j]<<" ";
                                     }*/
        vi basins(1, trusink[0][0] );
        For(i,0,h-1)
              {
                    For(j,0,w-1)
                    {
                                        findsink( (i*w)+j, sink, trusink, w);
                                                                        
                                        }
                                
                    }
        
        For(i,0,h-1)
                    For(j,0,w-1)
                    {
                                
                                
                                }
        

        
  		printf("Case #%d:\n", test);           
              For(i,0,h-1)
              {
                         
                         For(j,0,w-1)
                         {
                                     if(j) cout<<" ";
                                     if(find( All(basins), trusink[i][j]) == basins.end())
                                     {
                                              basins.push_back(trusink[i][j]);
                                              
                                              }
                                     cout<< char((find( All(basins), trusink[i][j]) -basins.begin() )+ 'a'-1);
                                     
                                     }
                                     
                                     cout<<"\n";
                                     }
	
		
		
		
		
		
		
		
		
//		printf("Case #%d: %d %d\n", test, r1, r2);
	}

	exit(0);
}
