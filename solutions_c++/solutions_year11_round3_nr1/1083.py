#include <iostream>
using namespace std;

#define forn(i, n) for(int i=0; i<(int)n; i++)

char a[100][100];
int main(){
	int T;
	int n, m;

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	cin>>T;
	forn(q, T){
		cout<<"Case #"<<q+1<<":"<<endl;
		cin>>n>>m;

		forn(i, n) cin>>a[i];
		
		bool ok=true;
		forn(i, n)forn(j, m){
			if(a[i][j]=='#'){
				if(i+1<n && j+1<m && a[i+1][j]=='#' && a[i+1][j+1]=='#' && a[i][j+1]=='#'){
					a[i][j]='/'; a[i+1][j]='\\'; a[i+1][j+1]='/'; a[i][j+1]='\\';
				}
				else {ok=false; break;}
			}
		}

		if(!ok) cout<<"Impossible"<<endl;
		else{
			forn(i, n) cout<<a[i]<<endl;
		}
	}

	return 0;
}