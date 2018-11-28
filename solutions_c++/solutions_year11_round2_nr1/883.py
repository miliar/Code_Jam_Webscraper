#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
using namespace std;

#define rep(i,a,b) for(typeof(a) i=(a);i<(b);i++ )
#define ll long long int
#define ii pair<int,int>
#define CLEAR(x,val) memset(x,val,sizeof(x))
#define SZ(v) (v).size()


int main()
{
	int cs = 1;
	int a[201][201];
	double wp[201];
	double owp[201];
	double oowp[201];
	double rep[201];
	double totl[201];
	int n , test;char ch;
	cin >> test;
	while( test-- ) {
		cin >> n;
		rep( i , 0 , 101  ) {wp[i] = 0.0 , owp[i] = 0.0 , oowp[i] = 0.0 , rep[i] = 0.0;} 
		rep( i ,0 , n ) 
			rep( j , 0 , n ) {
				cin >> ch;
				if( ch == '.') a[i][j] = 2;
				else a[i][j] = ch-'0';
			}
		
		rep( i , 0 , n ) {
				int tot = 0 , wn = 0;
				rep( j , 0 , n )  {
					if(a[i][j] == 1){ wn++;tot++;}
					if(a[i][j] == 0 ){ tot++;}
				}
				wp[ i ] = (double)(wn*1.0);	
				totl[ i ] = (double)(tot*1.0);
		}

		rep( i , 0 , n ) {
				double wn = 0.0;double tot = 0.0;
				rep( j , 0 , n ) { if( a[i][j] == 1 ) {
						wn += (wp[j]  )/(totl[j]-1.0);
						tot = tot + 1.0;
						}
						else if( a[i][j] == 0 ) { wn += (wp[j]-1.0)/(totl[j]-1.0);tot = tot+1.0;}
					}
			owp[i] =  wn / tot;
		}
		rep( i , 0 , n ) wp[ i ] = wp[i] / totl[i];
		rep( i , 0 , n ) {
			 int tot = 0;double wn = 0.0;
                        rep( j , 0 , n ) if(a[i][j]== 1 || a[i][j]==0 ) {tot++; wn+=owp[j];}
                        oowp[i] =  wn/(double)(tot*1.0);
		}	
		rep( i ,0 , n ) {
			rep[i] = 0.25*wp[i] + 0.50*owp[i] + 0.25*oowp[i];
		}
		printf("Case #%d:\n",cs++);
		rep( i , 0 , n ) cout<<rep[i]<<endl;	
	}
	return 0;
}
