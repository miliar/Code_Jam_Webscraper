#include <fstream>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <string>
//#include "BigIntegerLibrary.hh"

#define debug(x) cout<<#x<<' '<<x<<endl;
#define INF 1000000
#define MAXN 1000000
#define forn(i,n) for(int i=0; i<(int)(n); i++)
using namespace std;

int tab[128][128][2];

int main(){
	ifstream in("c.in");
	ofstream out("c.out");
	int T, w=0, x1, x2, y1, y2;
	in>>T;

	while(w<T){
		w++;
		forn(i,128)forn(j,128)tab[i][j][0]=0;
		
		int r;
		in>>r;
		forn(i,r){
			in>>x1>>y1>>x2>>y2;
			for(int j=x1; j<=x2; j++)
			for(int k=y1; k<=y2; k++)tab[j][k][0]=1;
			}
		
		int cnt=0;
		for(int i=1; i<=100; i++)
		for(int j=1; j<=100; j++)if(tab[i][j][0]==1)cnt++;
		
		int tmp=0;
		while(cnt>0){
			tmp++;

			for(int i=1; i<=100; i++)
			for(int j=1; j<=100; j++){
				tab[i][j][tmp%2]=tab[i][j][(tmp+1)%2];
				if(tab[i-1][j][(tmp+1)%2]==0 && tab[i][j-1][(tmp+1)%2]==0){tab[i][j][tmp%2]=0;if(tab[i][j][(tmp+1)%2]==1)cnt--;}
				if(tab[i-1][j][(tmp+1)%2]==1 && tab[i][j-1][(tmp+1)%2]==1){tab[i][j][tmp%2]=1;if(tab[i][j][(tmp+1)%2]==0)cnt++;}
				}
			
			}
		out<<"Case #"<<w<<": ";
		out<<tmp<<endl;
		}
}

