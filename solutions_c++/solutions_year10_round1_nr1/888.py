#include <fstream>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <string>
#define debug(x) cout<<#x<<' '<<x<<endl;
#define INF 1000000
#define MAXN 1000000
#define forn(i,n) for(int i=0; i<(int)(n); i++)
using namespace std;

vector <string>v;
string s;

int main(){
	ifstream in("a.in");
	ofstream out("a.out");
	int T, n, k, w=0;
	in>>T;
	//out<<T<<endl;
	while(w<T){
		w++;
		v.clear();
		in>>n>>k;
		forn(i,n){
			in>>s;
			v.push_back(s);
			}
		
		forn(i,n){
			int pos=n-1;
		for(int j=n-1; j>=0; j--){
			if(v[i][j]!='.'){swap(v[i][j], v[i][pos--]);}
			}
		}
		/*
		forn(i,n){
			out<<v[i]<<endl;
			}
		}
		*/
		
		bool rw=false, bw=false;
		forn(i,n)
		forn(j,n){
			if(v[i][j]=='R'){
				int x, y;
				x=1; y=1;
				while(i-x>=0 && v[i-x][j]=='R')x++;
				while(i+y<n && v[i+y][j]=='R')y++;
				if(x+y-1>=k)rw=true;

				x=1; y=1;
				while(j-x>=0 && v[i][j-x]=='R')x++;
				while(j+y<n && v[i][j+y]=='R')y++;
				if(x+y-1>=k)rw=true;

				x=1; y=1;
				while(j-x>=0 && i-x>=0 && v[i-x][j-x]=='R')x++;
				while(j+y<n && i+y<n && v[i+y][j+y]=='R')y++;
				if(x+y-1>=k)rw=true;

				x=1; y=1;
				while(j-x>=0 && i+x<n && v[i+x][j-x]=='R')x++;
				while(j+y<n && i-y>=0 && v[i-y][j+y]=='R')y++;
				if(x+y-1>=k)rw=true;
				}

			if(v[i][j]=='B'){
				int x, y;
				x=1; y=1;
				while(i-x>=0 && v[i-x][j]=='B')x++;
				while(i+y<n && v[i+y][j]=='B')y++;
				if(x+y-1>=k)bw=true;

				x=1; y=1;
				while(j-x>=0 && v[i][j-x]=='B')x++;
				while(j+y<n && v[i][j+y]=='B')y++;
				if(x+y-1>=k)bw=true;

				x=1; y=1;
				while(j-x>=0 && i-x>=0 && v[i-x][j-x]=='B')x++;
				while(j+y<n && i+y<n && v[i+y][j+y]=='B')y++;
				if(x+y-1>=k)bw=true;

				x=1; y=1;
				while(j-x>=0 && i+x<n && v[i+x][j-x]=='B')x++;
				while(j+y<n && i-y>=0 && v[i-y][j+y]=='B')y++;
				if(x+y-1>=k)bw=true;
				}


			}
			out<<"Case #"<<w<<": ";
			if(rw && bw)out<<"Both"<<endl;
			if(rw && !bw)out<<"Red"<<endl;
			if(!rw && bw)out<<"Blue"<<endl;
			if(!rw && !bw)out<<"Neither"<<endl;
		}
}

