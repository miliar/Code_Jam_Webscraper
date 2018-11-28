#include <iostream>
using namespace std;
#include <cstdio>
#include <algorithm>
#include <deque>
#include <map>
#include <set>
typedef pair<int,int> pii;
#include <vector>
typedef vector<int> vi;
#include <queue>
#include <stack>
#define For(i,a,b) for(int i=(a);i<(b);++i)

#define ForI(i,a,b) for(int i=(a);i<=(b);++i)
#define ForAll(it,set) for(typeof(set.begin()) it = set.begin(); it!=set.end(); ++it)

typedef stack<int> si;
typedef queue<int> qi;


int main(){
	int t;
	cin>>t;
	ForI(tt,1,t){
		int n;cin>>n;
		string s[n];
		For(i,0,n) cin>>s[i];
		double wp[n], owp[n], oowp[n];
		int games[n];
		For(i,0,n)wp[i] = owp[i] = oowp[i]=games[i]=0;
		For(i,0,n){
			For(j,0,n)
				if(s[i][j] != '.'){
					games[i]++;
					wp[i] += (s[i][j] == '1'?1:0);			
				}
			wp[i] /= games[i];
		}
		
		For(i,0,n){
			double sum = 0;
			For(j,0,n){
				if(s[i][j] != '.' ){
					sum += (wp[j] * games[j] - (s[j][i] == '1'?1:0))/(games[j] - 1);
				}			
			}
			owp[i] = sum/games[i];
		}
		For(i,0,n){
			double sum = 0;
			For(j,0,n)
				if(s[i][j] != '.'){
					sum += owp[j];
				}
			oowp[i] = sum/games[i];
		
		}
		cout<<"Case #"<<tt<<":"<<endl;
		#define debug(a) 
		//cerr<<#a" = "<<(a)<<endl;
		For(i,0,n){
			debug(wp[i]);
			debug(owp[i]);
			debug(oowp[i]);
			double score = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
			printf("%.14lf\n",score);
			
		}
	
	}

	return 0;
}
