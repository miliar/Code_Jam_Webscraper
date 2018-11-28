/* @author
 * bond, s_bond, sidhs
*/
#include <iostream>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <algorithm>
#include <cstring>
#include <fstream>
#include <bitset>
#include <set>
#include <cmath>
#include <time.h>
#include <string.h>
#include <stdio.h>
#include <cstdio>
#include <assert.h>
#include <functional>
/////////////////
#define GI ({int t;scanf("%d",&t);t;})
#define GL ({long long int t;scanf("%I64d",&t);t;})
#define PInt(a) printf("%d\n",(a))
#define PLng(a) printf("%I64d\n",(a))
#define FOR(i,a,b) for((i)=(a);(i)<(b);i++)
#define FORR(i,b,a) for((i)=(b);(i)>=(a);(i)--)
#define FORV(i,v) for((i)=0;(i)<v.size();i++)
#define All(v) v.begin(),v.end()
#define BS(v,val) (lower_bound(All(v),val)-v.begin())
#define pb(a) push_back((a))
#define Clear(a) memset((a),0,sizeof(a))
#define SV(v) sort((v).begin(),(v).end())
#define SA(a,n) sort((a),(a)+(n))
#define mp make_pair
#define IT ::iterator
using namespace std;
typedef long long int LL;
typedef unsigned long long int ULL;
typedef vector<int> vi;
typedef vector<LL> vl;
typedef vector<char> vc;
typedef vector<string> vs;
typedef map<int,int> mii;
typedef map<char,int> mci;
typedef map<string,int> msi;
typedef pair<int,int> pii;
typedef vector<pii> vp;
typedef vector< vector<int> > vvi;
typedef pair <int, long > pil;
typedef pair <long, long > pll;
typedef set <int> si;
typedef set <LL> sl;
typedef priority_queue <int> PQ;
/////////////////
int N, M, K;
void _file(){
	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);
	}
char ch[5][5];
int X[5][5], O[5][5];
bool o_won, x_won;
int main () {
	int i, j, k, t, _case=1, dot ;
	_file();
	t = GI;
	while(_case<=t){
		
		FOR(i,0,4) cin >> ch[i];
		dot = 0;
		cout<<"Case #"<<_case<<": ";
		FOR(i,0,4) FOR(j,0,4) if(ch[i][j]=='.') dot++;
		
			o_won = x_won = false;
			Clear(O);Clear(X);
			FOR(i,0,4){//Horizontal 
				FOR(j,0,4){
						
						if(ch[i][j]=='O' ){
							O[i][j] = O[i][j-1>=0?j-1:0] + 1;
							}
						else if(ch[i][j]=='X'){
							X[i][j] = X[i][j-1>=0?j-1:0] + 1;
							}
						else if(ch[i][j]=='T'){
							O[i][j] = O[i][j-1>=0?j-1:0] + 1;
							X[i][j] = X[i][j-1>=0?j-1:0] + 1;
							}
							
					}
				}
			FOR(i,0,4){	
				if(O[i][3]==4) o_won = true;
				if(X[i][3]==4) x_won = true;
				}
			Clear(O);Clear(X);
			
			FOR(i,0,4){//Vertical
				FOR(j,0,4){
					if(ch[i][j]=='O'){
						O[i][j] = O[i-1>=0?i-1:0][j] + 1;
						}
					else if(ch[i][j]=='X'){
						X[i][j] = X[i-1>=0?i-1:0][j] + 1;
						}
					else if(ch[i][j]=='T'){
						O[i][j] = O[i-1>=0?i-1:0][j] + 1;
						X[i][j] = X[i-1>=0?i-1:0][j] + 1;
						}	
					}
				}						
			FOR(i,0,4){	
				if(O[3][i]==4) o_won = true;
				if(X[3][i]==4) x_won = true;
				}
			
			Clear(O);Clear(X);
			FOR(i,0,4){//Main diagonal
				if(ch[i][i]=='O'){
					O[i][i] = O[i-1>=0?i-1:0][i-1>=0?i-1:0] + 1;
					}
				else if(ch[i][j]=='X'){
					X[i][j] = X[i-1>=0?i-1:0][i-1>=0?i-1:0] + 1;
					}
				else if(ch[i][j]=='T'){
					O[i][i] = O[i-1>=0?i-1:0][i-1>=0?i-1:0] + 1;
					X[i][j] = X[i-1>=0?i-1:0][i-1>=0?i-1:0] + 1;					
					}
				}
			if(O[3][3]==4) o_won = true; if(X[3][3]==4) x_won = true;
			
			Clear(O);Clear(X);
			FOR(i,0,4){// secondry diagonal
				
				if(ch[i][3-i]=='O'){
					O[i][3-i] = O[i-1>=0?i-1:0][3-i+1<4?3-i+1:3] + 1;
					}
				else if(ch[i][3-i]=='X'){
					X[i][3-i] = X[i-1>=0?i-1:0][3-i+1<4?3-i+1:3] + 1;
					}
				else if(ch[i][3-i]=='T'){
					O[i][3-i] = O[i-1>=0?i-1:0][3-i+1<4?3-i+1:3] + 1;
					X[i][3-i] = X[i-1>=0?i-1:0][3-i+1<4?3-i+1:3] + 1;
					}
				
				}
			
			if(O[3][0]==4)o_won = true; if(X[3][0]==true)x_won;
			
			if(x_won) cout<<"X won\n";
			else if(o_won) cout<<"O won\n";
			else if(dot>0) cout<<"Game has not completed\n";
			else	cout<<"Draw\n";
			
			
		_case++;
		}
	return 0;
}