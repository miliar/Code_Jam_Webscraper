#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <cstdlib>
#include <utility>

using namespace std;


#define INF 10005 
#define FOR(i,n) for(int i=0;i<(n);i++)
#define FILL(a) memset(a,0,sizeof(a))
#define FILL1(a) memset(a,-1,sizeof(a))
#define FILL2(a) memset(a,INF,sizeof(a))
#define MAX 10005
typedef pair<int,int> pii;
typedef pair<int,pair<int,int> > ppi;
typedef vector<pii > VP;
typedef priority_queue<ppi > PQ;
typedef vector<string> VS;
typedef long double ld;
typedef long long ll;
int bitc(ll r) {return r == 0 ? 0 : (bitc(r>>1) + (r&1));}
ll gcd(ll x, ll y) {return x>0 ? gcd(y%x,x) : y;}

//template<class T> T& operator >?= (T& x, T y) {if(y>x) x=y; return x;}
//template<class T> T& operator <?= (T& x, T y) {if(y<x) x=y; return x;}
//template<class T> T operator >? (T x, T y) {return x>y?x:y;}
//template<class T> T operator <? (T x, T y) {return x<y?x:y;}


int L,N;
int d[600][20];
string m="welcome to code jam";
int solve(string s){
	L=s.size();
	FILL(d);
	for(int i=L-1;i>=0;i--){
		FOR(j,m.size()){
			if(m[j]==s[i]){
				if(j==m.size()-1){
					d[i][j]=1;
					continue;
				}
				int& t=d[i][j];
				for(int k=i;k<L;k++){
					t=(t+d[k][j+1])%10000;		
				
				}					
			}		
		}	
	}

	int count=0;
	FOR(i,L)count=(count+d[i][0])%10000;
	return count;
}

int main(int argc,char** argv){
	istream* tstream=&cin;
	if(argc==1) tstream=new ifstream("C:\\Documents and Settings\\Maksim Piriyev\\Desktop\\in.txt");
	istream& in=(*tstream);
	//istream& in=cin;
	in>>N;
	string ss;
	getline(in,ss);			
	FOR(i,N){	
		getline(in,ss);			
		int ans=solve(ss);
		cout<<"Case #"<<(i+1)<<": ";
		char p[12];
		sprintf(p,"%4d",ans);
		//p[4]=0;
		FOR(j,4)if(p[j]==' ')p[j]='0';
		printf("%s\n",p);
		
		
	}
	

	
}
