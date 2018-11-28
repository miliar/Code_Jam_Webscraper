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

#define REP(i,a,b) for(typeof(a) i=(a);i<(b);i++)
#define ll long long int
#define ii pair<int,int>
#define CLEAR(x,val) memset(x,val,sizeof(x))
#define SZ(v) (v).size()


int main()
{
	int  t , cs = 1;char ch;
	cin >> t;int r ,c;
	char a[52][52];
	string s = "\\";
//	cout<<s<<endl;	
	while(t--) {
		cout<<"Case #"<<cs<<":"<<endl;cs++;
		cin >> r >> c;
		REP( i , 0 , r ) REP( j , 0 ,  c ) {cin>>ch;a[i][j] = ch;}
		bool f = 1;
		REP( i , 0 , r ){
		f = 1;
		 REP( j , 0 , c ) {
			if(a[i][j]=='#') {
				if( (j+1 < c)&& (i+1<r)&&(a[i][j+1] == '#' )&&(a[i+1][j]=='#')&&(a[i+1][j+1]=='#')){
					a[i][j] = '/';a[i][j+1] = s[0];a[i+1][j]=s[0];;a[i+1][j+1]='/';
				}  
				else f = 0;
				}
			if(!f) break;
			}
			if(!f) break;
		}
		if(!f) printf("Impossible\n");
		else {
		REP( i ,0 , r ) {
			REP( j , 0 , c ) 
				cout<<a[i][j];
			cout<<endl;
		}
		}
	}
	return 0;

}
