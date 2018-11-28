#include <cstdio>
#include <iostream>
#include <numeric>
#include <fstream>
#include <map>
#include <algorithm>
#include <bitset>
#include <set>
#include <vector>
#include <utility>
#include <cstring>
#include <string>
#include <cctype>
#include <cmath>
#include <climits>
using namespace std;
typedef vector<int> vi;
typedef vector< vi > vvi;
typedef pair<int,int> pi;
typedef vector< pi > vpi;
typedef vector< vpi > vvpi;
#define rep(i,a,b) for(i = a;i<=b;i++)
#define all(c) (c).begin(),(c).end()
#define present(c,x) (c).find(x)!=(c).end()
#define gpresent(c,x) find(all(c),x)
#define tr(c,it) for( vector<int>::iterator it = (c).begin();it!=(c).end();it++ )
#define accu(c) accumulate(all(c),0)
#define scalar(c1,c2) inner_product(all(c1),(c2).begin(),0)
#define maxel(c) max_element(all(c))
#define minel(c) min_element(all(c))
#define Size(C) C.size();
#define fx first
#define sx second
#define pb(a) push_back(a)
#define mp(a,b) make_pair(a,b)
#define inf -300010
#define ll long long
#define M 1000000007

ifstream in("A-small-attempt0.in",ios::in);
ofstream out("output.out",ios::out);

 int dot = 0,t,i,j,k,x = 0,o = 0,found = 0;
 char arr[6][6],c;

 int main(){
 	in>>t;
 	rep(i,1,t){
 		dot = 0;
 		found = 0;
 		rep(j,1,4){
 			rep(k,1,4){
 				in>>arr[j][k];
 				if(arr[j][k]=='.')
 					dot++;
 			}
 		}
 		//check rows
 		rep(j,1,4){
 			x  = o = 0;
 			rep(k,1,4){
				if(arr[j][k]=='X')
					x++;
				else if(arr[j][k]=='O')
					o++;
 			}
 			if(( x==0&&(o==3||o==4) ) || (o==0&&(x==3||x==4)) ){
 				found = 1;
 				if(x==0)
 					out<<"Case #"<<i<<":"<<' '<<'O'<<" won\n";
 				else
 					out<<"Case #"<<i<<":"<<' '<<'X'<<" won\n";
 				break;
 			}
 		}
 		
 		if(found)
 			continue;
 		
 		//check col
 		rep(k,1,4){
 			x = o = 0;
 			rep(j,1,4){
 				if(arr[j][k]=='X')
 					x++;
 				else if(arr[j][k]=='O')
 					o++;
 			}
 			if(( x==0&&(o==3||o==4) ) || (o==0&&(x==3||x==4)) ){
 				found = 1;
 				if(x==0)
 					out<<"Case #"<<i<<":"<<' '<<'O'<<" won\n";
 				else
 					out<<"Case #"<<i<<":"<<' '<<'X'<<" won\n";
 				break;
 			}
 		}
 		
 		if(found)
 			continue;
 		
 		x = o = 0;
 		// check right diagnol
 		for(k=1,j=1;j<=4;j++,k++){
 			if(arr[j][k]=='X')
 				x++;
 			else if(arr[j][k]=='O')
 				o++;
 		}
 		
 		if(( x==0&&(o==3||o==4) ) || (o==0&&(x==3||x==4)) ){
 				found = 1;
 				if(x==0)
 					out<<"Case #"<<i<<":"<<' '<<'O'<<" won\n";
 				else
 					out<<"Case #"<<i<<":"<<' '<<'X'<<" won\n";
 				continue;
		}
		x = o = 0;
		
		//check left diagnol
		for(j = 1,k = 4;j<=4;j++,k--){
			if(arr[j][k]=='X')
				x++;
			else if(arr[j][k]=='O')
				o++;
		}
 		if(( x==0&&(o==3||o==4) ) || (o==0&&(x==3||x==4)) ){
 				found = 1;
 				if(x==0)
 					out<<"Case #"<<i<<":"<<' '<<'O'<<" won\n";
 				else
 					out<<"Case #"<<i<<":"<<' '<<'X'<<" won\n";
 				continue;
		}
		
 		//neither of them won.
 		if(dot==0)
 			out<<"Case #"<<i<<":"<<" Draw\n";
 		else
 			out<<"Case #"<<i<<":"<<" Game has not completed\n";
 		
 	}
 
 return 0;
 }
