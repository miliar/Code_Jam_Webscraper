#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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

using namespace std;


char p[51][51];

int main() 
{
	
	freopen("C:/TestData/A-large.in","r",stdin);
	freopen("C:/TestData/A.out","w",stdout);
	int t; 
	cin>> t; 
	int r,c;
	for( int ti  =1 ; ti<= t ;ti++) {
		cin>>r>>c;
		cout<<"Case #"<<ti<<":"<<endl;
		memset(p,'.',51*51);
		for( int i = 0 ;i<r;i++ ) { 
			for( int j =0 ;j<c;j++ ) { 
				cin>>p[i][j];	
			}
		}

		for(int i =0;i<r;i++) {
			for(int j=0;j<c;j++) {
				if( p[i][j]=='#') {
					if ( p[i][j+1]=='#' && p[i+1][j] == '#' && p[i+1][j+1] == '#' ) {
						p[i][j]= p[i+1][j+1] = '/';
						p[i+1][j] = p[i][j+1]='\\';
					} 
					else {
						cout<<"Impossible"<<endl;
						goto over;
					}
				}
			}
		}

		for( int i = 0 ;i < r;i++ ) {
			for( int j = 0 ; j < c ; j++ ) {
				cout<<p[i][j];
			}
			cout<<endl;
		}
		over:;

	}
	//system("PAUSE");
	
}




