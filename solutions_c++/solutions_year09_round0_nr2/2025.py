#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<vector>
#include<cmath>
#include<ctime>
#include<algorithm>
#include <map>

using namespace std;
#define SZ(v) ((int)v.size())
#define FOR(i,b,e) for(int i = b;i < e; ++i)
#define REP(i,v) FOR(i,0,SZ(v))
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef vector<char> VC;
typedef long long int64;
typedef unsigned long long uint64;
const double pi=acos(-1.0);
const double eps=1e-11;
#define zero(x) memset(&x, 0, sizeof x);

int T,H,W;
int lmap[100][100];
char lab[100][100];
char mk='a';
int der[4][2]={-1,0,0,-1,0,1,1,0};

char go(int ben0,int ben1){
	int n0,n1;
	int ls=lmap[ben0][ben1];
	int ls0=ben0,ls1=ben1;
	FOR(i,0,4) {
		n0=ben0+der[i][0];
		n1=ben1+der[i][1];
		if (n0>-1&&n0<H&&n1>-1&&n1<W){
			if (lmap[n0][n1]<ls) {ls0=n0;ls1=n1;ls=lmap[n0][n1];}
		}
	}
	if (ls0==ben0&&ls1==ben1) {lab[ben0][ben1]=mk;++mk;}
	else if (lab[ls0][ls1]!=0) lab[ben0][ben1]=lab[ls0][ls1];
	else lab[ben0][ben1]=go(ls0,ls1);
	return lab[ben0][ben1];
}


int mark(){
	int ben0,ben1;
	bool f=true;
	for(ben0=0;ben0<H;++ben0){
		for(ben1=0;ben1<W;++ben1)
			if (lab[ben0][ben1]==0) {f=false;break;}
			if (f==false) break;
	}
	if (f) return 0;
	else{
	
		go(ben0,ben1);
	}
	return 1;
}
int main(){

	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>T;
	FOR(k,0,T){
		mk='a';
		cin>>H>>W;
		FOR(i,0,H)
			FOR(j,0,W)
				cin>>lmap[i][j];
		zero(lab);
		while (mark()==1){}
		cout<<"Case #"<<k+1<<":"<<endl;
		FOR(i,0,H){
			FOR(j,0,W-1)
				cout<<lab[i][j]<<' ';
			cout<<lab[i][W-1]<<endl;
		}
	
	
	}


	return 0;

}