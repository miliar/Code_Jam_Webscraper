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


#define INF 1000000 
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


int L,D,N;
string d[5005];


int cmp(string s,string m){

	int j=0;
	FOR(i,L){
		if(m[j]=='('){
			j++;
			bool f=false;
			while(m[j]!=')'){	
				if(m[j]==s[i]){f=true;break;}
				j++;
			}
			if(!f) return 0;
			while(m[j]!=')')j++;
			j++;
			continue;
		}	
		if(s[i]!=m[j]) return 0;
		j++;
	
	}

	return 1;
}

int main(int argc,char** argv){
	istream* tstream=&cin;
	if(argc==1) tstream=new ifstream("C:\\Documents and Settings\\Maksim Piriyev\\Desktop\\in.txt");
	istream& in=(*tstream);
	//istream& in=cin;
	in>>L>>D>>N;
	FOR(i,D) in>>d[i];
	FOR(i,N){
		string ss;
		in>>ss;
		int count=0;
		FOR(j,D){
			count+=cmp(d[j],ss);
		}		
		cout<<"Case #"<<(i+1)<<": "<<count;
		cout<<endl;	
	}
	

	
}
