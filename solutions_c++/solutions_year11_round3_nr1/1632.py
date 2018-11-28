#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <sstream>
#include <vector>
using namespace std;
#define DEBUG if(0)
#define FOR(i,a,x)  for(int i=a; i<(x); i++)
#define For(i,x) FOR(i,0,x)
#define CLR(x,a) memset(x,a,sizeof(x))

typedef vector<string> vs;
typedef vector<int> vi;
typedef long long ll;

#define FORALL(i,x) for(i=(x).begin();i!=(x).end();i++)
#define ALL(x) (x).begin(),(x).end()
#define pb push_back
#define sz(x) (int)(x).size()
vs pic;
int R,C;
bool check(int i, int j){
	if(i+1==R) return false;
	if(j+1==C) return false;
	return (pic[i][j+1]=='#' && pic[i+1][j]=='#' && pic[i+1][j+1]=='#');
}

ostream& operator<<(ostream& os,vector<string> v){
	if(v.size()==0) cout<<"NULL";
	for ( vector<string>::iterator it=v.begin() ; it != v.end(); it++ ) os <<*it<<endl ;
	return os;
}

void replace(int i,int j){
	pic[i][j]='/';
	pic[i+1][j]='\\';
	pic[i+1][j+1]='/';
	pic[i][j+1]='\\';
}
	
vector<string> solve(){
	vs ans;
	For(i,R){
		For(j,C){
			if(pic[i][j]=='#'){
				if(check(i,j)) replace(i,j);
				else {
					ans.pb("Impossible");
					return ans;
				}
			}
		}
	}
	return pic;
}

int main(){
	int T;
	fstream ps("statement.txt");
	fstream output("output.txt",fstream::trunc | fstream::out);
	ps>>T;
	int i=1;
	while(i!=T+1){
		pic.clear();
		ps>>R>>C;
		For(k,R){
			string row;
			ps>>row;
			pic.pb(row);
		}
	 output<<"Case #"<<i<<": "<<endl<<solve();
	 i++;	
	}		
	return 0;
}	
